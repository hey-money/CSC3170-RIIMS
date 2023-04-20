'''
page: dish data mining page
Author: Lai
Create Date: 2023.4.18
'''
import streamlit as st
import pandas as pd
import numpy as np

from utils import sql
from matplotlib import pyplot as plt 
from matplotlib import ticker

plt.rcParams['font.sans-serif']=['SimHei'] 
from pagelib.backend._analysis_page import(
    _fetch_foodorder_data,
    _process_dish_analysis
)
from pagelib.backend._data_mining_page import (
    _LR_predict_selling, 
    _get_support_matrix,
    _get_combinations,
)


# @st.cache_data
def dish_data_mining_page() -> None:
    ##
    st.title("Dish Data Mining")
    
    st.subheader("Frequent Selling Groups - Support Matrix")

    Support_Matrix, food = _get_support_matrix(st.session_state['RestaurantID'])

    fig, ax = plt.subplots()
    ax.imshow(Support_Matrix, cmap='coolwarm')
    print(food[3].tolist())
    # plt.xlabel(food[3].tolist())
    # plt.ylabel(food[3].tolist())
    ax.xaxis.set_major_locator(
        ticker.LinearLocator(len(food))
    )
    ax.xaxis.set_major_formatter(
        ticker.FuncFormatter(lambda x, pos: food[3].tolist()[pos])
    )
    plt.xticks(rotation=45)

    ax.yaxis.set_major_locator(
        ticker.LinearLocator(len(food))
    )
    ax.yaxis.set_major_formatter(
        ticker.FuncFormatter(lambda x, pos: food[3].tolist()[pos])
    )
    # plt.yticks(rotation=90)
    st.pyplot(fig)

    st.subheader("Highest Support Value View")

    threshold = st.slider('Support Value Threshold', 0.4, 1., 0.6)
    combs = _get_combinations(Support_Matrix, st.session_state['RestaurantID'], threshold)
    bestgroups = list(zip(*combs))
    bestgroups = pd.DataFrame({'Dish1': bestgroups[0], 'Dish2': bestgroups[1], 'Support Value': bestgroups[2]})

    bestgroups = bestgroups.sort_values(by='Support Value', ascending=False)

    st.dataframe(bestgroups, use_container_width=True)

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


