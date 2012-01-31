#Se crea una "clase" que contenga los modelos de contacto rueda riel de
#Carter, Kalker (Lineal), Kalker (Simplificado), Shen-Hendrick-Elkins,
#Polach y el modelo propuesto RailCCS.

#Estas funciones son denominadas carter, kalkerL, kalkerS, shen, polanch y railccs.
#la clase QUICK_TANG solo calcula las cargas.

from numpy import *
import scipy
import scipy.interpolate

class QUICKTANG:
	def __init__(self,xNload,xa,xb,xmu,xro,xG):
		#Se carga a la funcion tangente los datos obtenidos por el modelo
		#de Hertz, igualmente se determina los coeficientes de Kalker,
		#que son usados en los modelos de contacto rueda riel
		
		#Caracteristicas de la superficie de contacto:
		#Diametro longitudinal
		self.a=xa
		#Diametro lateral
		self.b=xb
		#Carga Vertical
		self.Nload=xNload
		#Modulo de poisson
		self.mu=xmu
		#Coeficiente de roce
		self.ro=xro
		#Modulo de Corte
		self.G=xG

		#--Constantes de Kalker.
		#Valores de C_11
		C_11_0_1=array([2.47,2.51,2.59,2.68,2.78,2.88,2.98,3.09,3.19,3.29])
		C_11_0_2=array([3.40,3.51,3.65,3.82,4.06,4.37,4.84,5.57,6.96,10.7])
		C_11_0=hstack((C_11_0_1,C_11_0_2))
		C_11_1_1=array([3.29,3.31,3.37,3.44,3.53,3.62,3.72,3.81,3.91,4.01])
		C_11_1_2=array([4.12,4.22,4.36,4.54,4.78,5.10,5.57,6.34,7.78,11.7])
		C_11_1=hstack((C_11_1_1,C_11_1_2))
		C_11_2_1=array([4.93,4.85,4.81,4.80,4.82,4.83,4.91,4.97,5.05,5.12])
		C_11_2_2=array([5.20,5.30,5.42,5.58,5.80,6.11,5.57,7.34,8.82,12.9])
		C_11_2=hstack((C_11_2_1,C_11_2_2))
		#Matriz final C_11
		C_11_m=vstack((C_11_0,C_11_1,C_11_2))

		#Valores de C_22
		C_22_0_1=array([2.47,2.51,2.59,2.68,2.78,2.88,2.98,3.09,3.19,3.29])
		C_22_0_2=array([3.40,3.51,3.65,3.82,4.06,4.37,4.84,5.57,6.96,10.7])
		C_22_0=hstack((C_22_0_1,C_22_0_2))
		C_22_1_1=array([2.47,2.52,2.63,2.75,2.88,3.01,3.14,3.28,3.41,3.54])
		C_22_1_2=array([3.67,3.81,3.99,4.21,4.50,4.90,5.48,6.40,8.14,12.8])
		C_22_1=hstack((C_22_1_1,C_22_1_2))
		C_22_2_1=array([2.47,2.53,2.66,2.81,2.98,3.14,3.31,3.48,3.65,3.82])
		C_22_2_2=array([3.98,4.16,4.39,4.67,5.04,5.56,6.31,7.51,9.79,16.0])
		C_22_2=hstack((C_22_2_1,C_22_2_2))
		#Matriz final C_11
		C_22_m=vstack((C_22_0,C_22_1,C_22_2))

		#Valores de C_23
		C_23_0_1=array([0,0.334,0.483,0.607,0.720,0.827,0.930,1.03,1.13,1.23])
		C_23_0_2=array([1.33,1.44,1.58,1.76,2.01,2.35,2.88,3.79,5.72,12.2])
		C_23_0=hstack((C_23_0_1,C_23_0_2))
		C_23_1_1=array([0,0.473,0.603,0.715,0.823,0.929,1.03,1.14,1.25,1.36])
		C_23_1_2=array([1.47,1.59,1.75,1.95,2.23,2.62,3.24,4.32,6.63,14.6])
		C_23_1=hstack((C_23_1_1,C_23_1_2))
		C_23_2_1=array([0,0.731,0.809,0.889,0.977,1.07,1.18,1.29,1.40,1.51])
		C_23_2_2=array([1.63,1.77,1.94,2.18,2.50,2.96,3.70,5.01,7.89,18.0])
		C_23_2=hstack((C_23_2_1,C_23_2_2))
		#Matriz final C_23
		C_23_m=vstack((C_23_0,C_23_1,C_23_2))

		#Se crea una fila valores para la relacion entre a/b denominada g (nomeclatura
		#propuesta por Iwinichi)
		g1=arange(0,1,0.1)
		g2=1/arange(1,0,-0.1)
		g=hstack((g1,g2))
		g,gridmu=meshgrid(g,[0,0.25,0.5])

		#Se crea una funcion para interpolar
		self.C_11=scipy.interpolate.interp2d(g,gridmu,C_11_m,kind="linear")
		self.C_22=scipy.interpolate.interp2d(g,gridmu,C_22_m,kind="linear")
		self.C_23=scipy.interpolate.interp2d(g,gridmu,C_23_m,kind="linear")

	def carter(self,v_x,v_y,v_z):
		#Coeficiente de Carter
		k=4*0.430/(self.mu*self.a)
		#Modelo de Carter, se separa el comportamiento de adhesion del deslizamiento.
		if k*abs(v_x)<2:
			fx=(self.ro*self.NLoad)*(0.25*k*k*v_x*abs(v_x)-k*abs(v_x))
		else:
			fx=(self.ro*self.NLoad)*abs(v_x)/v_x
		#El modelo de Carter, no interpreta cargas laterales, por tanto fy es 0.
		return fx,0

	def kalkerL(self,v_x,v_y,v_z):
		#Calcula las cargas longitudinales y laterales considerando la fuga como la
		#deformacion en la superfie, por tanto el comportamiento del materal en el punto
		#de contacto es lineal.
		c11=self.C_11(self.a/self.b,self.mu)
		c22=self.C_22(self.a/self.b,self.mu)
		c23=self.C_23(self.a/self.b,self.mu)
		fx=-self.G*self.a*self.b*c11*v_x
		fy=-self.G*self.a*self.b*c22*v_y-self.G*self.a*self.b*sqrt(self.a*self.b)*c23*v_z
		ftangmax=self.ro*self.Nload
		if abs(fx)>(ftangmax):
			fx=(ftangmax)*abs(fx)/fx
		if abs(fy)>(ftangmax):
			fy=(ftangmax)*abs(fy)/fy

		return fx,fy
	def shen(self,v_x,v_y,v_z):
		#Calcula las cargas longitudinales y laterales considerando las cargas obtenidas por el
		#modelo de Kalker, suavizando la curva de obtenida por el modelo lineal de Kalker.
		fx,fy=kalkerL(v_x,v_y,v_z)
		F_t=sqrt(fx*fx+fy*fy)
		if F_t<3*(self.ro*self.NLoad):
			ft=(self.ro*self.NLoad)*((F_t/(self.ro*self.NLoad))-((F_t/(self.ro*self.NLoad))**2)/3+((F_t/(self.ro*self.NLoad))**3)/27)
		else:
			ft=(self.ro*self.NLoad)
		fx=ft*(fx/F_t)
		fy=ft*(fy/F_t)
		return fx,fy

	def kalkerS(self,v_x,v_y,v_z):
		#Calcula inicialmente una serie de puntos X y Y de modo que se calcule el domo de saturacion
		#de presiones tangenciales, para ello se hace con un numero standar de 10000 iteraciones.
		DY=2*self.b/100
		X=zeros((100,100))
		Y=zeros((100,100))
		Pn=zeros((100,100))
		Tmax=zeros((100,100))
		Tx=zeros((100,100))
		Ty=zeros((100,100))
		#Constantes geometricas de de Kalker
		c11=self.C_11(self.a/self.b,self.mu)
		c22=self.C_22(self.a/self.b,self.mu)
		c23=self.C_23(self.a/self.b,self.mu)
		#Coeficientes elasticos de Kalker
		L1=8*self.a/(3*self.G*c11);
		L2=8*self.a/(3*self.G*c22);
		L3=pi*(self.a**2)/(4*self.G*sqrt(self.a*self.b)*c23);
		#Inicio de las iteraciones verticales
		for j in range(0,100):
			fx=0
			fy=0
			#Determina el valor de la coordenada lateral del punto de estudio
    			Yo=DY*(50-j)
    			#Determina el valor de la coordenada del primer punto de estudio
    			Xo=-self.a*real(sqrt(1-(Yo/self.b)**2))
    			#Determina la longitud del segmento longitudinal de estudio
    			DX=2*self.a*real(sqrt(1-(Yo/self.b)**2))/100
    			#Inicia las iteraciones longitudinales
    			for i in range(0,100):
    				#Llenado de la matriz de coordenadas de Y
                		Y[j,i]=Yo;
                		#Llenado de la matriz de coordenadas de X
            			X[j,i]=Xo+DX*(i);
            			#Se determina la presion normal aplicada sobre el punto de estudio
            			Pn[j,i]=((3*self.Nload)/(2*pi*self.a*self.b))*real(sqrt(1-(X[j,i]/self.a)**2-(Y[j,i]/self.b)**2))
            			#Presion maxima tangencial permitida en la superficie
            			Tmax[j,i]=self.ro*Pn[j,i]
            			#Distribucion de presion tangencial lineal
            			Tx[j,i]=(v_x/L1-Y[j,i]*v_z/L3)*(X[j,i]-Xo);
                		Ty[j,i]=(v_y/L2)*(X[j,i]-Xo)+(0.5*v_z/L3)*(X[j,i]**2-Xo**2);
                		if abs(Tx[j,i])<Tmax[j,i]:
                			Tx[j,i]=Tx[j,i]
                		else:
                			Tx[j,i]=Tmax[j,i]*abs(Tx[j,i])/Tx[j,i]
                		if abs(Ty[j,i])<Tmax[j,i]:
                			Ty[j,i]=Ty[j,i]
                		else:
                			Ty[j,i]=Tmax[j,i]*abs(Ty[j,i])/Ty[j,i]
                		fx=fx+Tx[j,i]*DX*DY
                		fy=fy+Ty[j,i]*DX*DY
                return fx,fy
	def polanch(self,v_x,v_y,v_z):
		#El modelo requiere determinar la fuga tangencial, para ello se calcula la fuga lateral
		#considerando la fuga rotacional.
		if abs(v_y+v_z*self.a)>abs(v_y):
			vy=v_y+v_z*self.a
		else:
			vy=v_y
		v=sqrt(v_x**2+vy**2)
		#Constantes geometricas de de Kalker
		c11=self.C_11(self.a/self.b,self.mu)
		c22=self.C_22(self.a/self.b,self.mu)
		c23=self.C_23(self.a/self.b,self.mu)
		cjj=sqrt((c11*v_x/v)**2+(c22*v_y/v)**2)
		#Gradiente de deformacion
		eta=0.25*self.G*pi*self.a*self.b*cjj*v/(self.ro*self.Nload)
		ft=-(2*self.ro*self.Nload/pi)*((eta/(1+eta**2))+arctan(eta))
		fx=ft*v_x/v
		fy=ft*v_y/v
		return fx,fy
