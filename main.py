import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans
import csv
dataset1=[]
with open('datos_1.csv')as file:
    count=0
    reader=csv.reader(file)
    if count>0:
        for row in reader:
            dataset1.append([row[0],row[1]])
    count=count+1
dataset1=np.array(dataset1)

kmeans = KMeans(n_clusters=5)
kmeans.fit(dataset1)

plt.scatter(dataset1[:,0], dataset1[:,1], c=kmeans.labels_, cmap='rainbow')
plt.scatter(kmeans.cluster_centers_[:,0] ,kmeans.cluster_centers_[:,1], color='black')
plt.xlim(-6,6)
plt.ylim(-6,6)