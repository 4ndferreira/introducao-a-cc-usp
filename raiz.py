import math

a=float(input("digite o valor de a:"))
b=float(input("digite o valor de b:"))
c=float(input("digite o valor de c:"))

delta=(b**2)-(4*a*c)

if delta<0:
	print("esta equação não possui raízes reais")
else:
	raiz1=(-b+math.sqrt(delta))/(2*a)
	raiz2=(-b-math.sqrt(delta))/(2*a)
	if delta==0:
		print("a raiz desta equação é",raiz1)
	else:
		raizes=[raiz1,raiz2]
		raizes.sort()
		print("as raízes da equação são ",end="")
		print(*(raizes),sep=" e ")