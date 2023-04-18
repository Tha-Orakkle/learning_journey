#!/usr/bin/env bash

#using array
# bash supports single dimensional array 

os=('ubuntu' 'windows' 'kali')
os[3]='mac' # adding an element to an array

unset os[2] # removes the element of an array
echo "${os[@]}" # prints all the element of the array
echo "${os[1]}"
echo "${!os[@]}" # prints the indices of the array 
echo "${#os[@]}" # prints the length of the array

# NOTE elements of an array can be set at any index. thereofr there
# can be gaps btween indices of an array.

string=thisisastring
echo "${string[@]}"
# a variable can be printed like an array and the value of the variable will be saved at index of the array variable
