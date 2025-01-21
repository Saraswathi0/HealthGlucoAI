# -*- coding: utf-8 -*-
"""diabetes

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/19Zr-Kc3-nR3etDVw1j4K8SZJlPuklReh
"""

import pandas as pd

r=pd.read_csv("diabetes.csv")

#r.head(5)

#r.isnull().sum()

#r.shape

#r.describe()

x=r.drop('Outcome',axis=1)
y=r['Outcome']
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
x_train = scaler.fit_transform(x_train)
x_test = scaler.transform(x_test)

from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier

model1=LogisticRegression()
model2=SVC()
model3=RandomForestClassifier()
model4=DecisionTreeClassifier()

model1.fit(x_train,y_train)

model2.fit(x_train,y_train)

model3.fit(x_train,y_train)

model4.fit(x_train,y_train)

y_pred1=model1.predict(x_test)
y_pred2=model2.predict(x_test)
y_pred3=model3.predict(x_test)
y_pred4=model4.predict(x_test)

from sklearn.metrics import f1_score,accuracy_score

m1=f1_score(y_test,y_pred1)
m2=f1_score(y_test,y_pred2)
m3=f1_score(y_test,y_pred3)
m4=f1_score(y_test,y_pred4)

a1=accuracy_score(y_test,y_pred1)
a2=accuracy_score(y_test,y_pred2)
a3=accuracy_score(y_test,y_pred3)
a4=accuracy_score(y_test,y_pred4)

#print(a2*100)
#print(a3*100)
#print(a4*100)

#print(m1*100)
#print(m2*100)
#print(m3*100)
#print(m4*100)

import matplotlib.pyplot as plt

plt.figure(figsize=(8,6))
plt.bar(['LogisticRegression','SVC','RandomForestClassifier','DecisionTreeClassifier'],[m1*100,m2*100,m3*100,m4*100])
plt.xlabel("model")
plt.ylabel("accuracy")
plt.title("accuracy comparsion")
plt.show()

plt.scatter(x['Age'],y)
plt.show()

from sklearn.model_selection import cross_val_score

score1=cross_val_score(model1,x,y,cv=5,scoring='accuracy')
score2=cross_val_score(model2,x,y,cv=5,scoring='accuracy')
score3=cross_val_score(model3,x,y,cv=5,scoring='accuracy')
score4=cross_val_score(model4,x,y,cv=5,scoring='accuracy')

#print(score1.mean()*100)
#print(score2.mean()*100)
#print(score3.mean()*100)
#print(score4.mean()*100)

import streamlit as st

st.title("HealthGlucoAI")
st.write("This app will help you to find if your have diabetes or not")

name = st.text_input("Enter your name:")
age=st.number_input("Enter your age:")
gender = st.selectbox("Select your gender:", ["Male", "Female", "Other"])
Pregnancies=st.number_input("Enter your Pregnancies:")
Glucose=st.number_input("Enter your Glucose:")
BloodPressure=st.number_input("Enter your BloodPressure:")
SkinThickness=st.number_input("Enter your SkinThickness:")
Insulin=st.number_input("Enter your Insulin:")
BMI=st.number_input("Enter your BMI:")
DiabetesPedigreeFunction=st.number_input("Enter your DiabetesPedigreeFunction:")

if st.button("predict"):
    data=[[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,age]]
    data = scaler.transform(data)
    final_solution=model3.predict(data)
    if final_solution==1:
        st.write(name)
        st.write(gender)
        st.write("you are suffering from diabetes")
    else:
        st.write(name)
        st.write(gender)
        st.write("you are not suffering from diabetes")
