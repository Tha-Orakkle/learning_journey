#!/usr/bin/env bash

name="Evil Orakkle"

#saving the output of ac ommand to a variable
user=$(whoami)
date=$(date)
whereami=$(pwd)

echo "Good Morning $name"
sleep 1
echo "You're looking good today $name"
sleep 1
echo "You have the best Beard I've ever seen $name"
sleep 2
echo "You are currently logged in as $user and you are in the directory $whereami. Also today is: $date"
