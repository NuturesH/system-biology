#-*-coding:UTF-8-*-

###############
#Huangxianhui
#2017/12/13
###############

import numpy as np
from numpy.linalg import svd


#定义计算零空间的类
class space():
	#初始化
	def __init__(self):
		self.reac_matrix = np.array([1,-1,0,0,0,0,0,0,1,-1,0,0,0,0,0,0,1,-1,1,0,0,0,0,0,1,-1,-1,0,0,-1,0,-1,0,0,1,0,1,0,1,0,0,-1]).reshape((6,7))
		self.atol = 1e-13
		self.rtol = 0
		print "\n","反应矩阵如下："
		print self.reac_matrix, "\n"
		#return 0
	#定义计算零空间函数	
	def nullspace(self):
		reac_matrix = self.reac_matrix
		atol = self.atol
		rtol = self.rtol
		A = np.atleast_2d(reac_matrix)
		u,s,vh = svd(A)
		tol = max(atol,rtol * s[0])
		nnz = (s >= tol).sum()
		ns = vh[nnz:].conj().T
		print "反应矩阵的右零空间如下："
		print ns
		return 0

#调用类
reaction = space()
#调用类函数
reaction.nullspace()

