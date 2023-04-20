'''
page: data mining page processing functions
Author: Lai
Create Date: 2023.4.20
'''
import streamlit as st
import pandas as pd
import numpy as np

from utils import sql
from sklearn.linear_model import LinearRegression



def _LR_predict_selling(previous: pd.DataFrame, forecast_days=5) -> pd.DataFrame:
    X = np.arange(len(previous)).reshape(-1, 1)
    Y = previous.copy().to_numpy()

    reg = LinearRegression().fit(X,Y)
    Predict_X = np.arange(len(previous) + forecast_days).reshape(-1, 1)

    Predict_Y = reg.predict(Predict_X)

    return Predict_X, Predict_Y

@st.cache_data
def _get_support_matrix(id):
    cnx, cursor = sql.create_session_cursor()
    food = sql.execute_fetchall(cursor, 'SELECT * from food where RESTAURANT_ID=%s;', [id])
    food = pd.DataFrame(food)
    Food_num = len(food)

    Order = sql.execute_fetchall(cursor, 'SELECT * from `order` where RESTAURANT_ID=%s;', [id])
    Order = pd.DataFrame(Order)

    Order_detail = sql.execute_fetchall(cursor, 'SELECT * from `order` where RESTAURANT_ID=%s', [id])
    Order_detail = pd.DataFrame(Order_detail)

    Order_num=len(Order_detail)

    Dish_Relation= pd.DataFrame(np.zeros((Food_num, Food_num)),
                                columns=food[0], index=food[0])

    Order_detail = sql.execute_fetchall(cursor, 'SELECT * from order_details', tuple())
    Order_detail = pd.DataFrame(Order_detail)

    for i in Order[0]:
        Temp = Order_detail.loc[ Order_detail[0] == i ]
        # Temp = pd.DataFrame(Temp)
        for j in Temp[1].tolist():
            for k in Temp[1].tolist():
                Dish_Relation.loc[j, k] += 1

    cnx.close()
    return Dish_Relation / Order_num, food


def _get_combinations(Support_Matrix, id, threshold):
    idx, idy = np.where(Support_Matrix > threshold)
    combs = set()
    for i in range(len(idx)):
        if idx[i] != idy[i]:
            combs.add((min(idx[i], idy[i]), max(idx[i], idy[i])))
    print(combs)

    combs = list(combs)
    cnx, cursor = sql.create_session_cursor()
    food = sql.execute_fetchall(cursor, 'SELECT * from food where RESTAURANT_ID=%s;', [id])
    cnx.close()
    food = pd.DataFrame(food)
    food.index = food[0]
    # print(food)
    result = []
    for comb in combs:
        dishname1 = food.iloc[comb[0], 3]
        dishname2 = food.iloc[comb[1], 3]
        Support_Index = Support_Matrix.iloc[comb[0], comb[1]]
        result.append((dishname1, dishname2, Support_Index))
    return result

