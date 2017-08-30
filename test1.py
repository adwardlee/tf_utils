import numpy as np
from scipy.spatial.distance import cdist, squareform, pdist

Z = np.array(([0.141876578331, 0.505939126015, 0.260887920856, 0.0300328638405],[0.278316497803,0.687233030796,0.487134724855,0.0802232772112],[0.573730945587, 0.383623540401, 0.29230093956, 0.132815793157]))

dists = squareform(pdist(Z, 'sqeuclidean'))
median_dist = np.median(dists)
sigma = np.sqrt(0.5 * median_dist)
gamma = 0.5 / (sigma ** 2)