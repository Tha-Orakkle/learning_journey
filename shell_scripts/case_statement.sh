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
