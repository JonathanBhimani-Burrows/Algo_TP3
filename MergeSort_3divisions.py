import math
def merge(arr):
    if len(arr) > 1:
        n = math.ceil(len(arr)/3)
        L = arr[:n]
        M = arr[n:2*n]
        R = arr[2*n:]
        print('right after assignment')
        print('n is ', n)
        print('L is ', L)
        print('M is ', M)
        print('R is ', R)
        M_len = len(M)
        R_len = len(R)
        L_len = len(L)

        merge(L)
        merge(M)
        merge(R)
        i, j, k, l = 0,0,0,0
        # first, we need to compare values and sort for all 3
        while i < L_len and j < M_len and k < R_len:
            if L[i] < M[j] and L[i] < R[k]:
                arr[l] = L[i]
                i += 1
            elif M[j] < L[i] and M[j] < R[k]:
                arr[l] = M[j]
                j += 1
            # elif R[k] < L[i] and R[k] < M[j]:
            else:
                arr[l] = R[k]
                k += 1
            print('arr here is',arr)
            print('L is',L)
            print('M is',M)
            print('R is',R)
            # else:
            #     print('Something is wrong - 1')

            l += 1
        # issue is that the final re-copying is being done on the origina arrays and not the new ones
        # now compare and sort for the remaining 2, if they exist
        if i == L_len:
            arr, M, R, j, k, l = sort2(arr, M, R, j, k, l)
        elif j == M_len:
            arr, L, R, i, k, l = sort2(arr, L, R, i, k, l)
        # elif k == R_len:
        else:
            print('L and M are',L,M)
            arr, L, M, i, j, l = sort2(arr, L, M, i, j, l)
        # else:
        #     print('Something is wrong - 2')
        # now clean up the rest
        while i < L_len:
            arr[l] = L[i]
            i+=1
            l+=1
        while j < M_len:
            arr[l] = M[j]
            j+=1
            l+=1
        while k < R_len:
            arr[l] = R[k]
            k+=1
            l+=1
        print('n is',n)
        print('array is - double merge',arr)
    return arr

def sort2(arr, subarr1, subarr2, subarr1_index, subarr2_index, arr_index):
    # print('new arr is before sort2',arr)
    print('subarr1 is',subarr1)
    print('subarr2 is',subarr2)
    while subarr1_index < len(subarr1) and subarr2_index < len(subarr2):
        if subarr1[subarr1_index] < subarr2[subarr2_index]:
            arr[arr_index] = subarr1[subarr1_index]
            subarr1_index += 1
        # elif subarr1[subarr1_index] > subarr2[subarr2_index]:
        else:
            arr[arr_index] = subarr2[subarr2_index]
            subarr2_index += 1
        # else:
        #     print('Something is wrong - 3')
        arr_index += 1
    print('arr is',arr)
    return arr, subarr1, subarr2, subarr1_index, subarr2_index, arr_index

if __name__ == '__main__':
    A1 = [1,2,4,65,11,9,7,8,3,55,5,45,76,99]
    # A1 = [99,88,77,66,55,44,33,22,11]
    # A1 = [99,88,77,66,55,44]
    # A1 = [66,55,44]
    print('The original array is', A1)
    A1_sorted = merge(A1)
    print('The sorted array is',A1_sorted)
