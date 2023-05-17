#!/usr/bin/env bash

# prevents var from being overwritten

var=31
readonly var
var=50 #this will give an error
echo "var => $var"

# functions can also be made readonly

hello() {
	echo "Hello World"
}

readonly -f hello # -f should be used with functions

hello() {
	echo "Hello World Again" # this will give an error
}

hello

# readonly without any arg displays all built-in readonly variables
readonly
readonly -f # for all readonly functions
