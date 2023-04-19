'''
page: dish data mining page
Author: Lai
Create Date: 2023.4.18
'''
import streamlit as st
import pandas as pd
import numpy as np

from utils import sql
from sklearn.linear_model import LinearRegression

from pagelib.backend._analysis_page import(
    _fetch_foodorder_data,
    _process_dish_analysis
)


def _LR_predict_selling(previous: pd.DataFrame, forecast_days=5) -> pd.DataFrame:
    X = np.arange(len(previous)).reshape(-1, 1)
    Y = previous.copy().to_numpy()

    reg = LinearRegression().fit(X,Y)
    Predict_X = np.arange(len(previous) + forecast_days).reshape(-1, 1)

    Predict_Y = reg.predict(Predict_X)

    return Predict_X, Predict_Y


def dish_data_mining_page() -> None:
    ##
    st.title("Dish Data Mining")
    
    st.subheader("Frequent Selling Groups")



    st.subheader("Dish Sale Prediction")

    # fetch data
    result = _fetch_foodorder_data()
    # process data
    result = _process_dish_analysis(result, 'D')    

    dish = st.selectbox('Select a dish to predict:', result.columns)

    alg_select = st.radio('Prediction Methods:', 
             ['Linear Regression', 'ARMA (To Be Supported Later)'])
    st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)

    
    PredictionX, PredictionY = _LR_predict_selling(result[dish])

    ans = pd.DataFrame({"Predicted": PredictionY}, index=pd.date_range(result.index[0], periods=len(result)+5))
    ans[dish] = np.concatenate([result[dish].to_numpy(), np.array([np.nan]*5)])

    st.line_chart(ans)


