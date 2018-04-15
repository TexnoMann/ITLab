from MatPy.Matrix import *


class StateSpaceModel():

	def __init__(self, filename):
		self.__file=open(filename)
		self.__parseFile()
		self.matA
		self.matB
		self.matC

	def getMatrixControl(self):
		matControl=self.matB
		for i in range(self.matA.getRowCount()-1):
			matControl.addColumn(pow(self.matA,i+1)*self.matB)
		return matControl

	def getMatrixObservability(self):
		matObservability=self.matC
		for i in range(self.matA.getRowCount()-1):
			matObservability.addRow(self.matC*(pow(self.matA,i+1)))
		return matObservability

	def __parseFile(self):
		self.matA=self.__getMatrixinFile()
		self.matB=self.__getMatrixinFile()
		self.matC=self.__getMatrixinFile()

	def __getMatrixinFile(self):
		n=0
		matList=[]
		while True:
			line= self.__file.readline()
			if (line is "\n") or (line is ''):
				break
			else :
				lists=list(map(int,line.split()))
				assert(n == 0 or len(lists) == n), "Error count elements in row"
				n=len(lists)
				matList.append(lists)
		return Matrix(matList)






