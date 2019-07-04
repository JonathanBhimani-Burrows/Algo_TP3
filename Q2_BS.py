import numpy as np
import math
import sys

def Search(arr, n, odd, alpha):
    # first if statement will check if an index exists, then it will check if T(i) = i , then will
    # call itself recursively with n/2
    # odd ensures that, once n = n/2, that the second if is triggered, such that
    # the array will be sliced into upper an lower
    if odd:
        if arr[n - 1] - alpha < n - 1:
            print('No index found')
        elif arr[n - 1] - alpha == n - 1:
            print('Answer is index ', n - 1 + alpha)
            sys.exit()
        elif arr[n - 1] - alpha > n - 1:
            n = math.floor(n / 2)
            odd = False
            Search(arr, n, odd, alpha)
        else:
            print('Something is wrong')
        # this second if is in charge of slicing the array depending on whether the index occurs
        # in the top half of the n/2, or the bottom half
        # In addition, it also checks if, for n/2 = i, T(i) = i
        if arr[n] - alpha < n:
            print('searching upper')
            odd = True
            alpha = len(arr[n:])
            Search(arr[n:], n, odd, alpha)  # search upper
        elif arr[n] - alpha == n:
            print('Answer is index ', n + alpha)
            sys.exit()
        elif arr[n] - alpha > n:
            print('searching lower')
            odd = True
            Search(arr[:n], n, odd, alpha)  # search lower
        else:
            print('Something is wrong')

if __name__ == '__main__':
    A1 = [-3, -2, -1, 0, 1, 2,6, 8, 14, 15, 17, 19]
    A1_np = np.asarray(A1)
    Search(A1_np, A1_np.shape[0], odd=True, alpha=0)

    # as this code uses the principle of divide and conquer, in that
    # the array is subdivided into 2 seconds and then sub divided again until
    # we reach the correct index, if it exists, we know that it will perform
    # the search in O(logn)