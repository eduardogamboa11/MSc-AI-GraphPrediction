from matplotlib import pyplot as pl
import numpy
import math


average1,average2,average3 = -10, 0, 10
standard_deviation1,standard_deviation2,standard_deviation3 = 4.25, 0.5, 4.25
p1,p2,p3 = 1, 2, 1
q1,q2,q3 = 0, 0, 0

x = [i/10 for i in range(-100,101)]
numbers = [i for i in range(200)]

gaussian1 = [math.exp(-(((x[i]-average1)**2)/(2*(standard_deviation1**2)))) for i in numbers]
gaussian2 = [math.exp(-(((x[i]-average2)**2)/(2*(standard_deviation2**2)))) for i in numbers]
gaussian3 = [math.exp(-(((x[i]-average3)**2)/(2*(standard_deviation3**2)))) for i in numbers]

sp1 = [gaussian1[i]*((p1*x[i])+q1) for i in numbers]
sp2 = [gaussian2[i]*((p2*x[i])+q2) for i in numbers]
sp3 = [gaussian3[i]*((p3*x[i])+q3) for i in numbers]

a = [sp1[i] + sp2[i] + sp3[i] for i in numbers]
b = [gaussian1[i] + gaussian2[i] + gaussian3[i] for i in numbers]
y = [a[i]/b[i] for i in numbers]

pl.plot(x, 'blue',y, 'red')
pl.show()
