X=0:0.001:0.01;
Y1=X;
Y2=X;
Y3=X;
for i=1:length(X)
	Y1(i)=carter(30000,0.0002,0.0001,0.25,0.55,300*10^9,X(i),0,0);
	[FX,FY]=kalkerL(30000,0.0002,0.0001,0.25,0.55,300*10^9,X(i),0,0);
	Y2(i)=FX;
	[FX,FY]=kalkerS(30000,0.0002,0.0001,0.25,0.55,300*10^9,X(i),0,0);
	Y3(i)=FX;
	i
end
plot(X,Y1,X,Y2,X,Y3);