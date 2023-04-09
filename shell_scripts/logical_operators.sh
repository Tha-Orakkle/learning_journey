#!/usr/bin/env bash

# using logical AND
# '-a' or &&  can be used
# [ condition -a condition ]
# [[ condition && condition ]]

age=25
if [ "$age" -gt 18 ] && [ "$age" -lt 30 ]
then
	echo "valid age"
else
	echo "age not valid"
fi
