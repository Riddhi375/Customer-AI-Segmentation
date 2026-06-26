import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib

data = pd.DataFrame({
    "age":[20,25,30,35,40,45,50,55],
    "income":[20000,25000,30000,45000,60000,70000,80000,90000],
    "orders":[1,2,3,5,6,8,10,12],
    "churn":[1,1,1,0,0,0,0,0]
})

X=data[["age","income","orders"]]
y=data["churn"]

model=RandomForestClassifier()

model.fit(X,y)

joblib.dump(model,"trained_models/churn_model.pkl")

print("Model Trained Successfully")