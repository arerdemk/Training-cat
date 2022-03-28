import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

x=np.log(np.e**2)


df=pd.read_csv('logedeneme.csv')

convertloge=np.log(df['gas'])
df['loge']=convertloge

normal=pd.DataFrame(df,columns=['min','gas'])
lncsv=pd.DataFrame(df,columns=['min','loge'])

min=df['min']
gas=df['gas']
loge=df['loge']


plt.subplot(1,2,1)
plt.scatter(min,gas)

plt.subplot(1,2,2)
plt.scatter(min,loge)
plt.show()








