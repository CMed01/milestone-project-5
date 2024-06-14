import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from src.data_management import load_house_sale_price_data, load_pkl_file
from src.machine_learning.evaluate import regression_evaluation, regression_performance


def page_technical_body():

    # load tenure pipeline files
    version = 'v1'

    hsp_pipeline = load_pkl_file(
        f'outputs/ml_pipeline/predict_sale_price/{version}/predict_house_sales_pipeline.pkl')
    hsp_features = (
        pd.read_csv(f"outputs/ml_pipeline/predict_sale_price/{version}/X_train.csv").columns.to_list())
    feature_importance_plots = plt.imread(
        f"outputs/ml_pipeline/predict_sale_price/{version}/features_importance.png")
    evaluation_plots = plt.imread(
        f"outputs/ml_pipeline/predict_sale_price/{version}/regression_evaluation.png")
    X_train = pd.read_csv(
        f"outputs/ml_pipeline/predict_sale_price/{version}/X_train.csv")
    X_test = pd.read_csv(
        f"outputs/ml_pipeline/predict_sale_price/{version}/X_test.csv")
    y_train = pd.read_csv(
        f"outputs/ml_pipeline/predict_sale_price/{version}/y_train.csv")
    y_test = pd.read_csv(
        f"outputs/ml_pipeline/predict_sale_price/{version}/y_test.csv")

    st.write("### ML Pipeline: Predict House Sale Price")

    # display pipeline training summary conclusions
    st.info(
        f"* We aimed to develop an ML model to predict house sale price, based on house attributes."
        f"The model was considered a success if: \n"
        f"* At least 0.75 for R2 score, on train and test set. \n"
        f"* Both the train and tests after cleaning data and applying feature engineering "
        f" achieved an R2 score > 0.75 (0.886, 0.797) \n"
        f"* The R2 value in the test set compared to the train set was lower, " 
        f"but deemed within acceptable ranges. \n"
        f"* There may be a suggestion that the model has overfitted in the train set "
        f"and futher exploration may be warrented in the future to improves the "
        f"models performance on unseen data. \n"
    )

    st.write("---")

    # show pipeline steps
    st.write("* ML pipeline to predict sale price.")
    st.write(hsp_pipeline)
    st.write("---")

    # show feature importance
    st.write(f"* The features the model was trained and their importance.\n")
    st.write(X_train.columns.to_list())
    st.write(
        f"* Note following the application of the pipeline, the model was "
        f"trained on a new feature 'TotalLivArea' - which is a combination of "
        f"'GrLivArea' and 'TotalBsmtSF'.\n"
        f"* 'TotalLivArea' had a higher correlation to sale price - "
        f"see the 'House Price Sale Study Page'.\n"
        )
    st.image(feature_importance_plots)
    st.write("---")

    # evaluate performance on both sets
    st.write("### Pipeline Performance")

    regression_performance(X_train, y_train, X_test, y_test, hsp_pipeline)

    # show pipeline performance plot
    st.image(evaluation_plots)
    