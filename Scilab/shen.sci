function [fx,fy]=shen(Nload,a,b,mu,ro,G,v_x,v_y,v_z)
    //Calcula las cargas longitudinales y laterales considerando las cargas 
	//obtenidas por el modelo de Kalker, suavizando la curva de obtenida por 
    //el modelo lineal de Kalker.
    [fx,fy]=kalkerL(Nload,a,b,mu,ro,G,v_x,v_y,v_z);
	F_t=sqrt(fx**2+fy**2);
	if (F_t<3*(ro*Nload))
		ft=(ro*Nload)*((F_t/(ro*Nload))-((F_t/(ro*Nload))**2)/3+((F_t/(ro*Nload))**3)/27);
	else
		ft=(ro*Nload);
    end		
    fx=ft*(fx/F_t);
	fy=ft*(fy/F_t);
	
endfunction