#!/usr/bin/env bash
# passing arguments to bash scripts

echo $0 $1 $2 $3 '> echo $0 $1 $2 $3'

# saving the arguments a an array
args=("$@")
echo ${args[0]} ${args[1]} ${args[2]} ${args[3]}

# a default var that saves all args
echo $@

#a default var that saves the number of args passed
echo $#
