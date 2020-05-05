# mnist-to-numpy-array

A simple program to read MNIST data files downloaded from http://yann.lecun.com/exdb/mnist/ and save them as numpy arrays which may 
be loaded using `numpy.load`.

 - Label files are stored as an array of bytes, one byte per label (i.e., an array of type `numpy.ubyte` of shape (N,), where N is the number of
 labels in the data file).

 - Image files are stored as a single array of shape (N, 28, 28), where N is the number of images in the data file.
 
 Once converted with this program, the files may be loaded: 
 
 ```
 labels = np.load('label_file.npy')
 images = npl.load('image_file.npy')
 
 # image[X] now contains a 28x28 image of a handwritten label[X]
 ```
