from numpy import*
import numpy as np
from MatPy import*

class StateSpaceModelNP():

    def __init__(self, filename):
        self.__file=open(filename)
        self.__parseFile()

    def __init__(self, matA, matB, matC):
        self.matA=matA
        self.matB=matB
        self.matC=matC

    def getMatrixControlNP(self):
        matControl=array(self.matB.copy())
        for i in range(shape(self.matA)[0]-1):
            matControl=np.append(matControl, np.dot(linalg.matrix_power(self.matA, i+1), self.matB), axis=1)
        return matControl

    def checkControlNP(self):
        if (matrix_rank(self.getMatrixControlNP()) == shape(self.getMatrixControlNP())[0]):
            return True
        else:
            return False


    def getMatrixObservabilityNP(self):
        matObservability=array(self.matC.copy())
        for i in range((shape(self.matA)[0])-1):
            matObservability=np.append(matObservability,np.dot(self.matC,(linalg.matrix_power(self.matA, i+1))), axis=0)
        return matObservability

    def checkObservabilityNP(self):
        if matrix_rank(self.getMatrixObservabilityNP()) == shape(self.getMatrixObservabilityNP())[0]: return True
        else: return False

    def generateMatrixNP(filename,M,a,b):
        file=open(filename)
        matrix=[]
        line= file.readline()
        lists=list(map(int,line.split()))
        for n in range(M):
            if a>=b:str=b;
            else: str=a;
            for j in range(str):
                matrix.append(lists[(j*2+a*b*n) : (j*2 + a*b*n +2)])
        return matrix
