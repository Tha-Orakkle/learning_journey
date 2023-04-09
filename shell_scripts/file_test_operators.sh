#!/usr/bin/env bash

# '\c' keeps the cursor on the same line in an echo string
#	used along with the -e flag

echo -e "Enter the name of the file : \c"
read file_name

# character special file - a normal file containing texts/characters
# block special file - a binary file that contains pictures, video etc

# '-e' checking if the file exist
# '-f' checks if it is a file
# '-d' checks if it is a directory
# '-b' checks if it is a block special file
# '-c' checks if it is a character special file
# '-s' checks if it is empty or not
# '-r' checks if it is read permission
# '-w' checks if it is write permission
# '-x' checks if it is execution permission


if [ -e $file_name ] 
then
	echo "$file_name found"
else
	echo "$file_name not found"
fi
