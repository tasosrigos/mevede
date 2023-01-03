#from TSP_Model import Model

from Solver import Solver
from VRP_Model import Model

m = Model()
m.BuildModel()
s = Solver(m)
sol = s.solve()

