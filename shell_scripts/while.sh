#!/usr/bin/env bash

# using while loops
# (( n++ )) post/pre-increment can also be used

n=1

while [ $n -le 10 ]
do
	echo -e "$n\c"
	n=$(( n + 1 ))
	sleep 1 # using sleep (in secs)
done


# open a new terminal using bash script

i=1

while [ $i -le 3 ]
do 
	echo "$i"
	(( i++ ))
	bash & #opens new terminal
done
