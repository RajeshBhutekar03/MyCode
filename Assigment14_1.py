import pandas as pd  #example of training to the test set for the diabetes dataset
from pandas import read_csv
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier

url='PlayPredictor.csv'
df=pd.read_csv(url)
r=df.head()
print(r)


X = df[['Whether','Temperature']]
y = df['Play']

print(X)
print(y)


hist = y.hist(bins=10)

sns.heatmap(df.corr())


#Split the dataset

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 0)




# define model
model=KNeighborsClassifier(n_neighbors=1)

# fit model
model.fit(X_train, y_train)


# make predictions
yhat = model.predict(X_test)