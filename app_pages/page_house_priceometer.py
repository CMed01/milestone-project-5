import streamlit as st
import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin
from src.data_management import load_house_sale_price_data, load_pkl_file
from src.machine_learning.predictive_analysis_ui import Create_TotalLivArea_Transformer, Drop_Cols_Transformer
from src.machine_learning.predictive_analysis_ui import (predict_house_sale_price)


def page_priceometer_body():

     # load predict house sale prices files
    version = 'v1'
    hsp_pipeline = load_pkl_file(
        f'outputs/ml_pipeline/predict_sale_price/{version}/predict_house_sales_pipeline.pkl')
    hsp_features = (pd.read_csv(f"outputs/ml_pipeline/predict_sale_price/{version}/X_train.csv")
                      .columns
                      .to_list()
                      )

    st.write("---")

    # Generate Live Data
    # check_variables_for_UI(tenure_features, churn_features, cluster_features)
    X_live = DrawInputsWidgets()
