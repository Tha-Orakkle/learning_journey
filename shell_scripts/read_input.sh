#!/usr/bin/env bash

# reads multiple input
echo "Enter names: "
read name1 name2 name3
echo "Entered names: $name1, $name2, $name3"

# reads from input on the same line
read -p "username: " user_var # -p flag reads on the same line
echo "username: $user_var"

# reads input silently
read -sp "password: " pass_var # -s flag reads silently
echo
echo "password: $pass_var"

# save multiple input in an array
echo "Enter names: "
read -a names # -a flag reads into an array
echo "Names : ${names[0]}, ${names[1]}, ${names[2]}"

# $REPLY: default var where var name is not provided for read
echo "Enter name: "
read
echo "Name: $REPLY" # default variable
