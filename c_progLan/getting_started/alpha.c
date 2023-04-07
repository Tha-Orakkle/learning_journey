#include <stdio.h>

int main(void)
{
	int i;
	
	for (i = 0; i <= 10; i++)
	{
		char ch;

		for (ch = 'a'; ch <= 'z'; ch++)
		{
			putchar(ch);
		}
		putchar('\n');
	}

	int j;

	j = 0;

	while (j <= 10)
	{
		char cr;
		
		cr = 'z';

		while (cr >= 'a')
		{
			putchar(cr);
			cr--;
		}
		putchar('\n');
		j++;
	}


}
