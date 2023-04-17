#!/usr/bin/env bash

# using case statement - similar to the switch function in C
# used to find a matching pattern

vehicle=$1

case $vehicle in
	"car" )
		echo "Rent of $vehicle is 100 USD" ;;
	"van" )
		echo "Rent of $vehicle is 80 USD" ;;
	"bicycle" )
		echo "Rent of $vehicle is 5 USD" ;;
	"truck" )
		echo "Rent of $vehicle is 150 USD" ;;
	* )
		echo "The vehicle is unknown" ;;
esac


# ============================================

# learning case statement using regex
# where the cap letters are not recognised on your terminal,
# set LANG=C

echo -e "Enter some characters: \c"
read value

case $value in
	[a-z] )
		echo "Use entered $value a to z" ;;
	[A-Z] )
		echo "Use entered $value A to Z" ;;
	[0-9] )
		echo "Use entered $value 0 to 9" ;;
	? )
		echo "Use entered $value special character" ;;
	* )
		echo "Unknown input" ;;
esac
