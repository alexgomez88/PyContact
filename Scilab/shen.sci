function [fx,fy]=shen(Nload,a,b,mu,ro,G,v_x,v_y,v_z)
    //Calcula las cargas longitudinales y laterales considerando las cargas 
	//obtenidas por el modelo de Kalker, suavizando la curva de obtenida por 
    //el modelo lineal de Kalker.
        //--Constantes de Kalker.
	//Valores de C_11
	C_11_0_1=[2.47,2.51,2.59,2.68,2.78,2.88,2.98,3.09,3.19,3.29];
	C_11_0_2=[3.40,3.51,3.65,3.82,4.06,4.37,4.84,5.57,6.96,10.7];
	C_11_0=[C_11_0_1,C_11_0_2]
	C_11_1_1=[3.29,3.31,3.37,3.44,3.53,3.62,3.72,3.81,3.91,4.01];
	C_11_1_2=[4.12,4.22,4.36,4.54,4.78,5.10,5.57,6.34,7.78,11.7];
	C_11_1=[C_11_1_1,C_11_1_2];
	C_11_2_1=[4.93,4.85,4.81,4.80,4.82,4.83,4.91,4.97,5.05,5.12];
	C_11_2_2=[5.20,5.30,5.42,5.58,5.80,6.11,5.57,7.34,8.82,12.9];
	C_11_2=[C_11_2_1,C_11_2_2];

	//Valores de C_22
	C_22_0_1=[2.47,2.51,2.59,2.68,2.78,2.88,2.98,3.09,3.19,3.29];
	C_22_0_2=[3.40,3.51,3.65,3.82,4.06,4.37,4.84,5.57,6.96,10.7];
	C_22_0=[C_22_0_1,C_22_0_2];
	C_22_1_1=[2.47,2.52,2.63,2.75,2.88,3.01,3.14,3.28,3.41,3.54];
	C_22_1_2=[3.67,3.81,3.99,4.21,4.50,4.90,5.48,6.40,8.14,12.8];
	C_22_1=[C_22_1_1,C_22_1_2];
	C_22_2_1=[2.47,2.53,2.66,2.81,2.98,3.14,3.31,3.48,3.65,3.82];
	C_22_2_2=[3.98,4.16,4.39,4.67,5.04,5.56,6.31,7.51,9.79,16.0];
	C_22_2=[C_22_2_1,C_22_2_2];

	//Valores de C_23
	C_23_0_1=[0,0.334,0.483,0.607,0.720,0.827,0.930,1.03,1.13,1.23];
	C_23_0_2=[1.33,1.44,1.58,1.76,2.01,2.35,2.88,3.79,5.72,12.2];
	C_23_0=[C_23_0_1,C_23_0_2];
	C_23_1_1=[0,0.473,0.603,0.715,0.823,0.929,1.03,1.14,1.25,1.36];
	C_23_1_2=[1.47,1.59,1.75,1.95,2.23,2.62,3.24,4.32,6.63,14.6];
	C_23_1=[C_23_1_1,C_23_1_2];
	C_23_2_1=[0,0.731,0.809,0.889,0.977,1.07,1.18,1.29,1.40,1.51];
	C_23_2_2=[1.63,1.77,1.94,2.18,2.50,2.96,3.70,5.01,7.89,18.0];
	C_23_2=[C_23_2_1,C_23_2_2];

	//Se crea una fila valores para la relacion entre a/b denominada g (nomeclatura
	//propuesta por Iwinichi)
	g1=0:0.1:1;
	g2=(0.9:-0.1:0.1)^-1;
	g=[g1,g2];

    //Interpolacion g
    C_11_a=interp1(g,C_11_0,a/b,'linear');
    C_11_b=interp1(g,C_11_1,a/b,'linear');
    C_11_c=interp1(g,C_11_2,a/b,'linear');
    C_22_a=interp1(g,C_22_0,a/b,'linear');
    C_22_b=interp1(g,C_22_1,a/b,'linear');
    C_22_c=interp1(g,C_22_2,a/b,'linear');
    C_23_a=interp1(g,C_23_0,a/b,'linear');
    C_23_b=interp1(g,C_23_1,a/b,'linear');
    C_23_c=interp1(g,C_23_2,a/b,'linear');
    
    //Valores de C
    C_11=interp1([0,0.25,0.5],[C_11_a,C_11_b,C_11_c],mu,'linear');
    C_22=interp1([0,0.25,0.5],[C_22_a,C_22_b,C_22_c],mu,'linear');
    C_23=interp1([0,0.25,0.5],[C_23_a,C_23_b,C_23_c],mu,'linear');
    
    //Calcula las cargas longitudinales y laterales considerando la fuga como la
	//deformacion en la superfie, por tanto el comportamiento del materal en el punto
	//de contacto es lineal.
	fx=G*a*b*C_11*v_x;
	fy=G*a*b*C_22*v_y-G*a*b*sqrt(a*b)*C_23*v_z;
	
	F_t=sqrt(fx**2+fy**2);
    if (F_t==0)
		fx=0;
		fy=0;
	else
        if (F_t<3*(ro*Nload))
            ft=(ro*Nload)*((F_t/(ro*Nload))-((F_t/(ro*Nload))**2)/3+((F_t/(ro*Nload))**3)/27);    
        else
            ft=(ro*Nload);
        end
        fx=ft*(fx/F_t);
        fy=ft*(fy/F_t);
    end		

	
endfunction