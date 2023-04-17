#include <stdlib.h>
#include <stdio.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* twoSum(int* nums, int numsSize, int target)
{
	int i, j;
	int *returned_arr = malloc(sizeof(int) * 2);

	for (i = 0; i < numsSize; i++)
	{
		for (j = 0; j < numsSize; j++)
		{
			if (i == j)
				continue;
			if (nums[i] + nums[j] == target)
				break;
		}
		if(nums[i] + nums[j] == target)
			break;
	}

	*returned_arr = i;
	*(returned_arr + 1) = j;

	return (returned_arr);
}

int main(void)
{
	int arr[5] = {2, 5, 11, 6, 9};
	int target = 16, size = sizeof(arr) / sizeof(arr[0]);
	int *ret;

	ret = twoSum(arr, size, target);
	printf("[%d, %d]", ret[0], ret[1]);

	return (0);
}
