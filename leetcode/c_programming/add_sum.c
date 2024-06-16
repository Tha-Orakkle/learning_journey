/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* twoSum(int* nums, int numsSize, int target, int* returnSize) {
    int i, j;
    int *result = (int *)malloc(2 * sizeof(int));
    
    
    for (i = 0; i < numsSize; i++) {
        j = i + 1;
        while (j < numsSize) {
            if ((nums[i] + nums[j]) == target) {
                result[0] = i;
                result[1] = j;
                *returnSize = 2;
                break;
            }
            j++;
        }
    }
    return result;
}
