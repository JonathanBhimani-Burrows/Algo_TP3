import math


def merge(arr):
    if len(arr) > 1:
        n = math.ceil(len(arr)/3)
        L = arr[:n]
        M = arr[n:2*n]
        R = arr[2*n:]
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
            else:
                arr[l] = R[k]
                k += 1

            l += 1
        # now compare and sort for the remaining 2, if they exist
        if i == L_len:
            arr, M, R, j, k, l = sort2(arr, M, R, j, k, l)
        elif j == M_len:
            arr, L, R, i, k, l = sort2(arr, L, R, i, k, l)
        else:
            arr, L, M, i, j, l = sort2(arr, L, M, i, j, l)
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
    return arr

# 2 element sort function - this is performed the same way a regular merge sort would be done
def sort2(arr, subarr1, subarr2, subarr1_index, subarr2_index, arr_index):
    while subarr1_index < len(subarr1) and subarr2_index < len(subarr2):
        if subarr1[subarr1_index] < subarr2[subarr2_index]:
            arr[arr_index] = subarr1[subarr1_index]
            subarr1_index += 1
        else:
            arr[arr_index] = subarr2[subarr2_index]
            subarr2_index += 1
        arr_index += 1
    return arr, subarr1, subarr2, subarr1_index, subarr2_index, arr_index


if __name__ == '__main__':
    A1 = [1,2,4,65,11,9,7,8,3,55,5,45,76,99]
    print('The original array is', A1)
    A1_sorted = merge(A1)
    print('The sorted array is',A1_sorted)
