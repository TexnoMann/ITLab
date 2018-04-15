
#!/bin/bash

fun(){
	N=$1
	fact=1
	for((i=2;i<=$N; i++)) do
		let "fact*=i"
	done
	echo "Факториал от $N = $fact"
	(echo "Факториал от $N = $fact")>"factor.data"

}

echo "Введите натуральное число N для вычисления факториала:"
read N
if [[  $N == *.* ]]
	then
	echo "Необходимо натуральное число! Выход" 
	exit 0
elif [[ $N == -* ]]
	then
	echo "Необходимо только неотрицательное число! Выход"
elif (( $N >= '0' )); then
	fun $N
else
	echo "Недопустимые символы, необходимо число! Выход"
	exit 0
fi
