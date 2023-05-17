#!/usr/bin/env bash

# until loop
# while in the while loop commands are only executed when they are true
# in the until loop, commands are executed when they are false

n=1

until [ $n -gt 10 ]
do
	echo $n
	(( n++ ))
done 
