#!/usr/bin/env bash
#using trap command to trap some signals

trap "echo this tests the trap command; exit" 0 2

echo "pid is $$"

while (( COUNT < 10 ))
do
	sleep 10
	(( COUNT ++ ))
	echo $COUNT
done
exit 0
