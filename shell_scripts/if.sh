#!/usr/bin/env bash

count=10

if [ $count -gt 15 ]
then
	echo "$count is > 15"
elif [ $count -lt 15 ]
then
	echo "$count is < 15"
else
	echo "Condition is False"
fi
