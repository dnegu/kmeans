from math import sqrt, floor
import numpy as np
import scipy.spatial.distance as euclidea

def inicializacion(ds, k):
	n = np.shape(ds)[1]
	centroides = np.mat(np.zeros((k,n)))
	for j in range(n):
		min_j = min(ds[:,j])
		range_j = float(max(ds[:,j]) - min_j)
		centroides[:,j] = min_j + range_j * np.random.rand(k, 1)

	return centroides


def distancia_euclidea(A, B):
	return euclidea.euclidean(A, B)


def kmeans(ds, k):
	matriz = np.shape(ds)[0]
	clase_cluster = np.mat(np.zeros((matriz, 2)))
	centroides = inicializacion(ds, k)
	centroides_orig = centroides.copy()

	changed = True
	num_iter = 0

	while changed:

		changed = False

		for i in range(matriz):
			min_dist = np.inf
			min_index = -1
			for j in range(k):

				dist_ji = distancia_euclidea(centroides[j,:], ds[i,:])
				if dist_ji < min_dist:
					min_dist = dist_ji
					min_index = j
			if clase_cluster[i, 0] != min_index: 
				changed = True
			clase_cluster[i, :] = min_index, min_dist**2
		for cent in range(k):
			points = ds[np.nonzero(clase_cluster[:,0].A==cent)[0]]
			centroides[cent,:] = np.mean(points, axis=0)
		num_iter += 1
	return centroides, clase_cluster, num_iter, centroides_orig

iris_data = np.genfromtxt('Iris.csv', delimiter=',')
centroides, clase_cluster, iteraciones, orig_centroides = kmeans(iris_data, 3)

print centroides
print iteraciones
