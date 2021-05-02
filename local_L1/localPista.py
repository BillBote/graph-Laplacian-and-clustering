from __future__ import print_function
from __future__ import division

import numpy as np

from sklearn.base import BaseEstimator, ClassifierMixin, RegressorMixin
from sklearn.utils.extmath import safe_sparse_dot
from sklearn.isotonic import isotonic_regression
from sklearn.preprocessing import LabelBinarizer

from fista import fista
from loss import get_loss
from laplace import distance


def prox_l1(v, alpha):
    """L1 penality
  
    """
    v_abs = np.abs(v)

    return alpha*sum(v_abs)

def locality(X,y,v,beta):
    """Locality added to L1 regression

    """

    n=X.shape[1]
    s=0
    for i in range(n):
        s=s+distance(y,X[:,i])*v[i]
    return s*beta



def _fit_local_fista(X, y, alpha, beta, loss, max_iter=10000, max_linesearch=20, eta=2.0,
                   tol=1e-3, verbose=0):

    # least squares loss
    def sfunc(coef, grad=False):
        y_scores = safe_sparse_dot(X, coef)
        if grad:
            obj, lp = loss(y, y_scores, return_derivative=True)
            grad = safe_sparse_dot(X.T, lp)
            return obj, grad
        else:
            return loss(y, y_scores)

    def nsfunc(coef, L):
        return prox_l1(coef, alpha)+locality(X, y, coef, beta)

    coef = np.zeros(X.shape[1])
    return fista(sfunc, nsfunc, coef, max_iter, max_linesearch,
                 eta, tol, verbose)


class _BaseLocal(BaseEstimator):
    """

    Solves sum loss(y_pred, y) + sum_j weights_j |coef|_(j)
           where u_(j) is the jth largest component of the vector u.
           and weights is a monotonic nonincreasing vector.

    OWL is also known as: sorted L1 norm, SLOPE

    Parameters
    ----------

    weights: array, shape (n_features,) or tuple, length 2
        Nonincreasing weights vector for the ordered weighted L1 penalty.
        If weights = (alpha, 0, 0, ..., 0), this amounts to a L_inf penalty.
        If weights = alpha * np.ones(n_features) it amounts to L1.
        If weights is a tuple = (alpha, beta), the OSCAR penalty is used::
            alpha ||coef||_1 + beta sum_{i<j} max{|x_i|, |x_j|)
        by computing the corresponding `weights` vector as::
            weights_i = alpha + beta(n_features - i - 1)

    loss: string, default: "squared"
        Loss function to use, see loss.py to add your own.

    max_iter: int, default: 500
        Maximum FISTA iterations.

    max_linesearch: int, default: 20
        Maximum number of FISTA backtracking line search steps.

    eta: float, default: 2
        Amount by which to increase step size in FISTA bactracking line search.

    tol: float, default: 1e-3
        Tolerance for the convergence criterion.

    verbose: int, default 0:
        Degree of verbosity to print from the solver.

    References
    ----------
        X. Zeng, M. Figueiredo,
        The ordered weighted L1 norm: Atomic formulation, dual norm,
        and projections.
        eprint http://arxiv.org/abs/1409.4271
    """

    def __init__(self, alpha, beta, loss='squared', max_iter=10000,
                 max_linesearch=20, eta=2.0, tol=1e-3, verbose=0):
        self.alpha = alpha
        self.beta = beta
        self.loss = loss
        self.max_iter = max_iter
        self.max_linesearch = max_linesearch
        self.eta = eta
        self.tol = tol
        self.verbose = verbose

    def fit(self, X, y):

        n_features = X.shape[1]

        loss = self.get_loss()
        alpha = self.alpha
        beta = self.beta

        self.coef_ = _fit_local_fista(X, y, alpha, beta, loss, self.max_iter,
                                    self.max_linesearch, self.eta, self.tol,
                                    self.verbose)
        return self

    def _decision_function(self, X):
        return safe_sparse_dot(X, self.coef_)


class LocalRegressor(_BaseLocal, RegressorMixin):
    """Ordered Weighted L1--penalized (OWL) regression solved by FISTA"""
    __doc__ += _BaseLocal.__doc__

    def get_loss(self):
        if self.loss != 'squared':
            raise NotImplementedError('Only regression loss implemented '
                                      'at the moment is squared.')

        return get_loss(self.loss)

    def predict(self, X):
        return self._decision_function(X)


class LocalClassifier(_BaseLocal, ClassifierMixin):
    """Ordered Weighted L1--penalized (OWL) classification solved by FISTA"""
    __doc__ += _BaseLocal.__doc__
    def get_loss(self):
        return get_loss(self.loss)

    def fit(self, X, y):
        self.lb_ = LabelBinarizer(neg_label=-1)
        y_ = self.lb_.fit_transform(y).ravel()
        return super(LocalClassifier, self).fit(X, y_)

    def decision_function(self, X):
        return self._decision_function(X)

    def predict(self, X):
        y_pred = self.decision_function(X) > 0
        return self.lb_.inverse_transform(y_pred)

"""
if __name__ == '__main__':

    from sklearn.model_selection import train_test_split
    from sklearn.datasets import load_boston, load_breast_cancer

    print("OSCAR proximal operator on toy example:")
    v = np.array([1, 3, 2.9, 4, 0])
    w_oscar = _oscar_weights(alpha=0.01, beta=1, size=5)
    print(prox_owl(v, w_oscar))
    print()

    print("Regression")
    X, y = load_boston(return_X_y=True)
    X = np.column_stack([X, -X[:, 0] + 0.01 * np.random.randn(X.shape[0])])
    X_tr, X_te, y_tr, y_te = train_test_split(X, y, random_state=0)
    clf = OwlRegressor(weights=(1, 100))
    clf.fit(X_tr, y_tr)
    print("Correlated coefs", clf.coef_[0], clf.coef_[-1])
    print("Test score", clf.score(X_te, y_te))
    print()

    print("Classification")
    X, y = load_breast_cancer(return_X_y=True)
    X = np.column_stack([X, -X[:, 0] + 0.01 * np.random.randn(X.shape[0])])
    X_tr, X_te, y_tr, y_te = train_test_split(X, y, random_state=0)
    clf = OwlClassifier(weights=(1, 100), loss='squared-hinge')
    clf.fit(X_tr, y_tr)
    print("Correlated coefs", clf.coef_[0], clf.coef_[-1])
    print("Test score", clf.score(X_te, y_te))
"""