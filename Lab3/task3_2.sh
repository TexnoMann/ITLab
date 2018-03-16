
#!/bin/bash
N=$1
fact=1
for((i=2;i<=$N; i++))
do
	let "fact*=i"
done
echo "Факториал от $N = $fact"
(echo "Факториал от $N = $fact")>"factor.data"
