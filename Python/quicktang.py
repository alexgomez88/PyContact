#Modulo de Computo con los modelos de contacto rueda-riel
#con los metodos "carter", "kalkerL", "kalkerS", "shen" y
#"polanch". Estos metodos son introducidos dentro de un
#objeto denominado QuickTang que una vez creado interpola
#las constantes de Kalker con la finalidad de acelerar la
#estimacion de su valor.

import numpy as np
import scipy as sp
import scipy.interpolate as spi
import math

def carter(Nload,a,b,mu,ro,G,v_x,v_y,v_z):
	k=4.*0.430/(mu*a)
	#Modelo de Carter, se separa el comportamiento de adhesion del deslizamiento.
	if k*abs(v_x)<2:
		fx=(ro*Nload)*(0.25*k*k*v_x*abs(v_x)-k*abs(v_x))
	else:
		fx=math.copysign((ro*Nload),v_x)
	#El modelo de Carter, no interpreta cargas laterales, por tanto fy es 0.
	return fx,0.

def kalkerL(Nload,a,b,mu,ro,G,v_x,v_y,v_z):
	#Tabla de Constantes de Kalker
	C_11_0_1=np.array([2.47,2.51,2.59,2.68,2.78,2.88,2.98,3.09,3.19,3.29])
	C_11_0_2=np.array([3.40,3.51,3.65,3.82,4.06,4.37,4.84,5.57,6.96,10.7])
	C_11_0=np.hstack((C_11_0_1,C_11_0_2))
	C_11_1_1=np.array([3.29,3.31,3.37,3.44,3.53,3.62,3.72,3.81,3.91,4.01])
	C_11_1_2=np.array([4.12,4.22,4.36,4.54,4.78,5.10,5.57,6.34,7.78,11.7])
	C_11_1=np.hstack((C_11_1_1,C_11_1_2))
	C_11_2_1=np.array([4.93,4.85,4.81,4.80,4.82,4.83,4.91,4.97,5.05,5.12])
	C_11_2_2=np.array([5.20,5.30,5.42,5.58,5.80,6.11,5.57,7.34,8.82,12.9])
	C_11_2=np.hstack((C_11_2_1,C_11_2_2))
	#Matriz final C_11
	C_11_m=np.vstack((C_11_0,C_11_1,C_11_2))

	#Valores de C_22
	C_22_0_1=np.array([2.47,2.51,2.59,2.68,2.78,2.88,2.98,3.09,3.19,3.29])
	C_22_0_2=np.array([3.40,3.51,3.65,3.82,4.06,4.37,4.84,5.57,6.96,10.7])
	C_22_0=np.hstack((C_22_0_1,C_22_0_2))
	C_22_1_1=np.array([2.47,2.52,2.63,2.75,2.88,3.01,3.14,3.28,3.41,3.54])
	C_22_1_2=np.array([3.67,3.81,3.99,4.21,4.50,4.90,5.48,6.40,8.14,12.8])
	C_22_1=np.hstack((C_22_1_1,C_22_1_2))
	C_22_2_1=np.array([2.47,2.53,2.66,2.81,2.98,3.14,3.31,3.48,3.65,3.82])
	C_22_2_2=np.array([3.98,4.16,4.39,4.67,5.04,5.56,6.31,7.51,9.79,16.0])
	C_22_2=np.hstack((C_22_2_1,C_22_2_2))
	#Matriz final C_11
	C_22_m=np.vstack((C_22_0,C_22_1,C_22_2))

	#Valores de C_23
	C_23_0_1=np.array([0.,0.334,0.483,0.607,0.720,0.827,0.930,1.03,1.13,1.23])
	C_23_0_2=np.array([1.33,1.44,1.58,1.76,2.01,2.35,2.88,3.79,5.72,12.2])
	C_23_0=np.hstack((C_23_0_1,C_23_0_2))
	C_23_1_1=np.array([0.,0.473,0.603,0.715,0.823,0.929,1.03,1.14,1.25,1.36])
	C_23_1_2=np.array([1.47,1.59,1.75,1.95,2.23,2.62,3.24,4.32,6.63,14.6])
	C_23_1=np.hstack((C_23_1_1,C_23_1_2))
	C_23_2_1=np.array([0.,0.731,0.809,0.889,0.977,1.07,1.18,1.29,1.40,1.51])
	C_23_2_2=np.array([1.63,1.77,1.94,2.18,2.50,2.96,3.70,5.01,7.89,18.0])
	C_23_2=np.hstack((C_23_2_1,C_23_2_2))
	#Matriz final C_23
	C_23_m=np.vstack((C_23_0,C_23_1,C_23_2))

	#Se crea una fila valores para la relacion entre a/b denominada g (nomeclatura
	#propuesta por Iwinichi)
	g1=np.arange(0.,1.,0.1)
	g2=1./np.arange(1.,0.,-0.1)
	g=np.hstack((g1,g2))
	g,gridmu=np.meshgrid(g,[0.,0.25,0.5])

	#Se crea una funcion para interpolar
	C_11=spi.interp2d(g,gridmu,C_11_m,kind="linear")
	C_22=spi.interp2d(g,gridmu,C_22_m,kind="linear")
	C_23=spi.interp2d(g,gridmu,C_23_m,kind="linear")

	c11=C_11(a/b,mu)
	c22=C_22(a/b,mu)
	c23=C_23(a/b,mu)
	fx=G*a*b*c11*v_x
	fy=G*a*b*c22*v_y-G*a*b*math.sqrt(a*b)*c23*v_z
	ftangmax=ro*Nload
	if abs(fx)>(ftangmax):
		fx=math.copysign(ftangmax,fx)
	if abs(fy)>(ftangmax):
		fy=math.copysign(ftangmax,fx)
	return fx,fy

