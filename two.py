#-*- coding:utf-8 -*-

#####################
#huangxianhui
#2017/12/24
#biology of system 
#####################



import numpy as np
from scipy.integrate import odeint as ot
import matplotlib.pyplot as plt



def con_time(Tcon, T):
		
	
	#对每个反应赋予初始值
	glu = Tcon[0]
	g6p = Tcon[1]
	fru = Tcon[2]
	f6p = Tcon[3]
	atp = Tcon[4]
	adp = Tcon[5] 
	
	k = [1, 0.25, 1, 1, 1, 1, 1, 2.5]
	#v与k间的参数关系
	v1 = k[1]
	v2 = k[2] * glu * atp
	v3 = k[3] * g6p - k[0] * fru
	v4 = k[4] * fru * atp
	v5 = k[5] * f6p
	v6 = k[6] * f6p
	v7 = k[7] * adp
	
	#各物质浓度与反应路径间的关系
	rh = [0,0,0,0,0,0]

	rh[0] = d_gul_dt = v1 - v2
	rh[1] = d_g6p_dt = v2 - v3
	rh[2] = d_fru_dt = v3 - v4 + v5
	rh[3] = d_f6p_dt = v4 - v5 - v6
	rh[4] = d_atp_dt = -v2 - v4 + v7
	rh[5] = d_adp_dt = v2 + v4 - v7 
	print rh[5]	
	return 	rh

def plo_draw(res,t):
	# 定义六种物质颜色
	col = ['pink','red','blue','black','gold','green']
	# 绘制六种物质浓度变化关系图 ，保存为plt1.jpg
	for i in range(6):
		plt.plot(t, res[:,i], color = col[i])
	
	plt.xlabel('Time')
	plt.ylabel('Concentration')
	plt.savefig('plt1.jpg')
	plt.close()
		
	## 绘制Glucose 与 Fruc1.6P2间的浓度关系，保存为plt2.jpg
	
	plt.plot(res[:,0], res[:,3], color = 'yellow')
	plt.xlabel("Glucose__Concentration")
	plt.ylabel("Fruc1,6P2__Concemtration")
	plt.savefig("plt2.jpg")
	plt.close
	
	return 0
				

#给定时间Time 为1min， 以0.01s为时间步长

Time = np.arange(0, 60,0.01)
Tcon = [0,0,0,0,0.5,0.5]
res = ot(con_time,Tcon,Time)

plo_draw(res, Time)	
