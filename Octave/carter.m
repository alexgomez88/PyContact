function [fx,fy]=carter(Nload,a,b,mu,ro,G,v_x,v_y,v_z)
	%Coeficiente de Carter
	k=4.*0.430/(mu*a);
	%Modelo de Carter, se separa el comportamiento de adhesion del deslizamiento.
	if (k*abs(v_x)<2)
		fx=(ro*Nload)*(0.25*(k**2)*v_x*abs(v_x)-k*abs(v_x));
	else
		fx=(ro*Nload)*abs(v_x)/v_x;
	end
	%El modelo de Carter, no interpreta cargas laterales, por tanto fy es 0.
	fy=0;
end
