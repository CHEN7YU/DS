# https://github.com/codebasics/py/blob/master/ML/11_random_forest/11_random_forest.ipynb



%matplotlib inline
import matplotlib.pyplot as plt
import seaborn as sn
plt.figure(figsize=(10,7))
sn.heatmap(cm, annot=True)
plt.xlabel('Predicted')
plt.ylabel('Truth')