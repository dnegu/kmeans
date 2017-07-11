import numpy as np
import random
import math

dataset = np.genfromtxt('Iris.csv', delimiter=',')
num_cluster = 3
cluster = [[],[],[]]
size_data = len(dataset)
datos = 150*[None]
centroides = [random.randint(0, 149),random.randint(0, 149),random.randint(0, 149)]

def distancia(i,j):
	return math.sqrt(math.pow(dataset[i][0]-dataset[j][0],2)+math.pow(dataset[i][1]-dataset[j][1],2)+math.pow(dataset[i][2]-dataset[j][2],2)+math.pow(dataset[i][3]-dataset[j][3],2))

def actualizar_centroide():
	for i in range(len(cluster)):
		for j in range(len(dataset)):
			print j
	return True

def esta_convergiendo():
	return False

def main():
	converge = True	
	while(converge):
		centroides = actualizar_centroide()
		converge = esta_convergiendo()
main()
	

