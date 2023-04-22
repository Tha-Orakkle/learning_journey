#!/usr/bin/env bash

#functions can be declared using the fuction keyword or not
# arguments can be passed to a function and the same logic that applies to read arguments from command applies

function print()(
	echo $1
)

# OR

#print()(
#	echo "This is another way to declare a funcion"
#)

print World

echo "foo"

# variables in shell scipts are global vars. To make a var local
#+ we need to prefix the keyword `local` at the declaration of the var

function fprint()(
	local name=$1
	echo "value of name is $name"
)


name="Max"
fprint Tom
echo "value of name is $name"

