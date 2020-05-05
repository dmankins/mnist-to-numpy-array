'''
Read the MNIST data into numpy arrays

Data format described here: http://yann.lecun.com/exdb/mnist/

This works on an Intel processor, might not work on a big-endian
machine (this probably depends on how well struct.unpack('>ii', ...)
does its thing on those machines.
'''

import matplotlib.pyplot as plt
import numpy as np
import struct
import sys

debug = False

def main(args):
    '''
    Read files.  Figure out whether they're labels or images by magic
    number.

    Write out the results as numpy arrays with the same name as the
    file read in with a .npy extension.
    '''
    for fname in args:
        print(f'processing {fname}')
        with open(fname, 'rb') as fp:
            magic, count = struct.unpack('>ii', fp.read(8))
            if magic == 0x801:
                print(f'...label file; {count} entries')
                labels = np.zeros(count).astype(np.ubyte)
                lread_size = 8
                if count % lread_size != 0:
                    print(f'...{count} not divisible by {lread_size},'
                          ' so reading byte at a time')
                    lread_size = 1
                for idx in range(0, count, lread_size):
                    ls = struct.unpack(f'>{"B"*lread_size}', fp.read(lread_size))
                    labels[idx:idx+lread_size] = ls
                np.save(f'{fname}.npy', labels)
            elif magic == 0x803:
                print(f'....image file; {count} entries')
                rows, cols = struct.unpack('>ii', fp.read(8))
                print(f'....{rows} rows x {cols} cols')
                images = np.zeros(count * rows * cols).reshape(count, rows, cols).astype(np.ubyte)
                for idx in range(count):
                    for row in range(rows):
                        images[idx, row] = np.array(
                            struct.unpack(f'>{"B"*cols}',
                                          fp.read(cols)
                            )
                        )
                    if debug:
                        plt.imshow(images[idx])
                        plt.show()

                np.save(f'{fname}.npy', images)
            else:
                print(f'{fname}: magic number {magic} not recognized')
        
if __name__ == '__main__':
    main(sys.argv[1:])

    
