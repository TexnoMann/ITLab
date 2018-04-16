from SAU.StateSpaceModel import *

ssm =StateSpaceModel("testMatrix")
mat1=ssm.matA
mat2=ssm.matC
mat3=ssm.matB
print(mat1.getRang())

