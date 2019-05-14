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

First focus on $\epsilon$-neighborhood graphs(k-nearest-neighborhood would be better). Let $K:[0,\infty)\rightarrow [0,\infty)$
$$
K(r)=\left\{
\begin{aligned}
1,&if r\leq 1\\
0,&otherwise
\end{aligned}
\right.
$$


