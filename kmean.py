from math import sqrt, floor
import numpy as np
import scipy.spatial.distance as metric

def inicializacion(ds, k):
	n = np.shape(ds)[1]
	centroids = np.mat(np.zeros((k,n)))
	for j in range(n):
		min_j = min(ds[:,j])
		range_j = float(max(ds[:,j]) - min_j)
		centroids[:,j] = min_j + range_j * np.random.rand(k, 1)

	return centroids


def distancia_euclidea(A, B):
	return metric.euclidean(A, B)


def cluster(ds, k):
	m = np.shape(ds)[0]
	cluster_assignments = np.mat(np.zeros((m, 2)))
	cents = inicializacion(ds, k)
	cents_orig = cents.copy()

	changed = True
	num_iter = 0

	while changed:

		changed = False

		for i in range(m):
			min_dist = np.inf
			min_index = -1
			for j in range(k):

				dist_ji = distancia_euclidea(cents[j,:], ds[i,:])
				if dist_ji < min_dist:
					min_dist = dist_ji
					min_index = j
			if cluster_assignments[i, 0] != min_index: 
				changed = True
			cluster_assignments[i, :] = min_index, min_dist**2
		for cent in range(k):
			points = ds[np.nonzero(cluster_assignments[:,0].A==cent)[0]]
			cents[cent,:] = np.mean(points, axis=0)
		num_iter += 1
	return cents, cluster_assignments, num_iter, cents_orig