def kalkerS(Nload,a,b,mu,ro,G,v_x,v_y,v_z):
	#Tabla de Constantes de Kalker
	C_11_0_1=np.array([2.47,2.51,2.59,2.68,2.78,2.88,2.98,3.09,3.19,3.29])
	C_11_0_2=np.array([3.40,3.51,3.65,3.82,4.06,4.37,4.84,5.57,6.96,10.7])
	C_11_0=np.hstack((C_11_0_1,C_11_0_2))
	C_11_1_1=np.array([3.29,3.31,3.37,3.44,3.53,3.62,3.72,3.81,3.91,4.01])
	C_11_1_2=np.array([4.12,4.22,4.36,4.54,4.78,5.10,5.57,6.34,7.78,11.7])
	C_11_1=np.hstack((C_11_1_1,C_11_1_2))
	C_11_2_1=np.array([4.93,4.85,4.81,4.80,4.82,4.83,4.91,4.97,5.05,5.12])
	C_11_2_2=np.array([5.20,5.30,5.42,5.58,5.80,6.11,5.57,7.34,8.82,12.9])
	C_11_2=np.hstack((C_11_2_1,C_11_2_2))
	#Matriz final C_11
	C_11_m=np.vstack((C_11_0,C_11_1,C_11_2))

	#Valores de C_22
	C_22_0_1=np.array([2.47,2.51,2.59,2.68,2.78,2.88,2.98,3.09,3.19,3.29])
	C_22_0_2=np.array([3.40,3.51,3.65,3.82,4.06,4.37,4.84,5.57,6.96,10.7])
	C_22_0=np.hstack((C_22_0_1,C_22_0_2))
	C_22_1_1=np.array([2.47,2.52,2.63,2.75,2.88,3.01,3.14,3.28,3.41,3.54])
	C_22_1_2=np.array([3.67,3.81,3.99,4.21,4.50,4.90,5.48,6.40,8.14,12.8])
	C_22_1=np.hstack((C_22_1_1,C_22_1_2))
	C_22_2_1=np.array([2.47,2.53,2.66,2.81,2.98,3.14,3.31,3.48,3.65,3.82])
	C_22_2_2=np.array([3.98,4.16,4.39,4.67,5.04,5.56,6.31,7.51,9.79,16.0])
	C_22_2=np.hstack((C_22_2_1,C_22_2_2))
	#Matriz final C_11
	C_22_m=np.vstack((C_22_0,C_22_1,C_22_2))

	#Valores de C_23
	C_23_0_1=np.array([0.,0.334,0.483,0.607,0.720,0.827,0.930,1.03,1.13,1.23])
	C_23_0_2=np.array([1.33,1.44,1.58,1.76,2.01,2.35,2.88,3.79,5.72,12.2])
	C_23_0=np.hstack((C_23_0_1,C_23_0_2))
	C_23_1_1=np.array([0.,0.473,0.603,0.715,0.823,0.929,1.03,1.14,1.25,1.36])
	C_23_1_2=np.array([1.47,1.59,1.75,1.95,2.23,2.62,3.24,4.32,6.63,14.6])
	C_23_1=np.hstack((C_23_1_1,C_23_1_2))
	C_23_2_1=np.array([0.,0.731,0.809,0.889,0.977,1.07,1.18,1.29,1.40,1.51])
	C_23_2_2=np.array([1.63,1.77,1.94,2.18,2.50,2.96,3.70,5.01,7.89,18.0])
	C_23_2=np.hstack((C_23_2_1,C_23_2_2))
	#Matriz final C_23
	C_23_m=np.vstack((C_23_0,C_23_1,C_23_2))

	#Se crea una fila valores para la relacion entre a/b denominada g (nomeclatura
	#propuesta por Iwinichi)
	g1=np.arange(0.,1.,0.1)
	g2=1./np.arange(1.,0.,-0.1)
	g=np.hstack((g1,g2))
	g,gridmu=np.meshgrid(g,[0.,0.25,0.5])

	#Se crea una funcion para interpolar
	C_11=spi.interp2d(g,gridmu,C_11_m,kind="linear")
	C_22=spi.interp2d(g,gridmu,C_22_m,kind="linear")
	C_23=spi.interp2d(g,gridmu,C_23_m,kind="linear")

	c11=C_11(a/b,mu)
	c22=C_22(a/b,mu)
	c23=C_23(a/b,mu)

	DY=2*b/100
	X=np.zeros((100,100))
	Y=np.zeros((100,100))
	Pn=np.zeros((100,100))
	Tmax=np.zeros((100,100))
	Tx=np.zeros((100,100))
	Ty=np.zeros((100,100))
	
	#Coeficientes elasticos de Kalker
	L1=8*a/(3*G*c11);
	L2=8*a/(3*G*c22);
	L3=math.pi*(a**2)/(4*G*math.sqrt(a*b)*c23);
		
	#Inicio de las iteraciones verticales
	fx=0
	fy=0
	for j in range(0,100):
		#Determina el valor de la coordenada lateral del punto de estudio
    		Yo=DY*(50-j)
    		#Determina el valor de la coordenada del primer punto de estudio
    		Xo=-a*np.real(math.sqrt(1-(Yo/b)**2))
    		#Determina la longitud del segmento longitudinal de estudio
    		DX=2*a*np.real(math.sqrt(1-(Yo/b)**2))/100
    		#Inicia las iteraciones longitudinales
    		for i in range(0,100):
    			#Llenado de la matriz de coordenadas de Y
                	Y[j,i]=Yo
                	#Llenado de la matriz de coordenadas de X
            		X[j,i]=Xo+DX*(i)
            		#Se determina la presion normal aplicada sobre el punto de estudio
			point=1-(X[j,i]/a)**2-(Y[j,i]/b)**2
			if point>=0:
	        		point=point
	        	else:
	        		point=0
	        	Pn[j,i]=((3*Nload)/(2*math.pi*a*b))*np.real(math.sqrt(point))
	        	#Presion maxima tangencial permitida en la superficie
            		Tmax[j,i]=ro*Pn[j,i]
            		#Distribucion de presion tangencial lineal
            		Tx[j,i]=(v_x/L1-Y[j,i]*v_z/L3)*(X[j,i]-Xo);
                	Ty[j,i]=(v_y/L2)*(X[j,i]-Xo)+(0.5*v_z/L3)*(X[j,i]**2-Xo**2);
                	if abs(Tx[j,i])<Tmax[j,i]:
                		Tx[j,i]=Tx[j,i]
                	else:
                		Tx[j,i]=math.copysign(Tmax[j,i],Tx[j,i])
                	if abs(Ty[j,i])<Tmax[j,i]:
                		Ty[j,i]=Ty[j,i]
               		else:
               			Ty[j,i]=math.copysign(Tmax[j,i],Ty[j,i])
               		fx=fx+Tx[j,i]*DX*DY
               		fy=fy+Ty[j,i]*DX*DY
	return fx,fy
	
