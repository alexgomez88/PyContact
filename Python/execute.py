import numpy as np
import pylab
from quicktang import *
m=100
X=np.array(np.arange(0,m+1))/m
Y1=X;
Y2=X;
Y3=X;
Y4=X;
Y5=X;
for i in range(0,m+1):
	YF=np.array([0.,0.])
	F=carter(30000.,0.0002,0.0001,0.25,0.55,300.*10**9,X[i],0,0)
	Y1[i]=F[1]/(30000.*0.55);
	F=kalkerL(30000.,0.0002,0.0001,0.25,0.55,300.*10**9,X[i],0,0);
	Y2[i]=F[1]/(30000.*0.55);
	F=kalkerS(30000.,0.0002,0.0001,0.25,0.55,300.*10**9,X[i],0,0);
	Y3[i]=F[1]/(30000.*0.55);
	F=shen(30000.,0.0002,0.0001,0.25,0.55,300.*10**9,X[i],0,0);
	Y4[i]=F[1]/(30000.*0.55);
	F=polanch(30000.,0.0002,0.0001,0.25,0.55,300.*10**9,X[i],0,0);
	Y5[i]=F[1]/(30000.*0.55);

pylab.figure(1)
graph1=demo1.add_subplot(111)
pylab.plot(X,Y1,X,Y2,X,Y3,X,Y4,X,Y5);
pylab.setp(graph1,linewidth=6);
pylab.title('Modelos de Contacto rueda-riel vs fuga')
pylab.xlabel('Fuga')
pylab.ylabel('Relacion Carga vs Maxima Carga Tangencial')
pylab.legend ("carter","kalkerL","kalkerS","shen","polanch");
pylab.show()

#Tiempo de Computo
n=5
for i in range(1,n+1):
	for j in range(1,i):
		F=carter(30000.,0.0002,0.0001,0.25,0.55,300.*10**9,0.01,0,0)
	for j in range(1,i):
		F=kalkerL(30000.,0.0002,0.0001,0.25,0.55,300.*10**9,0.01,0,0)
	for j in range(1,i):
		F=kalkerS(30000.,0.0002,0.0001,0.25,0.55,300.*10**9,0.01,0,0)
	for j in range(1,i):
		F=shen(30000.,0.0002,0.0001,0.25,0.55,300.*10**9,0.01,0,0)
	for j in range(1,i):
		F=polanch(30000.,0.0002,0.0001,0.25,0.55,300.*10**9,0.01,0,0)
pylab.figure(2)
graph2=demo2.add_subplot(111)
pylab.plot(X,Y1,X,Y2,X,Y3,X,Y4,X,Y5);
pylab.setp(graph1,linewidth=6);
pylab.title('Modelos de Contacto rueda-riel vs fuga')
pylab.xlabel('Fuga')
pylab.ylabel('Relacion Carga vs Maxima Carga Tangencial')
pylab.legend ("carter","kalkerL","kalkerS","shen","polanch");
pylab.show()
#saveas(demo0,'demo1.jpg');
#n=1:50;
#for i=n
#	tic();
#	for j=1:i
#		FX=carter(30000,0.0002,0.0001,0.25,0.55,300*10^9,0.001,0,0)/(30000*0.55);
#	end
#	T1(i)=toc();
#	tic();
#	for j=1:i
#		FX=kalkerL(30000,0.0002,0.0001,0.25,0.55,300*10^9,0.001,0,0)/(30000*0.55);
#	end
#	T2(i)=toc();
#	tic();
#	for j=1:i
#		FX=kalkerS(30000,0.0002,0.0001,0.25,0.55,300*10^9,0.001,0,0)/(30000*0.55);
#	end
#	T3(i)=toc();
#	tic();
#	for j=1:i
#		FX=shen(30000,0.0002,0.0001,0.25,0.55,300*10^9,0.001,0,0)/(30000*0.55);
#	end
#	T4(i)=toc();
#	tic();
#	for j=1:i
#		FX=polanch(30000,0.0002,0.0001,0.25,0.55,300*10^9,0.001,0,0)/(30000*0.55);
#	end
#	T5(i)=toc();
#end
#figure('Name','Comparacion de tiempo de ejecucion')
#demo1=plot(n,T1,n,T2,n,T3,n,T4,n,T5);
#set(demo1,'LineWidth',6);
#title('Tiempo de computo entre modelos de contacto rueda-riel')
#xlabel('Iteraciones')
#ylabel('Tiempo (s)')
#legend ("carter","kalkerL","kalkerS","shen","polanch");
#saveas(demo1,'demo2.jpg');
#figure('Name','Comparacion de tiempo de ejecucion')
#demo2=plot(n,T1,n,T2,n,T4,n,T5);
#set(demo2,'LineWidth',6);
#title('Tiempo de computo entre modelos de contacto rueda-riel')
#xlabel('Iteraciones')
#ylabel('Tiempo (s)')
#legend ("carter","kalkerL","shen","polanch");
#saveas(demo2,'demo3.jpg');
