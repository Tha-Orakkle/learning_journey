#include <stdio.h>
#include <sys/types.h>
#include <unistd.h>

/**
 * main - creates a child process with fork
 *
 * Return: 0
 */

int main(void)
{
	pid_t mypid1;
	pid_t mypid2;
	pid_t pid;

	mypid1 = getpid();
	printf("Before fork, PID is %u\n", mypid1);

	pid = fork();
	if (pid == -1)
	{
		perror("Error: ");
		return (1);
	}
	mypid2 = getpid();
	printf("After fork, PID is %u\n", mypid2);
	mypid2 = getppid();
	printf("Parent PID is %u\n", mypid2);

	return (0);
}
