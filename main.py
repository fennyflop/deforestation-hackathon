import csv
from pylab import *

country = input().capitalize()

file = open("annual-deforestation.csv")
csvreader = csv.reader(file)

header = next(csvreader)

x = []
y = []

for row in csvreader:
    if(row[0] == country):
        x.append(int(row[2]))
        y.append(int(row[3]))

file.close()

scatter(x, y)
(m, b) = polyfit(x, y, 1)

x2 = 2025
y2 = m*x2 + b
x.append(x2)
y.append(y2)

yp = polyval([m,b],x)
 
plot(x2, y2, 'ro')
plot(x, yp)
 
grid(True)
xlabel('Years')
ylabel('Deforestation')

show()