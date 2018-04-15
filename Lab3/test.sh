#!/bin/bash


fun(){
	local a=$(($1+1))
	echo $a
	return $a
}


var=0
a=1
numbervar=0
read a
echo $a
fun $a
echo $a

case "$a" in
	'0') echo $a
		;;
	*) echo atata
		;;
esac

