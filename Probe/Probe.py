#!/usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt

def Roll(size, n):
    rolls = np.random.randint(1, size+1, n)
    while len(rolls[(rolls%size)==0]) != 0:
        newrolls = np.random.randint(1, size+1, len(rolls[(rolls%size)==0]))
        positions = np.where(rolls%size==0)
        np.add.at(rolls,positions,newrolls)
    
    return rolls

def PrintRoll(roll1, roll2, threshhold, bonus=0):
    rolls=roll1+roll2+bonus
    N=len(rolls)
    print(len(rolls[rolls>=threshhold])/N)

N = 400000

w4=Roll(4,N)
w6=Roll(6,N)
w8=Roll(8,N)
w10=Roll(10,N)
w12=Roll(12,N)

w42=Roll(4,N)
w62=Roll(6,N)
w82=Roll(8,N)
w102=Roll(10,N)
w122=Roll(12,N)

# PrintRoll(w12, w122, 20,1)

# PrintRoll(w10, w62, 8)
# PrintRoll(w10, w62, 9)
# PrintRoll(w10, w62, 10)
# PrintRoll(w10, w62, 11)
biden10 = w10+w102
mittelBiden10 = np.sum(biden10)/N
abweichBiden10 = np.sqrt(1/(N-1)*np.sum((biden10-mittelBiden10)**2))
mittelAxt6 = np.sum(w6+w42)/N
mittelAxt8 = np.sum(w8+w42)/N
mittelAxt10 = np.sum(w10+w42)/N
mittelAxt12 = np.sum(w12+w42)/N
mittelSchwert6 = np.sum(w6+2)/N
mittelSchwert8 = np.sum(w8+2)/N
mittelSchwert10 = np.sum(w10+2)/N
mittelSchwert12 = np.sum(w12+2)/N
print('Axt mit W6 = {0:.2f} +/- {1:.2f}'.format(mittelAxt6, np.sqrt(1/(N-1)*np.sum((w6+w42-mittelAxt6)**2))))
print('Axt mit W8 = {0:.2f} +/- {1:.2f}'.format(mittelAxt8, np.sqrt(1/(N-1)*np.sum((w6+w42-mittelAxt8)**2))))
print('Axt mit W10 = {0:.2f} +/- {1:.2f}'.format(mittelAxt10, np.sqrt(1/(N-1)*np.sum((w6+w42-mittelAxt10)**2))))
print('Axt mit W12 = {0:.2f} +/- {1:.2f}'.format(mittelAxt12, np.sqrt(1/(N-1)*np.sum((w6+w42-mittelAxt12)**2))))
print('Schwert mit W6 = {0:.2f} +/- {1:.2f}'.format(mittelSchwert6, np.sqrt(1/(N-1)*np.sum((w6+2-mittelSchwert6)**2))))
print('Schwert mit W8 = {0:.2f} +/- {1:.2f}'.format(mittelSchwert8, np.sqrt(1/(N-1)*np.sum((w6+2-mittelSchwert8)**2))))
print('Schwert mit W10 = {0:.2f} +/- {1:.2f}'.format(mittelSchwert10, np.sqrt(1/(N-1)*np.sum((w6+2-mittelSchwert10)**2))))
print('Schwert mit W12 = {0:.2f} +/- {1:.2f}'.format(mittelSchwert12, np.sqrt(1/(N-1)*np.sum((w6+2-mittelSchwert12)**2))))
print('Bidenhänder mit W10 = {0:.2f} +/- {1:.2f}'.format(mittelBiden10, abweichBiden10))
print('')

# print(np.sum(Roll(8,N))/N)
# print(np.sum(Roll(6,N)+Roll(6,N)+Roll(6,N))/N)
# print(np.sum(Roll(6,N)+Roll(6,N)+Roll(6,N)+Roll(6,N)+Roll(6,N))/N)
# print(np.sum(Roll(10,N)+Roll(6,N))/N)
# PrintRoll(w4, w42, 9)
# PrintRoll(w6, w42, 9)
# PrintRoll(w8, w42, 9)
# PrintRoll(w10, w42, 9)
# print('')
# PrintRoll(w4, w62, 9)
# PrintRoll(w6, w62, 9)
# PrintRoll(w8, w62, 9)
# PrintRoll(w10, w62, 9)
# PrintRoll(w12, w122, 9, 1)

fig, axs = plt.subplots(2, 2)

# axs[0,0].hist(w4+w42,density=True, bins=np.arange(40)-0.5)
# axs[1,0].hist(w6+w42,density=True, bins=np.arange(40)-0.5)
# axs[0,1].hist(w8+w42,density=True, bins=np.arange(40)-0.5)
# axs[1,1].hist(w10+w82,density=True, bins=np.arange(40)-0.5)

axs[0,0].hist(w6+w42,density=True, bins=np.arange(35)-0.5)
axs[0,0].hist(w6+2,density=True, bins=np.arange(35)-0.5, alpha=0.5)
axs[0,1].hist(w8+w42,density=True, bins=np.arange(35)-0.5)
axs[0,1].hist(w8+2,density=True, bins=np.arange(35)-0.5, alpha=0.5)
axs[1,0].hist(w10+w42,density=True, bins=np.arange(35)-0.5)
axs[1,0].hist(w10+2,density=True, bins=np.arange(35)-0.5, alpha=0.5)
axs[1,0].hist(biden10,density=True, bins=np.arange(35)-0.5, alpha=0.5)
axs[1,1].hist(w12+w42,density=True, bins=np.arange(35)-0.5)
axs[1,1].hist(w12+2,density=True, bins=np.arange(35)-0.5, alpha=0.5)
# axs[1,0].hist(w6,density=True, bins=np.arange(30)-0.5)
# axs[0,1].hist(w8+w42,density=True, bins=np.arange(30)-0.5)
# axs[1,1].hist(w10,density=True, bins=np.arange(30)-0.5)
# axs[0,1].hist(w6+w62,density=True, bins=np.arange(30)-0.5)

plt.show()
