#include <stdio.h>

main()
{
	float fahr, celsius;
	float lower, upper, step;

	lower = 0;
	upper = 300;
	step = 20;

	celsius = lower;

	printf("The Equivalent of Celsius\n");
	while (celsius <= upper)
	{
		fahr = (((9.0 * celsius) / 5) + 32);
		printf("%3.0f\t%6.1f\n", celsius, fahr);
		celsius = celsius + step;
	}
}
