import streamlit as st
import pandas as pd
import numpy as np
import joblib


@st.cache(suppress_st_warning=True, allow_output_mutation=True)
def load_house_sale_price_data():
    df_saleprice = pd.read_csv("outputs/datasets/collection/house_prices_records.csv")
    return df_saleprice


@st.cache(suppress_st_warning=True, allow_output_mutation=True)
def load_inherited_housing_data():
    df_inherited = pd.read_csv("outputs/datasets/collection/inherited_houses.csv")
    return df_inherited


def load_pkl_file(file_path):
    return joblib.load(filename=file_path)