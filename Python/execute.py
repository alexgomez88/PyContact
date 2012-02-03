import numpy as np
import pylab
from quicktang import *
import time
m=100.
X=np.array(np.arange(0,m+1))/m
Y1=np.array(np.arange(0,m+1))/m
Y2=np.array(np.arange(0,m+1))/m
Y3=np.array(np.arange(0,m+1))/m
Y4=np.array(np.arange(0,m+1))/m
Y5=np.array(np.arange(0,m+1))/m
for i in range(0,int(m)+1):
	Y1[i]=abs(carter(30000.,0.0002,0.0001,0.25,0.55,300.*10**9,X[i],0,0)[0]/(30000.*0.55))
	Y2[i]=abs(kalkerL(30000.,0.0002,0.0001,0.25,0.55,300.*10**9,X[i],0,0)[0]/(30000.*0.55))
	Y3[i]=abs(kalkerS(30000.,0.0002,0.0001,0.25,0.55,300.*10**9,X[i],0,0)[0]/(30000.*0.55))
	Y4[i]=abs(shen(30000.,0.0002,0.0001,0.25,0.55,300.*10**9,X[i],0,0)[0]/(30000.*0.55))
	Y5[i]=abs(polanch(30000.,0.0002,0.0001,0.25,0.55,300.*10**9,X[i],0,0)[0]/(30000.*0.55))

pylab.figure(1)
pylab.plot(X,Y1,linewidth=6.0)
pylab.plot(X,Y2,linewidth=6.0)
pylab.plot(X,Y3,linewidth=6.0)
pylab.plot(X,Y4,linewidth=6.0)
pylab.plot(X,Y5,linewidth=6.0)
pylab.title('Modelos de Contacto rueda-riel vs fuga')
pylab.xlabel('Fuga')
pylab.ylabel('Relacion Carga vs Maxima Carga Tangencial')
pylab.legend (("carter","kalkerL","kalkerS","shen","polanch"))
pylab.ylim(0, 1.1)
pylab.savefig('Fig1.png')
#pylab.show()

#Tiempo de Computo
n=50
T1=np.array(np.arange(0,float(n)))
T2=np.array(np.arange(0,float(n)))
T3=np.array(np.arange(0,float(n)))
T4=np.array(np.arange(0,float(n)))
T5=np.array(np.arange(0,float(n)))
for i in range(1,n+1):
	tic=time.time() 
	for j in range(1,i):
		F=carter(30000.,0.0002,0.0001,0.25,0.55,300.*10**9,0.01,0,0)
	toc=time.time()
	T1[i-1]=toc-tic
	tic=time.time()
	for j in range(1,i):
		F=kalkerL(30000.,0.0002,0.0001,0.25,0.55,300.*10**9,0.01,0,0)
	toc=time.time()
	T2[i-1]=toc-tic
	tic=time.time()
	for j in range(1,i):
		F=kalkerS(30000.,0.0002,0.0001,0.25,0.55,300.*10**9,0.01,0,0)
	toc=time.time()
	T3[i-1]=toc-tic
	tic=time.time()
	for j in range(1,i):
		F=shen(30000.,0.0002,0.0001,0.25,0.55,300.*10**9,0.01,0,0)
	toc=time.time()
	T4[i-1]=toc-tic
	tic=time.time()
	for j in range(1,i):
		F=polanch(30000.,0.0002,0.0001,0.25,0.55,300.*10**9,0.01,0,0)
	toc=time.time()
	T5[i-1]=toc-tic

pylab.figure(2)
pylab.plot(np.arange(1,n+1),T1,linewidth=6.0)
pylab.plot(np.arange(1,n+1),T2,linewidth=6.0)
pylab.plot(np.arange(1,n+1),T3,linewidth=6.0)
pylab.plot(np.arange(1,n+1),T4,linewidth=6.0)
pylab.plot(np.arange(1,n+1),T5,linewidth=6.0)
pylab.title('Tiempo de computo entre modelos de contacto rueda-riel')
pylab.xlabel('Iteraciones')
pylab.ylabel('Tiempo (s)')
pylab.legend (("carter","kalkerL","kalkerS","shen","polanch"))
pylab.savefig('Fig2.png')

pylab.figure(3)
pylab.plot(np.arange(1,n+1),T1,linewidth=6.0)
pylab.plot(np.arange(1,n+1),T2,linewidth=6.0)
pylab.plot(np.arange(1,n+1),T4,linewidth=6.0)
pylab.plot(np.arange(1,n+1),T5,linewidth=6.0)
pylab.title('Tiempo de computo entre modelos de contacto rueda-riel')
pylab.xlabel('Iteraciones')
pylab.ylabel('Tiempo (s)')
pylab.legend (("carter","kalkerL","shen","polanch"))
pylab.savefig('Fig3.png')


pylab.show()

np.savetxt("ResultadosB.csv", np.transpose((X,Y1,Y2,Y3,Y4,Y5)), delimiter=',')
np.savetxt("ResultadosA.csv", np.transpose((np.arange(1,n+1),T1,T2,T3,T4,T5)), delimiter=',')

