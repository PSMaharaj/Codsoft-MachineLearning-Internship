import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv("spam.csv",encoding='latin-1')
df.head()
df = df.drop(['Unnamed: 2','Unnamed: 3','Unnamed: 4'],axis=1)
df = df.rename(columns={'v1':'label','v2':'Text'})
df['label_enc'] = df['label'].map({'ham':0,'spam':1})
df.head()
sns.countplot(x=df['label'])
plt.show()
avg_words_len=round(sum([len(i.split()) for i in df['Text']])/len(df['Text']))
print(avg_words_len)
s = set()
for sent in df['Text']:
    for word in sent.split():
	    s.add(word)
total_words_length=len(s)
print(total_words_length)



