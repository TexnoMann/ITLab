from numpy import*

class StateSpaceModelNP():

    def getMatrixControlNP(self):
    		matControl=array(self.matB.copy())
    		for i in range((ndarray.shape(self.matA)[0])-1):
    			matControl=np.append(matControl, linalg.matrix_power(self.matA, i+1)*self.matB, axis=1)
    		return matControl

    def checkControlNP(self):
		if matrix_rank(self.getMatrixControlNP()) == ndarray.shape(self.getMatrixControlNP())[0]: return True
		else: return False

	def getMatrixObservabilityNP(self):
		matObservability=array(self.matC.copy())
		for i in range((ndarray.shape(self.matA)[0])-1):
			matObservability=np.append(matControl, (self.matB)*(linalg.matrix_power(self.matA, i+1)), axis=0)
		return matObservability

	def checkObservabilityNP(self):
		if matrix_rank(self.getMatrixObservabilityNP()) == ndarray.shape(self.getMatrixObservabilityNP())[0]: return True
		else: return False
