import numpy as np
import math
def merge(arr, newarr):
    if arr.shape[0] > 1:
        n = math.ceil(arr.shape[0]/3)
        L = arr[:n]
        M = arr[n:2*n]
        R = arr[2*n:]

        print('n is ', n)
        print('L is ', L)
        print('M is ', M)
        print('R is ', R)
        M_len = M.shape[0]
        R_len = R.shape[0]
        L_len = L.shape[0]
        
        merge(L, newarr)
        merge(M, newarr)
        merge(R, newarr)
        if n ==1:
            L = newarr[:n]
            M = newarr[n:2*n]
            R = newarr[2*n:]
        i, j, k, l = 0,0,0,0

        # first, we need to compare values and sort for all 3
        while i < L_len and j < M_len and k < R_len:
            if L[i] < M[j] and L[i] < R[k]:
                newarr[l] = L[i]
                i += 1
            elif M[j] < L[i] and M[j] < R[k]:
                newarr[l] = M[j]
                j += 1
            elif R[k] < L[i] and R[k] < M[j]:
                print('R is',R)
                newarr[l] = R[k]
                k += 1
            else:
                print('Something is wrong - 1')

            l += 1
        # issue is that the final re-copying is being done on the origina arrays and not the new ones
        # now compare and sort for the remaining 2, if they exist
        if i == L_len:
            newarr, M, R, j, k, l = sort2(newarr, M, R, j, k, l)
        elif j == M_len:
            newarr, L, R, i, k, l = sort2(newarr, L, R, i, k, l)
        elif k == R_len:
            newarr, L, M, i, j, l = sort2(newarr, L, M, i, j, l)
        else:
            print('Something is wrong - 2')
        # now clean up the rest
        while i < L_len:
            newarr[l] = L[i]
            i+=1
            l+=1
        while j < M_len:
            newarr[l] = M[j]
            j+=1
            l+=1
        while k < R_len:
            newarr[l] = R[k]
            k+=1
            l+=1
        print('n is',n)
        print('new array is - double merge',newarr)
    return newarr

def sort2(newarr, subarr1, subarr2, subarr1_index, subarr2_index, arr_index):
    # print('new arr is before sort2',newarr)
    # print('subarr1 is',subarr1)
    # print('subarr2 is',subarr2)
    while subarr1_index < subarr1.shape[0] and subarr2_index < subarr2.shape[0]:
        if subarr1[subarr1_index] < subarr2[subarr2_index]:
            newarr[arr_index] = subarr1[subarr1_index]
            subarr1_index += 1
        elif subarr1[subarr1_index] > subarr2[subarr2_index]:
            newarr[arr_index] = subarr2[subarr2_index]
            subarr2_index += 1
        else:
            print('Something is wrong - 3')
        arr_index += 1
    # print('new arr is',newarr)
    return newarr, subarr1, subarr2, subarr1_index, subarr2_index, arr_index

if __name__ == '__main__':
    # A1 = [1,2,4,65,11,9,7,8,3,55,5,45,76,99]
    A1 = [99,88,77,66,55,44,33,22,11]
    # A1 = [99,88,77,66,55,44]
    # A1 = [66,55,44]
    A1_np = np.asarray(A1)
    print('The original array is', A1_np)
    A1_sorted = merge(A1_np, np.zeros(A1_np.shape[0]))
    print('The sorted array is',A1_sorted)
