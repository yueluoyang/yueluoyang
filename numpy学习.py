import numpy
a = numpy.array([1,2,3])  
print (a)

b = numpy.array([[1,  2],  [3,  4]])  
print (b)

c = numpy.array([1, 2, 3, 4, 5], ndmin =  3)  
print (c)

d = b.reshape((1,4))
print(d)

e = b.reshape((4,1))
print(e)

d[0] = 9
print(d)
e[1] = 8
e[2] = 7
print(e)