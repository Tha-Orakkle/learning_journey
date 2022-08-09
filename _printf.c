#include <stdio.h>
#include <stdarg.h>

int _vprintf(const char *format, va_list ap);
void number_to_string(int number, int base, char *buf);
void print_string(char *s);
/**
 * int _printf(const char *format, ...);
 * int main(void)
 * {
 * _printf("%d\n", printf("this is a strung"));
 * return (0);
 * }
 */
int _printf(const char *format, ...)
{
	va_list ap;
	int retval, val;

	va_start(ap, format);
	if (format == NULL)
		return (-1);
	val = _vprintf(format, ap);
	va_end(ap);
	retval = val;
	return (retval);
}

int _vprintf(const char *format, va_list ap)
{
	int flag = 0;
	char *str;
	int count = 0;
	char buffer[1024];

	while (*format)
	{
		if (flag == 0)
		{
			if (*format == '%')
				flag = 1;
			else
			{
				putchar(*format);
			}
			count++;
		}
		else
		{
			switch (*format)
			{
				case 'c':
				{
					putchar(va_arg(ap, int));
					count++;
					break;
				}
				case 's':
				{
					str = va_arg(ap, char *);
					print_string(str);
					count++;
					break;
				}
				case '%':
					putchar('%');
					count++;
					break;
				case 'd':
				{
					int n = va_arg(ap, int);

					number_to_string(n, 10, buffer);
					print_string(buffer);
					count++;
					break;
				}

				default:
					break;
			}
			flag = 0;
		}
		format++;
	}
	return (count);
}

void number_to_string(int number, int base, char *buf)
{
	int i = 0, j;
	char tmp[65];

	if (number < 0)
	{
		buf[0] = '-';
		number *= -1;
	}
	if (number == 0)
	{
		*buf = '0';
		*buf = '\0';
		return;
	}
	while (number)
	{
		int rem = number % base;
		if (rem >= 10)
			tmp[i++] = 'a' + (rem - 10);
		else
			tmp[i++] = '0' + rem;

		number /= base;
	}
	for (j = i - 1; j >= 0; j--)
		*buf++ = tmp[j];
	*buf = '\0';
}

void print_string (char *s)
{
	int i = 0;
	while (s[i])
	{
		putchar(s[i]);
		i++;
	}
}
