import numpy as np

#la fuincion entrega una lista de numeros aleatorios que siguen la distribucion dada.
def sample_1(N):
	return (np.random.choice(a=[-10,-5,3,9],size=N,p=[0.1,0.4,0.2,0.3]))

#la fuincion entrega una lista de numeros aleatorios que siguen una distribucion exponencial.
def sample_2(N):
	return (np.random.exponential(size=N,scale=0.5))

#genera M promedios provenientes de calcular M veces la duncion sampling_fun con N numeros. 
def get_mean(sampling_fun,N,M):
	promedios=[]
	for i in range (M):	
		promedios.append(sampling_fun(N))
	return np.array(promedios)

lista=[sample_1, sample_2]
lista2=[10,100,1000]

nombres=["sample_1_10.txt","sample_1_100.txt","sample_1_1000.txt","sample_2_10.txt","sample_2_100.txt","sample_2_1000.txt"]

a=0
for b in range (len(lista2)):
	for c in range(len(lista)):
		N=lista2[b]
		nombre=lista[c]
		np.savetxt(fname=nombres[a],X= get_mean((nombre),N,10000))
		a+=1
