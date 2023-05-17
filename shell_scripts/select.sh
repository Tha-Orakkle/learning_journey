#!/usr/bin/env bash

# select helps generate easy menus
# prints list out and request that an option is selected

select name in Mark John Tom Ben Greg
do
	echo "$name selected"
	break
done

# select is often used with case

select name in Mark John Tom Ben Greg
do
	case $name in
		"Mark" )
			echo "Mark is selected" ;;
		"John" )
			echo "John is selected" ;;
		"Tom" )
			echo "Tom is selected" ;;
		"Ben" )
			echo "Ben is selected" ;;
		"Greg" )
			echo "Greg is selected" ;;
		* )
			echo "Error: pls provide a number between 1..5" ;;

	esac
done
