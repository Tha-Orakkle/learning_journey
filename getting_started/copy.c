#include <stdio.h>

/**
 * main - reads the input text stream and
 * sends it to the output character by character
 */
main()
{
	int c;

	c = getchar();
	while (c != EOF)
	{
		putchar(c);
		c = getchar();
	}
}
