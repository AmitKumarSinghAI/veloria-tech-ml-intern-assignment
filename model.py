import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import warnings
warnings.filterwarnings("ignore")

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder,StandardScaler,MinMaxScaler,LabelEncoder,OrdinalEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.compose import ColumnTransformer
from sklearn.metrics import confusion_matrix,f1_score,classification_report,accuracy_score,recall_score,precision_score
from sklearn.pipeline import Pipeline
import pickle
from sklearn.ensemble import RandomForestClassifier,BaggingClassifier
from sklearn.tree import DecisionTreeClassifier
from xgboost import XGBClassifier

# Load dataset
data = pd.read_csv("matches.csv")
print(data.sample(3))

# EXtract importance col form the dataset
data = data[['team1', 'team2', 'toss_winner', 'toss_decision', 'venue', 'city',"winner"]]

print(data.sample(5))

print(data.info())

print(data.isnull().mean() * 100)

from sklearn.impute import SimpleImputer
# filling missing values
si = SimpleImputer(strategy="most_frequent")
data[["city"]] = si.fit_transform(data[["city"]])

print(data.isnull().mean() * 100)

print(data.duplicated().sum())

# Removing the duplicate
data.drop_duplicates(inplace=True)

print(data.duplicated().sum())

print("Original Winner Distribution:")
print(data["winner"].value_counts())

# Handling the imblance class using sampling techniques
# get the largets winner size
max_size = data["winner"].value_counts().max()

# preform oversampling

balanced_data = data.groupby('winner').apply(lambda x : x.sample(max_size,replace = True)).reset_index(drop=True)
 # shuffle the dataset to avoid any order bias
data = balanced_data.sample(frac=1).reset_index(drop=True)

# check the balance winnner distribution
print("/n Balanced Wineer Distribution (after oversampling):")
print(data["winner"].value_counts())

print(data.sample(5))

data["toss_decision"].value_counts()

x = data.iloc[:,:-1]
y = data[["winner"]]

import string
pu = string.punctuation
print(pu)


# preprocessing
def preprocessing(text):
    text = text.lower()
    text = text.replace(" ","")
    return text.translate(str.maketrans("","",pu))

x["team1"] = x["team1"].apply(preprocessing)
x["team2"] = x["team2"].apply(preprocessing)
x["toss_winner"] = x["toss_winner"].apply(preprocessing)
x["city"] = x["city"].apply(preprocessing)
x["venue"] = x["venue"].apply(preprocessing)
y["winner"] = y["winner"].apply(preprocessing)

print(x.sample(10))

le = LabelEncoder()
y_encoder = le.fit_transform(y)

# spliting the data set
x_train,x_test,y_train,y_test = train_test_split(x,y_encoder,test_size=0.2,random_state=42)

trf = ColumnTransformer(transformers=[
    ("OHE",OneHotEncoder(drop="first",sparse_output=True),["team1","team2","toss_winner","toss_decision","venue","city"])
],remainder="passthrough")

x_train_trf = trf.fit_transform(x_train)
x_test_trf = trf.transform(x_test)

print(x_train_trf.shape)

print(x_test_trf.shape)

def tranning(model):
    model1 = model
    model1.fit(x_train_trf, y_train)

    y_pred = model1.predict(x_test_trf)

    print(f"accuracy score : {accuracy_score(y_test, y_pred)}")
    print(f"F1 score : {f1_score(y_test, y_pred, average='macro')}")
    print(f"recall score : {recall_score(y_test, y_pred, average='macro')}")
    print(f"precision score : {precision_score(y_test, y_pred, average='macro')}")
    print("confusion_matrix :\n", confusion_matrix(y_test, y_pred))
    print("classification_report :\n", classification_report(y_test, y_pred))

    return model1

print("LogisticRegression Model")
logist_r = tranning(LogisticRegression())
print(logist_r)

print("RandomForestClassifier model")
randomforest_c = tranning(RandomForestClassifier())
print(randomforest_c)

print("XGBClassifier model")
xgb_c = tranning(XGBClassifier())
print(xgb_c)

print("BaggingClassifier Model")
bagging_c = tranning(BaggingClassifier(estimator=DecisionTreeClassifier(),n_estimators=100,random_state=42))
print(bagging_c)

from sklearn.svm import SVC
print("SVC MOdel")
svc = tranning(SVC(kernel='rbf', C=1.0))
print(svc)

print("DecisionTreeClassifier MOdel")
decisiontree_c = tranning(DecisionTreeClassifier(max_depth=6,
    min_samples_split=10,
    min_samples_leaf=5,
    criterion="gini",
    random_state=42))
print(decisiontree_c)

# Comparing to all other model but XGBoostClassifier perform well:
with open("x_g_b_model.pkl", "wb") as file:
    pickle.dump(xgb_c, file)

new_data = pd.DataFrame([{
    "team1": "mumbaiindians",
    "team2": "chennai  superkings",
    "toss_winner": "mumbai indians",
    "toss_decision" : "field",
    "venue": "wankhedestadium",
    "city": "mumbai"
}])


new_data["team1"] = new_data["team1"].apply(preprocessing)
new_data["team2"] = new_data["team2"].apply(preprocessing)
new_data["toss_winner"] = new_data["toss_winner"].apply(preprocessing)
new_data["city"] = new_data["city"].apply(preprocessing)
new_data["venue"] =new_data["venue"].apply(preprocessing)

new_data_trf = trf.transform(new_data)

print(le.inverse_transform(xgb_c.predict(x_test_trf))[0])