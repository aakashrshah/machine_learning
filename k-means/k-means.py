from random import choice
from math import sqrt
Centroid_List = []
Cluster_List = []
Cluster_Dict = {}


def euclidean(x1,y1,x2,y2):
	return sqrt(pow((x2 - x1),2) + pow((y2 - y1),2))

def main(K,set_of_points):
	Cluster_List = [[] for _ in range(K)] #NOTE TO REMEMBER! (09/05/2017) https://stackoverflow.com/questions/8713620/appending-items-to-a-list-of-lists-in-python
	Centroid_List = [] * K
	Temp_List = []
	for i in range(0,K):
		c_x = choice(range(10))
		c_y = choice(range(10))
		Temp_List.append([c_x, c_y])
	Centroid_List = Temp_List[:]
	print("Centroid_List :", Centroid_List)
	while(True):
		MakeCluster(set_of_points, K, Cluster_List, Centroid_List, Cluster_Dict)
		Centroid_List_copy = Centroid_List[:] #Good to remember
		for idx,each in enumerate(Cluster_List):
			Mean(idx, each, Centroid_List)
		print(Centroid_List)
		if(Verify(Centroid_List,Centroid_List_copy)):
			print("Cluster List:",Cluster_List)
			break
	# print(Cluster_List)
	# print(Centroid_List)
	
def MakeCluster(set_of_points, K, Cluster_List = Cluster_List, Centroid_List = Centroid_List, Cluster_Dict = Cluster_Dict):
	Distances = []
	print(len(set_of_points))
	for i in range(len(set_of_points)):
		for j in range(len(Centroid_List)):
			dist = euclidean(set_of_points[i][0],set_of_points[i][1],Centroid_List[j][0],Centroid_List[j][1])
			Distances.append(dist)
		favorable_centroid = Distances.index(min(Distances))
		Distances = []

		Cluster_List[favorable_centroid].append(set_of_points[i])
		# if favorable_centroid not in Cluster_Dict:
		# 	Cluster_Dict[favorable_centroid] = set_of_points[i]
		# elif favorable_centroid in Cluster_Dict:
		# 	Cluster_Dict[favorable_centroid].append(set_of_points[i])
		# print(Cluster_Dict)
		print(Cluster_List)


def Mean(j, Cluster, Centroid_List = Centroid_List):
	sum_x = sum([each[0] for each in Cluster])
	sum_y = sum([each[1] for each in Cluster])
	mean_x = sum_x/len(Cluster)
	mean_y = sum_y/len(Cluster)
	Centroid_List[j] = [mean_x,mean_y]
	# Centroid_List update

def Verify(Cen_old, Cen_new):
	if Cen_old == Cen_new:
		return True
	else:
		return False

def makeData(n = 10):
	set_of_points = []
	for i in range(0,n):
		c_x = choice(range(10))
		c_y = choice(range(10))
		set_of_points.append((c_x,c_y))
	return set_of_points

if __name__ == '__main__':
	set_of_points = makeData(5)
	print(set_of_points)
	main(2,set_of_points)
