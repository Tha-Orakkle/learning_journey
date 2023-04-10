#!/usr/bin/env bash

num1=20.5
num2=5

# method 1
# does not support floating point
echo $(( num1 + num2 ))
echo $(( num1 - num2 ))
echo $(( num1 * num2 ))
echo $(( num1 / num2 ))
echo $(( num1 % num2 ))

# method 2
# does not support floating point
echo $(expr $num1 + $num2 )
echo $(expr $num1 - $num2 )
echo $(expr $num1 \* $num2 ) # '*' needs to be escaped in this method
echo $(expr $num1 / $num2 )
echo $(expr $num1 % $num2 )

# working with floating points
# using Basic Calculator(BC)
echo "$num1+$num2" | bc
echo "20.5-5" | bc
echo "20.5*5" | bc
echo "scale=2;20.5/5" | bc # 'scale' will be required to determine how many decimal
echo "20.555" | bc

num3=81
echo "scale=2;sqrt($num3)" | bc -l # '-l' math library for the sqrt function
echo "scale=2;3^3" | bc -l # power
