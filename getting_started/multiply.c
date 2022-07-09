#include <stdio.h>

int main(void)
{
	int i, j, k;

	for (i = 1; i <= 12; i++)
	{
		for (j = 1; j <= 12; j++)			{
			k = j * i;
			printf("%d ", k);
		}
		printf("\n");
	}
	return (0);
}

