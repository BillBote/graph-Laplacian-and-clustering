This is a task to detect different objects(clusters). We are especially interested in different dimensional objects. This file contains code for simulating different objects and detecting.

## Stage 1 
Try a sphere and a line. First obtain eigenpairs for graph laplacian matrix(unnormalized) and make the plot.

Then try basic spectral clustering on data. Basic idea is to use first two eigenvectors corresponding to the first and second smallest eigenvalues. It do tell us something. An apparent line appears in one cluster which means we do detect a line among all data points. However, after checking the 3 axises, we only seperate a part of the line. This indicates this method only detect the existence of the line but not classifing two objects. 


