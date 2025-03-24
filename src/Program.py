from FlatShapes import Rectangle
from VolShapes import *
import pickle
import shelve

A = Rectangle()
B = Rectangle(5,4)
print(A, B)

L = [Cylinder(), Parallelepiped(2,3,4), Cone(5,2)]
for s in L:
    print(s)

print(L)

txt = L.__str__()
copy = eval(txt)
print(copy)
F = open('datafile.pkl', 'wb')
pickle.dump(L, F)
F.close()
F = open('datafile.pkl', 'rb')
E = pickle.load(F)
F.close()
print(E)

S = shelve.open('datafile.slv')
S['C'] = L[0]
S['P'] = L[1]
S['N'] = L[2]
S.sync()
S.close()

S = shelve.open('datafile.slv')
R = [S['N'], S['P'], S['C']]
S.close()
print(R)

