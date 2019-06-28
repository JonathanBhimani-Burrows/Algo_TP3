import numpy as np
import math
import sys

def Search(arr, n, odd, alpha, flag):
    if flag == False:
        if odd:
            if arr[n - 1] - alpha < n - 1:
                print('No index found')
                return 0
            elif arr[n - 1] - alpha == n - 1:
                print('Answer is index ', n - 1 + alpha)
                flag = True
            elif arr[n - 1] - alpha > n - 1:
                n = math.floor(n / 2)
                odd = False
                Search(arr, n, odd, alpha, flag)
            else:
                print('Something is wrong')

        if flag == False:
            if arr[n] - alpha < n:
                print('searching upper')
                odd = True
                alpha = len(arr[n:])
                Search(arr[n:], n, odd, alpha, flag)  # search upper
            elif arr[n] - alpha == n:
                print('Answer is index ', n + alpha)
                flag = True
            elif arr[n] - alpha > n:
                print('searching lower')
                odd = True
                Search(arr[:n], n, odd, alpha, flag)  # search lower
            else:
                print('Something is wrong')

if __name__ == '__main__':
    # A1 = [-2,-1,1,2,4,6]

    # A1 = [0,3,4,5,7,9]
    # A1 = [-2,-1,0,1,4,6,11,13,14,15,17,19]
    A1 = [-2, 1, 3, 4, 5, 6,7, 13, 14, 15, 17, 19]
    A1_np = np.asarray(A1)
    Search(A1_np, A1_np.shape[0], odd=True, alpha=0, flag=False)