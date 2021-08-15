import math

class KMeans:
    dataset = []
    center_pointset = []
    K = 0

    def __init__(self, dataset, center_pointset, K):
        self.dataset = dataset
        self.center_pointset = center_pointset
        self.K = K

    def euclidean_distance(self, point1, point2):
        return math.sqrt(pow(point1[0]-point2[0], 2) + pow(point1[1]-point2[1], 2))

    def set_euclidean_distance(self, set1, set2):
        if len(set1) == 0 or len(set2) == 0:
            return 1
        flag = 0
        for i in range(len(set1)):
            if self.euclidean_distance(set1[i], set2[i]) != 0:
                flag = 1
                break
        return flag

    def find_center_point(self, list):
        xsum = 0
        ysum = 0
        length = len(list)
        for data in list:
            xsum += data[0]
            ysum += data[1]
        return [xsum // length, ysum // length]

    def find_cluster_by_kmeans(self):
        kmeans_clusters = []
        count = 0
        old_center_pointset = self.center_pointset
        new_center_pointset = []
        flag = self.set_euclidean_distance(old_center_pointset, new_center_pointset)
        while count < 50 and flag != 0:
            if count != 0:
                old_center_pointset = new_center_pointset
            kmeans_clusters = [[] for _ in range(self.K)]
            for data in self.dataset:
                dist = []
                for i in range(len(old_center_pointset)):
                    distance = self.euclidean_distance(data, old_center_pointset[i])
                    dist.append(distance)
                kmeans_clusters[dist.index(min(dist))].append(data.tolist())
            count += 1
            new_center_pointset = []
            for cluster in kmeans_clusters:
                new_center_pointset.append(self.find_center_point(cluster))
            flag = self.set_euclidean_distance(old_center_pointset, new_center_pointset)
            print("更新后的中心点集：", end=" ")
            print(new_center_pointset)
        return new_center_pointset, kmeans_clusters
