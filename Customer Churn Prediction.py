from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix, roc_curve, auc
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
import warnings
warnings.filterwarnings("ignore")
df=pd.read_csv('customer_data.csv')
print("top 5:\n",df.head())
print("bottom 5 :\n",df.tail())
print(df.info())
print("The three unique countries are : ",df["Geography"].unique())
plt.figure(figsize = (10,5))
plt.pie(df['Gender'].value_counts().values,labels=['Male','Female'],autopct='%.f%%',explode = [0,0.1],shadow = True)
plt.show()
region = df.Geography.value_counts().to_frame().reset_index()
region.columns = ['Country','Count']
plt.figure(figsize = (5,5))
ax=sns.barplot(x = region['Country'],y = region['Count'],palette='GnBu')
for i in ax.containers:
    ax.bar_label(i,)
df.drop(columns=['RowNumber','CustomerId','Surname'],inplace=True)
print(df.head())
