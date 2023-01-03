import random
import math
import csv


class Model:

# instance variables
    def __init__(self):
        self.allNodes = []
        self.customers = []
        self.matrix = []
        self.capacity = -1

    def BuildModel(self):
        random.seed(1)

        self.capacity = 200
        totalCustomers = 100
        with open('Instance.txt', 'r') as f:
            reader = csv.reader(f)
            amr_csv = list(reader)
            for i in amr_csv:
                id = int(i[0])
                x = int(i[1])
                y = int(i[2])
                dem = int(i[3])
                unloading_time = int(i[4])
                cust = Node(id, x, y, dem, unloading_time)
                self.allNodes.append(cust)
                self.customers.append(cust)
        f.close()
        

        rows = len(self.allNodes)
        self.matrix = [[0.0 for x in range(rows)] for y in range(rows)]

        for i in range(0, len(self.allNodes)):
            for j in range(0, len(self.allNodes)):
                a = self.allNodes[i]
                b = self.allNodes[j]
                dist = math.sqrt(math.pow(a.x - b.x, 2) + math.pow(a.y - b.y, 2))
                self.matrix[i][j] = dist

class Node:
    def __init__(self, idd, xx, yy, dem, unloading_time):
        self.x = xx
        self.y = yy
        self.ID = idd
        self.demand = dem
        self.unloading_time = unloading_time
        self.isRouted = False

class Route:
    def __init__(self, dp, cap):
        self.sequenceOfNodes = []
        self.sequenceOfNodes.append(dp)
        self.sequenceOfNodes.append(dp)
        self.cost = 0
        self.capacity = cap
        self.load = 0