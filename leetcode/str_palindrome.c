#include <stdio.h>
#include <stdbool.h>


#define MAX_SIZE 100000

bool isPalindrome(char *s)
{
	char new_str[MAX_SIZE];
	char reversed_str[MAX_SIZE];
	int i, count = 0, j = 0;

	if (!s)
		return (false);

	for (i = 0; s[i] != '\0'; i++)
	{
		if (s[i] >= 'A' && s[i] <= 'Z')
		{
			new_str[j++] = s[i] +  32;
			count++;
		}

		if ((s[i] >= 'a' && s[i] <= 'z') || (s[i] >= '0' && s[i] <= '9'))
		{
			new_str[j++] = s[i];
			count++;
		}
	}
	new_str[j] = '\0';

	/* reverse the new string */
	count  -= 1;
	i = 0;

	while (count >= 0)
	{
		reversed_str[i] = new_str[count];
		count--;
		i++;
	}
	reversed_str[i] = '\0';

	/* compare reversed and new string */

	for (i = 0; new_str[i] != '\0' && reversed_str[i] != '\0'; i++)
	{
		if (new_str[i] != reversed_str[i])
			return (false);
	}

	return (true);
}


int main(void)
{
	char *str = "0P";
	bool ret;

	ret = isPalindrome(str);
	if (ret)
		printf("%s is a palindrome\n", str);
	else
		printf("%s is not a palindrome\n", str);

	return (0);
}
