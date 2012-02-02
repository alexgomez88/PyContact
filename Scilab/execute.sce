getd();
X=0:0.01:1;
Y1=X;
Y2=X;
Y3=X;
Y4=X;
Y5=X;
for i=1:length(X)
	Y1(i)=carter(30000,0.0002,0.0001,0.25,0.55,300*10^9,X(i),0,0)/(30000*0.55);
	[FX,FY]=kalkerL(30000,0.0002,0.0001,0.25,0.55,300*10^9,X(i),0,0);
	Y2(i)=FX/(30000*0.55);
	[FX,FY]=kalkerS(30000,0.0002,0.0001,0.25,0.55,300*10^9,X(i),0,0);
	Y3(i)=FX/(30000*0.55);
	[FX,FY]=shen(30000,0.0002,0.0001,0.25,0.55,300*10^9,X(i),0,0);
	Y4(i)=FX/(30000*0.55);
	[FX,FY]=polanch(30000,0.0002,0.0001,0.25,0.55,300*10^9,X(i),0,0);
	Y5(i)=FX/(30000*0.55);
end
figure(1)
demo0=plot(X,[Y1' Y2' Y3' Y4' Y5'],'LineWidth',6);
//set(demo0,'LineWidth',6);
title('Modelos de Contacto rueda-riel vs fuga')
xlabel('Fuga')
ylabel('Relación Carga vs Maxima Carga Tangencial')
legend ("carter","kalkerL","kalkerS","shen","polanch");
xs2jpg(1,'demo1.jpg');
n=1:50;
for i=n
	tic();
	for j=1:i
		FX=carter(30000,0.0002,0.0001,0.25,0.55,300*10^9,0.001,0,0)/(30000*0.55);
	end
	T1(i)=toc();
	tic();
	for j=1:i
		FX=kalkerL(30000,0.0002,0.0001,0.25,0.55,300*10^9,0.001,0,0)/(30000*0.55);
	end
	T2(i)=toc();
	tic();
	for j=1:i
		FX=kalkerS(30000,0.0002,0.0001,0.25,0.55,300*10^9,0.001,0,0)/(30000*0.55);
	end
	T3(i)=toc();
	tic();
	for j=1:i
		FX=shen(30000,0.0002,0.0001,0.25,0.55,300*10^9,0.001,0,0)/(30000*0.55);
	end
	T4(i)=toc();
	tic();
	for j=1:i
		FX=polanch(30000,0.0002,0.0001,0.25,0.55,300*10^9,0.001,0,0)/(30000*0.55);
	end
	T5(i)=toc();
end
figure(2)
demo1=plot(n,[T1 T2 T3 T4 T5],'LineWidth',6);
//set(demo1,'LineWidth',6);
title('Tiempo de computo entre modelos de contacto rueda-riel')
xlabel('Iteraciones')
ylabel('Tiempo (s)')
legend ("carter","kalkerL","kalkerS","shen","polanch");
xs2jpg(2,'demo2.jpg');
figure(3)
demo2=plot(n,[T1 T2 T4 T5],'LineWidth',6);
//set(demo1,'LineWidth',6);
title('Tiempo de computo entre modelos de contacto rueda-riel')
xlabel('Iteraciones')
ylabel('Tiempo (s)')
legend ("carter","kalkerL","shen","polanch");
xs2jpg(3,'demo3.jpg');