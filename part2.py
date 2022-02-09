import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score

data = pd.read_excel('part2.xlsx')


data=data[["customer_id","age","txn_description","balance","amount"]]

salary=data[data["txn_description"]=="PAY/SALARY"].groupby("customer_id").mean().reset_index()
salary=salary[["customer_id","amount"]]
salary=salary.rename(columns = {'amount':'salary'})

pos=data[data["txn_description"]==("POS"or"SALES-POS")].groupby("customer_id").mean().reset_index()
pos=pos[["customer_id","amount"]]
pos=pos.rename(columns = {'amount':'pos'})

payment=data[data["txn_description"]=="PAYMENT"].groupby("customer_id").mean().reset_index()
payment=payment[["customer_id","amount"]]
payment=payment.rename(columns = {'amount':'payment'})

customer=data.groupby("customer_id").mean().reset_index()
customer=customer[["customer_id","age","balance"]]
print(customer.head())

df=pd.merge(customer, payment, on="customer_id")
df=pd.merge(df, pos, on="customer_id")
df=pd.merge(df, salary, on="customer_id")

print (df.head())

X=df[["age","balance","payment","pos"]].values
y=df["salary"].values
X_train, X_test, y_train, y_test = train_test_split( X, y, test_size=0.2, random_state=42)
lr = LinearRegression()
lr.fit(X_train, y_train)
lr.score(X, y)
y_pred=lr.predict(X_test)

print('Coefficient of determination: ', r2_score(y_test, y_pred))
print("The model predicts salary will be=")
print(lr.predict([[60,5000,100,50]])[0])


dt = DecisionTreeRegressor()
dt.fit(X_train, y_train)
dt.score(X_train, y_train)
dt.predict(X_test)
dt.score(X_test, y_test)
print("The model predicts salary will be=")
print(dt.predict([[60,5000,100,50]])[0])