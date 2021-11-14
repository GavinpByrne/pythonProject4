#Distrubution Random Walks
import numpy as np
import matplotlib.pyplot as plt
np.random.seed(123)
find_tails=[]
for x in range (1000):
    tails=[0]
    for x in range (10):
        coin=np.random.randint(0,2)
        tails.append(tails[x]+coin)
        find_tails.append(tails[-1])
print(find_tails)
plt.hist(find_tails,bins=10,label='Test_plot',color='orange')
plt.show()
#np.mean(find_tails<30)
