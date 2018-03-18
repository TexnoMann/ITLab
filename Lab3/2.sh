#!/bin/bash

while (true)
do

echo "Enter your name:"
read name
if [ "$name" == "" ]
then
	echo "Bye :c">>"age.txt"
	exit 0
else
echo "The name you entered is $name. Hi $name!" >> "age.txt"
fi

echo "Do you want continue this program? (Yes/No)"
read answer
if [ -z $answer ]
then
	echo "Bye :c">>"age.txt"
	exit 0
else
case "$answer" in
   Y|y|yes|Yes) echo "You're amazing c:" >>"age.txt"
        ;;
    N|n|no|No) echo "Bye :c">>"age.txt"
        exit 0
        ;;
esac
fi

echo "Enter your age:"
read age
echo "$age">>"age.txt"
if ((0<"$age"))
then
	if (("$age"<=16)) 
	then
		group=child

	elif ((17<="$age" && "$age"<=25))
	then
		group=youth

	else
		group=adult
	fi
	echo "$name, your group is $group.">>"age.txt"
else
	echo "Bye :c">>"age.txt"
	exit 0
fi

done
