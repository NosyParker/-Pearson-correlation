import pandas
from pylab import *
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import math

G = gridspec.GridSpec(3, 3)
file = pandas.read_csv('advertising.csv')

def aver(name):
    s = 0
    aver_x = (sum(file[name]))/(len(file[name]))
    aver_y = (sum(file['Sales']))/(len(file['Sales']))
    #s = sum(file[name].values-aver_x)*(file['Sales'].values - aver_y)
    dividend = sum((aver_x - file[name])*(aver_y - file['Sales']))
    divider = math.sqrt((sum((file[name] - aver_x)**2))*(sum((file['Sales'] - aver_y)**2)))
    r = dividend/divider
    return(r)



plt.figure("Lab")
axes_1 = subplot(G[0, :])
plt.plot(file['TV'].values, file["Sales"].values, 'ro')
plt.ylabel('TV')
plt.xlim(0.00, 300.0)

axes_2 = subplot(G[1,:])
plt.plot(file['Radio'].values, file["Sales"].values, 'go')
plt.ylabel('Radio')
plt.xlim(0.00, 300.0)


axes_3 = subplot(G[2,:])
plt.plot(file['Newspaper'].values, file["Sales"].values, 'bo')
plt.ylabel('Newspaper')
plt.xlim(0.00, 300.0)

print('TV: ')
print (aver('TV'))
print('Radio: ')
print(aver('Radio'))
print('Newspaper: ')
print(aver('Newspaper'))
plt.show()
