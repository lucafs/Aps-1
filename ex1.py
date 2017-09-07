import scipy
from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt
import math
def Equidf(Y,t):
	O=Y[0]
	w=Y[1]
	dOdt=w
	dwdt=(gravidade*math.cos(O))/raio
	return(dOdt,dwdt)
#Parametros
raio=2
gravidade=9.8
massa=0.24
tempo=np.arange(0,10,0.01)
angulo=int(input("Qual o angulo A?"))
θ=90-angulo
x=(θ*math.pi)/180
H=[x,0]
sol=odeint(Equidf,H,tempo)
ListaO=sol[:,0]
Listaw=sol[:,1]
xlista=[]
ylista=[]
Tlista=[]
for i in range(len(ListaO)):
	T=massa*(gravidade*math.sin(ListaO[i])-Listaw[i]**2*raio)
	x=raio*math.cos(ListaO[i])
	y=-(raio*math.sin(ListaO[i]))
	xlista.append(x)
	ylista.append(y)
	Tlista.append(T)

plt.plot(xlista,ylista)
plt.title("{} graus".format(angulo))
plt.xlabel("x(m)")
plt.ylabel("y(m)")
plt.show()
plt.plot(tempo,xlista)
plt.title("{} graus".format(angulo))
plt.xlabel("tempo")
plt.ylabel("x(m)")
plt.show()

