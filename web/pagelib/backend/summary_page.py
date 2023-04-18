'''
page: summarization
Author: Lai
Create Date: 2023.4.16
'''
import streamlit as st
import datetime


from pagelib.backend._analysis_page import (
    _fetch_foodorder_data
)
from pagelib.backend._summary_page import (
    _fetch_order_data,
    _get_range_orders,
    _get_range_dishes,
    _get_range_turnover,
    _process_turnover_analysis,
    _get_best_selling_dish
)


def summary_page():
    st.title('General Sales Summary')
    st.text(f'You are logging as: {st.session_state["RestaurantName"]}')

    # General metrics
    st.subheader("Overall statistics")

    foodorder = _fetch_foodorder_data()
    order = _fetch_order_data()


    col1, col2, col3 = st.columns(3)
    # calculate these numbers
    
    # NOTE:
    # here, we use a fixed range for demonstration.
    # this is because our data is update to now(), we manually set two time range for comparison.
    start_time1 = datetime.datetime(year=2023, month=3, day=15) - datetime.timedelta(days=7)
    end_time1 = datetime.datetime(year=2023, month=3, day=15)
    start_time2 = datetime.datetime(year=2023, month=3, day=15) - datetime.timedelta(days=13)
    end_time2 = datetime.datetime(year=2023, month=3, day=15) - datetime.timedelta(days=7)

    # col1
    order_thisweek = _get_range_orders(order, start_time1, end_time1)
    order_lastweek = _get_range_orders(order, start_time2, end_time2)
    order_change = ((order_thisweek-order_lastweek)/order_lastweek*100)
    col1.metric("Orders", f"{order_thisweek}", f"{order_change:.2f}% compared to last week")

    # col2
    dishes_thisweek = _get_range_dishes(foodorder, start_time1, end_time1)
    dishes_lastweek = _get_range_dishes(foodorder, start_time2, end_time2)
    dishes_change = ((dishes_thisweek-dishes_lastweek)/dishes_lastweek*100)
    col2.metric("Dishes", f"{dishes_thisweek}", f"{dishes_change:.2f}% compared to last week")

    # col3
    to_thisweek = _get_range_turnover(foodorder, start_time1, end_time1)
    to_lastweek = _get_range_turnover(foodorder, start_time2, end_time2)
    to_change = ((to_thisweek-to_lastweek)/to_lastweek*100)
    col3.metric("Turnover", f"￥ {to_thisweek}", f"{to_change:.2f}% compared to last week")

    st.text('')
    st.subheader("Sales trend")

    turnover = _process_turnover_analysis(foodorder)
    st.line_chart(turnover)

    st.text('')
    st.subheader("Best selling dish")

    bestselling = _get_best_selling_dish(foodorder)
    st.dataframe(bestselling, use_container_width=True)


    # st.text('')
    # st.subheader("Inventory statistics")

    # st.text('Under construction...')

