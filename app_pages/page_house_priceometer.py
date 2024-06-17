import streamlit as st
import pandas as pd
from src.data_management import load_house_sale_price_data, load_inherited_housing_data, load_pkl_file
from src.machine_learning.predictive_analysis_ui import predict_house_sale_price, predict_sale_price_inherited
from transformers import Drop_Cols_Transformer, Create_TotalLivArea_Transformer


def page_priceometer_body():

    # load predict house sale prices files
    version = 'v1'

    hsp_pipeline = load_pkl_file(
        f'outputs/ml_pipeline/predict_sale_price/{version}/predict_house_sales_pipeline.pkl')

    hsp_features = (pd.read_csv(
        f"outputs/ml_pipeline/predict_sale_price/{version}/X_train.csv").columns.to_list())

    st.write("---")

    st.write("### Business Requirements")
    st.info(
        f"*  The client is interested in predicting the house sale price from her four inherited houses "
        f"and any other house in Ames, Iowa."
    )

    st.write("---")

    # generate Live Data
    st.write("### House Priceometer")
    st.write("")

    # check_variables_for_UI(tenure_features, churn_features, cluster_features)
    X_live = DrawInputsWidgets()

    # predict on live data
    st.text("")
    if st.button("Run Predictive Analysis"):
        sale_price_prediction = predict_house_sale_price(X_live, hsp_features, hsp_pipeline)

    if st.checkbox("Data entry help information"):
        st.warning(
            f"#### Above Ground Living Area \n"
            f"* Above grade (ground) living area square feet, exlcuding basement and "
            f"any external buildings, such as a garage\n"
            f"#### Total Basement Area \n"
            f"* Total square feet of basement area (habitable or not) \n"
            f"#### Kitchen Quality \n"
            f"* Rates the material and finish of the kitchen \n"
            f"* 5: Excellent; 4: Good; 3: Typical/Average; 2: Fair; 1: Poor \n"
            f"#### Overall Quality \n"
            f"* Rates the overall material and finish of the house \n"
            f"* 10: Very Excellent; 9: Excellent; 8: Very Good; 7: Good;"
            f"6: Above Average; 5: Average; 4: Below Average; 3: Fair; 2: Poor; 1: Very Poor \n"
            f"#### Year house was built \n"
            f"* Original construction date - ranging from 1872 - 2010"
        )

    st.write("---")

    # calculate inherited house prices
    # load inherited houses dataset
    df_inherited = load_inherited_housing_data()

    # display inherited house data
    if st.checkbox("Review inherited house data"):
        st.write(
            f"* The dataset has {df_inherited.shape[0]} rows and {df_inherited.shape[1]} columns, "
            f"find below details of 4 houses."
            )

        property_index = [f'Inherited property {i}' for i in range(1, len(df_inherited) + 1)]
        df_inherited.index = property_index

        st.write(df_inherited.head(4))

        if st.button("Run house sale prediciton for the inherited houses"):
            predict_sale_price_inherited(df_inherited, hsp_features, hsp_pipeline)


def DrawInputsWidgets():
    """
    Creates the inputs for user to input values of most important variables
    """

    # load dataset
    df = load_house_sale_price_data()

    # we create input widgets only for 5 features
    col1, col2 = st.beta_columns(2)
    col3, col4 = st.beta_columns(2)
    col5, col6 = st.beta_columns(2)

    # create an empty DataFrame, which will be the live data
    X_live = pd.DataFrame([], index=[0])

    # from here on we draw the widget and set initial values
    with col1:
        feature = "GrLivArea"
        st_widget = st.number_input(
            label="Above Ground Living Area",
            min_value=df[feature].min(),
            max_value=df[feature].max(),
            value=int(df[feature].median())
        )
    X_live[feature] = st_widget

    with col2:
        feature = "TotalBsmtSF"
        st_widget = st.number_input(
            label="Total Basement Area",
            min_value=df[feature].min(),
            max_value=df[feature].max(),
            value=int(df[feature].median())
        )
    X_live[feature] = st_widget

    with col3:
        feature = "KitchenQual"
        st_widget = st.number_input(
            label="Kitchen Quality",
            min_value=1,
            max_value=5,
            value=int(df[feature].median())
        )
    X_live[feature] = st_widget

    with col4:
        feature = "OverallQual"
        st_widget = st.number_input(
            label="Overall Quality",
            min_value=1,
            max_value=10,
            value=int(df[feature].median())
        )
    X_live[feature] = st_widget

    with col5:
        feature = "YearBuilt"
        st_widget = st.number_input(
            label="Year house was built",
            min_value=df[feature].min(),
            max_value=df[feature].max(),
            value=int(df[feature].median())
        )
    X_live[feature] = st_widget

    return X_live
