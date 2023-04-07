#include <stdio.h>

/**
 * main - reverses the elements of the array
 *
 * Return: 0
 */
int main(void)
{
	int i;
	int a[] = {32, 56, 54, 32, 67, 89, 90, 32, 21};

	for (i = 0; i < 9; ++i)
	{
		printf("%d ", a[i]);
	}
	printf("\nReversed:\n");
	for (i = 8; i >= 0; --i)
	{
		printf("%d ", a[i]);
	}
	printf("\n");
	return (0);
}
