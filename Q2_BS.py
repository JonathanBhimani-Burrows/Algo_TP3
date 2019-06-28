import numpy as np
import math

def Search(arr, n, odd):
    if odd:
        print('n is',n)
        if arr[n-1] < n-1:
            print('No index found')
            return 0
        elif arr[n-1] == n-1:
            print('Answer is index ', n-1)
            return 0
        elif arr[n-1] > n-1:
            n = math.floor(n/2)
            odd = False
            print('n is now ',n)
            Search(arr, n, odd)
        else:
            print('Something is wrong')
    print('The array is',arr)
    print('n is',n)
    if arr[n] < n:
        print('searching upper')
        odd = True
        print('The array will be ',arr[n:])
        Search(arr[n:], n, odd) #search upper
    elif arr[n] == n:
        print('Answer is index ', n)
    elif arr[n] > n:
        print('searching lower')
        odd = True
        print('The array will be', arr[:n])
        Search(arr[:n], n, odd) #search lower
    else:
        print('Something is wrong')

# try using a pointer with min and max instead of chopping the array

if __name__ == '__main__':
    # A1 = [-2,-1,1,2,3,5]
    A1 = [-2,-1,1,2,4,8]
    A1_np = np.asarray(A1)
    Search(A1_np, A1_np.shape[0], odd=True)