def shen(Nload,a,b,mu,ro,G,v_x,v_y,v_z):
	#Tabla de Constantes de Kalker
	C_11_0_1=np.array([2.47,2.51,2.59,2.68,2.78,2.88,2.98,3.09,3.19,3.29])
	C_11_0_2=np.array([3.40,3.51,3.65,3.82,4.06,4.37,4.84,5.57,6.96,10.7])
	C_11_0=np.hstack((C_11_0_1,C_11_0_2))
	C_11_1_1=np.array([3.29,3.31,3.37,3.44,3.53,3.62,3.72,3.81,3.91,4.01])
	C_11_1_2=np.array([4.12,4.22,4.36,4.54,4.78,5.10,5.57,6.34,7.78,11.7])
	C_11_1=np.hstack((C_11_1_1,C_11_1_2))
	C_11_2_1=np.array([4.93,4.85,4.81,4.80,4.82,4.83,4.91,4.97,5.05,5.12])
	C_11_2_2=np.array([5.20,5.30,5.42,5.58,5.80,6.11,5.57,7.34,8.82,12.9])
	C_11_2=np.hstack((C_11_2_1,C_11_2_2))
	#Matriz final C_11
	C_11_m=np.vstack((C_11_0,C_11_1,C_11_2))

	#Valores de C_22
	C_22_0_1=np.array([2.47,2.51,2.59,2.68,2.78,2.88,2.98,3.09,3.19,3.29])
	C_22_0_2=np.array([3.40,3.51,3.65,3.82,4.06,4.37,4.84,5.57,6.96,10.7])
	C_22_0=np.hstack((C_22_0_1,C_22_0_2))
	C_22_1_1=np.array([2.47,2.52,2.63,2.75,2.88,3.01,3.14,3.28,3.41,3.54])
	C_22_1_2=np.array([3.67,3.81,3.99,4.21,4.50,4.90,5.48,6.40,8.14,12.8])
	C_22_1=np.hstack((C_22_1_1,C_22_1_2))
	C_22_2_1=np.array([2.47,2.53,2.66,2.81,2.98,3.14,3.31,3.48,3.65,3.82])
	C_22_2_2=np.array([3.98,4.16,4.39,4.67,5.04,5.56,6.31,7.51,9.79,16.0])
	C_22_2=np.hstack((C_22_2_1,C_22_2_2))
	#Matriz final C_11
	C_22_m=np.vstack((C_22_0,C_22_1,C_22_2))

	#Valores de C_23
	C_23_0_1=np.array([0.,0.334,0.483,0.607,0.720,0.827,0.930,1.03,1.13,1.23])
	C_23_0_2=np.array([1.33,1.44,1.58,1.76,2.01,2.35,2.88,3.79,5.72,12.2])
	C_23_0=np.hstack((C_23_0_1,C_23_0_2))
	C_23_1_1=np.array([0.,0.473,0.603,0.715,0.823,0.929,1.03,1.14,1.25,1.36])
	C_23_1_2=np.array([1.47,1.59,1.75,1.95,2.23,2.62,3.24,4.32,6.63,14.6])
	C_23_1=np.hstack((C_23_1_1,C_23_1_2))
	C_23_2_1=np.array([0.,0.731,0.809,0.889,0.977,1.07,1.18,1.29,1.40,1.51])
	C_23_2_2=np.array([1.63,1.77,1.94,2.18,2.50,2.96,3.70,5.01,7.89,18.0])
	C_23_2=np.hstack((C_23_2_1,C_23_2_2))
	#Matriz final C_23
	C_23_m=np.vstack((C_23_0,C_23_1,C_23_2))

	#Se crea una fila valores para la relacion entre a/b denominada g (nomeclatura
	#propuesta por Iwinichi)
	g1=np.arange(0.,1.,0.1)
	g2=1./np.arange(1.,0.,-0.1)
	g=np.hstack((g1,g2))
	g,gridmu=np.meshgrid(g,[0.,0.25,0.5])

	#Se crea una funcion para interpolar
	C_11=spi.interp2d(g,gridmu,C_11_m,kind="linear")
	C_22=spi.interp2d(g,gridmu,C_22_m,kind="linear")
	C_23=spi.interp2d(g,gridmu,C_23_m,kind="linear")

	c11=C_11(a/b,mu)
	c22=C_22(a/b,mu)
	c23=C_23(a/b,mu)
	fx=G*a*b*c11*v_x
	fy=G*a*b*c22*v_y-G*a*b*math.sqrt(a*b)*c23*v_z
	F_t=math.sqrt(fx*fx+fy*fy)
	if F_t==0:
		fx=0
		fy=0
		return fx,fy 
	else:
		if F_t<3*(ro*Nload):
			ft=(ro*Nload)*((F_t/(ro*Nload))-((F_t/(ro*Nload))**2)/3+((F_t/(ro*Nload))**3)/27)
		else:
			ft=(ro*Nload)
		fx=ft*(fx/F_t)
		fy=ft*(fy/F_t)
		return fx,fy

