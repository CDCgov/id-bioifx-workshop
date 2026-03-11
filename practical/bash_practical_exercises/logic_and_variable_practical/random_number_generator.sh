#!/bin/bash
#Source code: https://www.w3resource.com/bash-script-exercises/conditional-statements.php

# Prompt the user to enter a number
echo "Input a number:"
read n

# Check if the number is greater than 100 (hint: look between the brackets)
if [ "$n" -gt 100 ]; then
    echo "The number is greater than 100."
else
    echo "The number is not greater than 100."
fi


#Exercise 1: change the ordinal statement to execute as true if the number is greater than 50 
#and less than 100

#Exercise 2: change the ordinal statement to execute as true if the number is less than 25 or greater
#than 75

#Exercise 3: change the ordinal statement to execute as true if the number is greater than 1 and
#less than 10, or greater than or equal to 90 and less than 100
