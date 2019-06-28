import numpy as np
import math

def Search(arr, n, odd, alpha):
    if odd:
        print('n is',n)
        if arr[n-1]-alpha < n-1:
            print('No index found')
            return 0
        elif arr[n-1]-alpha == n-1:
            print('Answer is index ', n-1+alpha)
            return 0
        elif arr[n-1]-alpha > n-1:
            n = math.floor(n/2)
            odd = False
            print('n is now ',n)
            Search(arr, n, odd, alpha)
        else:
            print('Something is wrong')
    print('The array is',arr)
    print('n is',n)
    if arr[n]-alpha < n:
        print('searching upper')
        odd = True
        print('The array will be ',arr[n:])
        alpha = len(arr[n:])
        Search(arr[n:], n, odd, alpha) #search upper
    elif arr[n]-alpha == n:
        print('Answer is index ', n+alpha)
    elif arr[n]-alpha > n:
        print('searching lower')
        odd = True
        print('The array will be', arr[:n])
        Search(arr[:n], n, odd, alpha) #search lower
    else:
        print('Something is wrong')

if __name__ == '__main__':
    # A1 = [-2,-1,1,2,4,6]

    # A1 = [0,3,4,5,7,9]
    A1 = [-2,-1,0,1,4,6,11,13,14,15,17,19]
    A1_np = np.asarray(A1)
    Search(A1_np, A1_np.shape[0], odd=True, alpha=0)