def polanch(Nload,a,b,mu,ro,G,v_x,v_y,v_z):
	#Tabla de Constantes de Kalker
	C_11_0_1=np.array([2.47,2.51,2.59,2.68,2.78,2.88,2.98,3.09,3.19,3.29])
	C_11_0_2=np.array([3.40,3.51,3.65,3.82,4.06,4.37,4.84,5.57,6.96,10.7])
	C_11_0=np.hstack((C_11_0_1,C_11_0_2))
	C_11_1_1=np.array([3.29,3.31,3.37,3.44,3.53,3.62,3.72,3.81,3.91,4.01])
	C_11_1_2=np.array([4.12,4.22,4.36,4.54,4.78,5.10,5.57,6.34,7.78,11.7])
	C_11_1=np.hstack((C_11_1_1,C_11_1_2))
	C_11_2_1=np.array([4.93,4.85,4.81,4.80,4.82,4.83,4.91,4.97,5.05,5.12])
	C_11_2_2=np.array([5.20,5.30,5.42,5.58,5.80,6.11,5.57,7.34,8.82,12.9])
	C_11_2=np.hstack((C_11_2_1,C_11_2_2))
	#Matriz final C_11
	C_11_m=np.vstack((C_11_0,C_11_1,C_11_2))

	#Valores de C_22
	C_22_0_1=np.array([2.47,2.51,2.59,2.68,2.78,2.88,2.98,3.09,3.19,3.29])
	C_22_0_2=np.array([3.40,3.51,3.65,3.82,4.06,4.37,4.84,5.57,6.96,10.7])
	C_22_0=np.hstack((C_22_0_1,C_22_0_2))
	C_22_1_1=np.array([2.47,2.52,2.63,2.75,2.88,3.01,3.14,3.28,3.41,3.54])
	C_22_1_2=np.array([3.67,3.81,3.99,4.21,4.50,4.90,5.48,6.40,8.14,12.8])
	C_22_1=np.hstack((C_22_1_1,C_22_1_2))
	C_22_2_1=np.array([2.47,2.53,2.66,2.81,2.98,3.14,3.31,3.48,3.65,3.82])
	C_22_2_2=np.array([3.98,4.16,4.39,4.67,5.04,5.56,6.31,7.51,9.79,16.0])
	C_22_2=np.hstack((C_22_2_1,C_22_2_2))
	#Matriz final C_11
	C_22_m=np.vstack((C_22_0,C_22_1,C_22_2))

	#Valores de C_23
	C_23_0_1=np.array([0.,0.334,0.483,0.607,0.720,0.827,0.930,1.03,1.13,1.23])
	C_23_0_2=np.array([1.33,1.44,1.58,1.76,2.01,2.35,2.88,3.79,5.72,12.2])
	C_23_0=np.hstack((C_23_0_1,C_23_0_2))
	C_23_1_1=np.array([0.,0.473,0.603,0.715,0.823,0.929,1.03,1.14,1.25,1.36])
	C_23_1_2=np.array([1.47,1.59,1.75,1.95,2.23,2.62,3.24,4.32,6.63,14.6])
	C_23_1=np.hstack((C_23_1_1,C_23_1_2))
	C_23_2_1=np.array([0.,0.731,0.809,0.889,0.977,1.07,1.18,1.29,1.40,1.51])
	C_23_2_2=np.array([1.63,1.77,1.94,2.18,2.50,2.96,3.70,5.01,7.89,18.0])
	C_23_2=np.hstack((C_23_2_1,C_23_2_2))
	#Matriz final C_23
	C_23_m=np.vstack((C_23_0,C_23_1,C_23_2))

	#Se crea una fila valores para la relacion entre a/b denominada g (nomeclatura
	#propuesta por Iwinichi)
	g1=np.arange(0.,1.,0.1)
	g2=1./np.arange(1.,0.,-0.1)
	g=np.hstack((g1,g2))
	g,gridmu=np.meshgrid(g,[0.,0.25,0.5])

	#Se crea una funcion para interpolar
	C_11=spi.interp2d(g,gridmu,C_11_m,kind="linear")
	C_22=spi.interp2d(g,gridmu,C_22_m,kind="linear")
	C_23=spi.interp2d(g,gridmu,C_23_m,kind="linear")

	c11=C_11(a/b,mu)
	c22=C_22(a/b,mu)
	c23=C_23(a/b,mu)	
	#El modelo requiere determinar la fuga tangencial, para ello se calcula la fuga lateral
	#considerando la fuga rotacional.
	if abs(v_y+v_z*a)>abs(v_y):
		vy=v_y+v_z*a
	else:
		vy=v_y
	v=math.sqrt(v_x**2+vy**2)
	if v==0:
		fx=0
		fy=0
		return fx,fy	
	else:
		cjj=math.sqrt((c11*v_x/v)**2+(c22*v_y/v)**2)
		#Gradiente de deformacion
		eta=0.25*G*math.pi*a*b*cjj*v/(ro*Nload)
		ft=-(2*ro*Nload/math.pi)*((eta/(1+eta**2))+math.atan(eta))
		fx=ft*v_x/v
		fy=ft*v_y/v
		return fx,fy

