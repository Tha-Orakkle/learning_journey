#include <stdio.h>

/**
 * main - checks of a digit appears more than once.
 * prints Yes, if so and No, if otherwise.
 * Return: 0
 */

int main(void)
{
	int i, rem, N;
	int seen[10] = {0};

	printf("Enter a number: ");
	scanf("%d", &N);
	while (N > 0)
	{
		rem = N % 10;
		if (seen[rem] == 1)
		{
			break;
		}
		seen[rem] = 1;
		N /= 10;
	}
	if (N > 0)
	{
		printf("YES");
	}
	else
	{
		printf("NO");
	}
	printf("\n");
}

