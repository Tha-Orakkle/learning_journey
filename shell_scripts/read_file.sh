#!/usr/bin/env bash

while read p # reads into variable p line by line
do 
	echo $p
	sleep 2
done < file.txt # redirection: reads from file.txt

# OR 
# can be done with pipe
echo "======================================"

cat file.txt | while read p
do 
	echo $p
	sleep 1
done


# using Internal Field Separator(IFS)
# when it is difficult to read a line due to special characters

echo "================================"

while IFS=' ' read -r line # assigning a blankspace to ifs
do
	echo $line
	sleep 1
done < file.txt
