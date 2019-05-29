# graph-Laplacian-and-clustering

This project is my research project during master degree. I work on Graph Laplician and try to find some methods to detect objects inspiring from graph Laplacian and Spectrum clustering. And I will record some progress here and upload corresponding code.

## Task 1
Read paper *ON THE CONSISTENCY OF GRAPH-BASED BAYESIAN LEARNING AND THE SCALABILITY OF SAMPLING ALGORITHMS* and know what is Graph Laplacian. This is a theoretical part and I focus on discrete settings.

### Notation

$\mathcal{M}$: m-dimentional, compact, smooth, manifold embedded in $R^d$

$\mathcal{M}_n={x_1,...,x_n}$: i.i.d samples from uniform distribution on $\mathcal{M}$

$L^2(r):$ space of functions on underlying manifold, Square Integrable Functions in $L^2(r)$ can be writen in terms of the (normalized) eigenfunctions {$\phi_i$} of Laplacian Beltrami operator $\Delta_{\mathcal{M}}$.

### Settings

View functions $u_n \in L^2(r_n)$ as vectors in $R^n$. That is let $u_n=[u_n(1),...,u_n[n]]'$, $u_n(i)$ is evaluation of the function $u_n$ at $x_i$.

1. Geometric Graph and Graph-Laplacian

First focus on $\epsilon$-neighborhood graphs(k-nearest-neighborhood would be better). Let $K:[0,\infty)\rightarrow [0,\infty):$ $K(r)=1$ if $r\leq 1$. For $\epsilon>0$, $K_{\epsilon}(r)=\frac{m+2}{n^2\alpha_m\epsilon^{m+2}}K(\frac{r}{\epsilon})$. Here $\alpha_m$ denote the volume of the m-dimensional unit ball. Then the weight between $x_i,x_j\in\mathcal{M}_n$: $W_n(x_i,x_j)=K_{\epsilon}(|x_i-x_j|)$. Thus obtain Laplacian of the geometric graph:
$$
\Delta_{\mathcal{M}_n}=D_n-W_n
$$

$D_n$ is the degree matrix of weighted graph: $D_{ii}=\sum_{j=1}^nW_n(x_i,x_j)$. Let {$\lambda_i,\phi_i$} denote eigenvalues and eigenvectors in ascending order.

2.Graph prior

$u_n\sim \widetilde{\pi_n}=N(0,C_{u_n})$ and $C_{u_n}=(\alphaI_n+\Delta^{\mathcal{M}_n})^{-\frac{s}{2}}$. Then $u_n=\sum_{i=1}^{k_n}(\alpha+\lambda_i^n)^{-\frac{s}{4}}\xi_i\phi_i^n$, here $\xi_n\sim N(0,1)$

3.Graph $\mathcal{F}$ and observation map $\mathcal{O}$

$\mathcal{F}:L^2(r_n)\rightarrow L^2(r_n)$ $\mathcal{F}_nu_n=\mathcal{F}_n^tu_n=e^{-t\Delta_{\mathcal{M}_n}u_n}$

$\mathcal{O}_n:$ for $\delta>0$, $L^2(r_n)\rightarrow R^p$ for $W\in L^2(r_n)$. We do not talk abour its specific form here.

4.noise model

Add random noise to the model we mentioned above.

5. Graph Posterior

## Task 2

Plot of prior distribution and posterior distribution.

We have obtain the simpler form of prior distribution via Karhunen-Loeve expansion

## Task 3

1.Simulation of data: two different dimensional objects--a 3-dim sphere and a 2-dim line.

2.Detecting two objects or just one out via Laplacian operator.

3.Details:

* Using kNN connection to build weight matrix W and notice each node is of same weight;

* Build Laplacian matrix $\Delta$ from the weight matrix W;

* Gain eigenpairs of matrix $\Delta$ {$\lambda_i,\phi_i$} and notice $\lambda_1<\lambda_2<...$;

* One way: plot the original points and set the color as corresponding eigenvectors; another way: using K-means clustering to do clustering on eigenvectors.

## Task 4

Consider Spectral Clustering. 

This method is quite similar to Task 3. Read paper *A Tutorial on Spectral Clustering* to get more details.

## Task 5

Read paper *Path-Based Spectral Clustering: Guarantees, Robustness to Outliers, and Fast Algorithms*, *Scalable Sparse Subspace Clustering via Ordered Weighted l1 Regression* and slides *Data Dependent Distances for Unsupervised Learning*.

## Task 6

After finding out that the spectral method does work, more things could be done. Try more models with different objects. Try adding noise to models and test if this model is sensitive. Then try denoising procedure. 

Then here comes another problem. Only a part of line is detected, then how to recover the whole thing. Could I find out the nearest neighbors of the line and iterate the procedure? Give a try.
