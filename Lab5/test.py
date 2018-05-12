from SAU.StateSpaceModel import *
from random import *

def generateMatrixA(filename):
	file=open(filename)
	matrixA=[]
	obj=[]
	line= file.readline()
	lists=list(map(int,line.split()))
	for n in range(3):
		for i in range(2):
			obj.append(lists[(i*2+4*n+0):(i*2+4*n+2)])
		matrixA.append(Matrix(obj.copy()))
		obj.clear()

	print(matrixA[0])
	return matrixA

def generateMatrixB(filename):
	file=open(filename)
	matrixB=[]
	obj=[]
	line= file.readline()
	lists=list(map(int,line.split()))
	for n in range(3):
		for i in range(1):
			obj.append(lists[(i*2+2*n+0):(i*2+2*n+2)])

		matrixB.append(Matrix(obj.copy()).transpose())

		obj.clear()

	print(matrixB[0])
	return matrixB

def generateMatrixC(filename):
	file=open(filename)
	matrixC=[]
	obj=[]
	line= file.readline()
	lists=list(map(int,line.split()))
	for n in range(3):
		for i in range(1):
			obj.append(lists[(i*2+2*n+0):(i*2+2*n+2)])

		matrixC.append(Matrix(obj.copy()))

		obj.clear()

	print(matrixC[0])
	return matrixC


fileA=open("files/A" , 'w' )
fileB=open("files/B" , 'w' )
fileC=open("files/C" , 'w' )

for i in range(100):
	fileA.write(str(randint(-1, 100))+ ' ')
	fileB.write(str(randint(-1, 100))+ ' ')
	fileC.write(str(randint(-1, 100))+ ' ')

fileA.close()
fileB.close()
fileC.close()

listMatA=generateMatrixA('files/A')
listMatB=generateMatrixB('files/B')
listMatC=generateMatrixC('files/C')

result=open('files/result', 'w')

ssm = StateSpaceModel(listMatA[0],listMatB[0], listMatC[0])
mat1=ssm.matA
mat2=ssm.matC
mat3=ssm.matB



result.write('Дано:' + '\n')
result.write('Матрица системы A1=[')

mat=mat1.getMatrixInList().copy()
for n in range(2):
	result.write(str(mat[n]))
result.write(']')
result.write('\n')

result.write('Матрица управления B1=[')

mat=mat3.getMatrixInList().copy()
for n in range(2):
	result.write(str(mat[n]))
result.write(']')
result.write('\n')

result.write('Матрица выхода С1=[')

mat=mat2.getMatrixInList().copy()
for n in range(1):
	result.write(str(mat[n]))
result.write(']')
result.write('\n')

result.write('Проверка системы на управляемость' + '\n')


if ssm.checkControl() :
	result.write('Система управляема' + '\n') 
else:
	result.write('Система неуправляема' + '\n') 

result.write('Проверка системы на наблюдаемость' + '\n')	

if ssm.checkObservability() :
	result.write('Система наблюдаема' + '\n') 
else:
	result.write('Система частично ненаблюдаема' + '\n') 

result.close()