import streamlit as st
from src.machine_learning.custom_transformers import Drop_Cols_Transformer, Create_TotalLivArea_Transformer

def predict_house_sale_price(X_live, house_sale_features, hsp_pipeline):

    # from live data, subset features related to this pipeline
    X_live_hsp = X_live.filter(house_sale_features)

    # predict
    hsp_prediction = hsp_pipeline.predict(X_live_hsp)
    
    st.write(hsp_prediction)

    return hsp_prediction

def predict_sale_price_inherited(X_live, house_features, hsp_pipeline):
    return