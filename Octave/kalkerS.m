function [fx,fy]=kalkerS(Nload,a,b,mu,ro,G,v_x,v_y,v_z)
    	%--Constantes de Kalker.
	%Tabla de Valores de C_11
	C_11_0_1=[2.47,2.51,2.59,2.68,2.78,2.88,2.98,3.09,3.19,3.29];
	C_11_0_2=[3.40,3.51,3.65,3.82,4.06,4.37,4.84,5.57,6.96,10.7];
	C_11_0=[C_11_0_1,C_11_0_2];
	C_11_1_1=[3.29,3.31,3.37,3.44,3.53,3.62,3.72,3.81,3.91,4.01];
	C_11_1_2=[4.12,4.22,4.36,4.54,4.78,5.10,5.57,6.34,7.78,11.7];
	C_11_1=[C_11_1_1,C_11_1_2];
	C_11_2_1=[4.93,4.85,4.81,4.80,4.82,4.83,4.91,4.97,5.05,5.12];
	C_11_2_2=[5.20,5.30,5.42,5.58,5.80,6.11,5.57,7.34,8.82,12.9];
	C_11_2=[C_11_2_1,C_11_2_2];
	%Matriz final C_11
	C_11=[C_11_0',C_11_1',C_11_2'];
	%Tabla de Valores de C_22
	C_22_0_1=[2.47,2.51,2.59,2.68,2.78,2.88,2.98,3.09,3.19,3.29];
	C_22_0_2=[3.40,3.51,3.65,3.82,4.06,4.37,4.84,5.57,6.96,10.7];
	C_22_0=[C_22_0_1,C_22_0_2];
	C_22_1_1=[2.47,2.52,2.63,2.75,2.88,3.01,3.14,3.28,3.41,3.54];
	C_22_1_2=[3.67,3.81,3.99,4.21,4.50,4.90,5.48,6.40,8.14,12.8];
	C_22_1=[C_22_1_1,C_22_1_2];
	C_22_2_1=[2.47,2.53,2.66,2.81,2.98,3.14,3.31,3.48,3.65,3.82];
	C_22_2_2=[3.98,4.16,4.39,4.67,5.04,5.56,6.31,7.51,9.79,16.0];
	C_22_2=[C_22_2_1,C_22_2_2];
	%Matriz final C_11
	C_22=[C_22_0',C_22_1',C_22_2'];
	%Tabla de Valores de C_23
	C_23_0_1=[0,0.334,0.483,0.607,0.720,0.827,0.930,1.03,1.13,1.23];
	C_23_0_2=[1.33,1.44,1.58,1.76,2.01,2.35,2.88,3.79,5.72,12.2];
	C_23_0=[C_23_0_1,C_23_0_2];
	C_23_1_1=[0,0.473,0.603,0.715,0.823,0.929,1.03,1.14,1.25,1.36];
	C_23_1_2=[1.47,1.59,1.75,1.95,2.23,2.62,3.24,4.32,6.63,14.6];
	C_23_1=[C_23_1_1,C_23_1_2];
	C_23_2_1=[0,0.731,0.809,0.889,0.977,1.07,1.18,1.29,1.40,1.51];
	C_23_2_2=[1.63,1.77,1.94,2.18,2.50,2.96,3.70,5.01,7.89,18.0];
	C_23_2=[C_23_2_1,C_23_2_2];
	%Matriz final C_23
	C_23=[C_23_0',C_23_1',C_23_2'];
	%Tabla de valores para interpolar de la relación entre el diametro mayor
	%y el diametro menor de la elipse de contacto.
	g1=0:0.1:0.9;
	g2=1./[1:-0.1:0.1];
	g=[g1,g2];
	[mu,g]=meshgrid([0,0.25,0.5],g);
	%Se calculan las constantes de Kalker C11, C22, C23, mediante la interpolación
	% de las tablas respectivas y la relación entre diametros.
	c11=interp2(mu,real(g),C_11,vmu,real(a/b));
	c22=interp2(mu,real(g),C_22,vmu,real(a/b));
	c23=interp2(mu,real(g),C_23,vmu,real(a/b));

    	%Calcula inicialmente una serie de puntos X y Y de modo que se calcule el domo de saturacion
	%de presiones tangenciales, para ello se hace con un numero standar de 10000 iteraciones.
	DY=2*b/100;
    	X=zeros(100,100);
	Y=zeros(100,100);
	Pn=zeros(100,100);
	Tmax=zeros(100,100);
	Tx=zeros(100,100);
	Ty=zeros(100,100);
	
    	%Coeficientes elasticos de Kalker
	L1=8*a/(3*G*c11);
	L2=8*a/(3*G*c22);
	L3=pi*(a**2)/(4*G*sqrt(a*b)*C_23);
	%Inicio de las iteraciones verticales
	for j=1:100
		fx=0;
		fy=0;
		%Determina el valor de la coordenada lateral del punto de estudio
        	Yo=DY*(50-j);
        	%Determina el valor de la coordenada del primer punto de estudio
		Xo=-a*real(sqrt(1-(Yo/b)**2));
		%Determina la longitud del segmento longitudinal de estudio
        	DX=2*a*real(sqrt(1-(Yo/b)**2))/100;
        	%Inicia las iteraciones longitudinales
		for i=1:100
            		%Llenado de la matriz de coordenadas de Y
            		Y(j,i)=Yo;
            		%Llenado de la matriz de coordenadas de X
            		X(j,i)=Xo+DX*(i);
            		%Se determina la presion normal aplicada sobre el punto de estudio
            		Pn(j,i)=((3*Nload)/(2*%pi*a*b))*real(sqrt(1-(X(j,i)/a)**2-(Y(j,i)/b)**2));
            		%Presion maxima tangencial permitida en la superficie
            		Tmax(j,i)=ro*Pn(j,i);
            		%Distribucion de presion tangencial lineal
            		Tx(j,i)=(v_x/L1-Y(j,i)*v_z/L3)*(X(j,i)-Xo);
            		Ty(j,i)=(v_y/L2)*(X(j,i)-Xo)+(0.5*v_z/L3)*(X(j,i)**2-Xo**2);
            		if (abs(Tx(j,i))<=Tmax(j,i))
            			Tx(j,i)=Tx(j,i);
            		else
                		Tx(j,i)=Tmax(j,i)*abs(Tx(j,i))/Tx(j,i);
            		end
            		if (abs(Ty(j,i))<=Tmax(j,i))
            			Ty(j,i)=Ty(j,i);
            		else
                		Ty(j,i)=Tmax(j,i)*abs(Ty(j,i))/Ty(j,i);
            		end
            		%Integración de las componentes tangenciales en la dirección
            		%longitudinal y lateral
            		fx=fx+Tx(j,i)*DX*DY;
            		fy=fy+Ty(j,i)*DX*DY;
        	end
	end
                
end
