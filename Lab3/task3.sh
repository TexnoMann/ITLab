#!/bin/bash
fiblast=1
fibfirst=1
fib=0
arrfibo=(0 1 1)
echo "$1 первых числа фибоначи:"
echo "======================================================="
(echo "$1 первых числа фибоначи:")>"fibi.data"
for((i=0;i<3 && i<$1;i++)) do
	echo ${arrfibo[i]}
	(printf '%b' 'Число Фибоначи №'  $((i+1)) ': '  ${arrfibo[i]})>>"fibi.data"
	(printf '%b' '\n')>>"fibi.data"
done
for((i=4; i<=$1; i++))
do
	fib=$((fiblast+fibfirst))
	fibfirst=$((fiblast))
	fiblast=$((fib))
	echo "$fiblast"
	(echo "Число Фибоначи №$i: $fiblast")>>"fibi.data"
done


