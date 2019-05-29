This is a task to detect different objects(clusters). We are especially interested in different dimensional objects. This file contains code for simulating different objects and detecting.

## Stage 1 
Try a sphere and a line. First obtain eigenpairs for graph laplacian matrix(unnormalized) and make the plot.

Then try basic spectral clustering on data. Basic idea is to use first two eigenvectors corresponding to the first and second smallest eigenvalues. It do tell us something. An apparent line appears in one cluster which means we do detect a line among all data points. However, after checking the 3 axises, we only seperate a part of the line. This indicates this method only detect the existence of the line but not classifing two objects. 

## Stage 2
Add noise to the model. To be specific, add random gaussian turbulence to points.

### Todo
First. Split each objects into 2 parts, one is accurate and the other add gaussian turbulence and watch its behavior. Notice the accurate part still has properties we assume(different dimension), but the other part is both 3 dimensin for two objects.

Second. Add gaussian turbulence to lines and decrease variance gradually until we obtain similar results in stage 1.

### Discovery
First. The upper part of line is accurate while the other part of line contains noise~N(0,0.001). Do same to sphere. The plot of points colored with eigenvector corresponding to the second smallest eigenvalue exibits two colors: most of the accurate part of line appears to be yellow while the rest appears to be purple(color is just example, any two colors would be fine). This indicates the dectection of line. Then the basic spectural clustering do support this idea. We detect obvious line from the accurate part.

Second. Just add gaussian turbulence to the line. Let noise follow N(0,0.06).

More details in my report 1.

