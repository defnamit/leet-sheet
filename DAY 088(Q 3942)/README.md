# **3942. Minimum Operations to Sort a Permutation**


You are given an integer array nums of length n, where nums is a permutation of the integers from 0 to n - 1.

You may perform only the following operations:

Reverse the entire array.
Rotate Left by One: Move the first element to the end of the array, and rest elements to left by one position.
Return an integer denoting the minimum number of operations required to sort the array in increasing order. If it is not possible to sort the array using only the given operations, return -1.


# MY EXPLANATION-

1. `nums = [0,1,2,3,4,10,6,7,8,9,5]`, so `n = 11`.
2. We only consider `k` values that divide `n` exactly.
3. Since 11 is prime, the only possible values are `k = 1` and `k = 11`.
4. For `k = 1`, every element forms a separate block, so the array cannot be sorted.
5. Therefore, `k = 1` is invalid.
6. For `k = 11`, the entire array is one block.
7. A block can be sorted by cyclic rotation only if it has at most one descending circular transition.
8. Here, `10 > 6`, `9 > 5`, and the wraparound `5 > 0` give three descending transitions.
9. Therefore, `k = 11` is also invalid.
10. No valid `k` exists, so the sum is `0`.