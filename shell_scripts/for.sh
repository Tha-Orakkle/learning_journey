#!/usr/bin/env bash

# for loop

for i in {2..10..2} # start..end..increment by
do
	echo $i
done

#OR
echo "===================================="

for (( i=0; i<=5; i++))
do
	echo $i
done

# Using for loop to execute commands
echo "===================================="

for command in ls pwd date
do
	echo "-----------------$command--------------"
	$command
done

# printing all directories in a folder

for item in *
do
	if [ -f $item ]
	then
		echo $item
	fi
done
