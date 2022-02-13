print("Slope(m),", m)
print("y-intercept (b), ", b)

yp = polyval([m,b],x)
x2 = 2020
y2 = m*x2 + b
 
plot(x2, y2, 'ro')
plot(x, yp)