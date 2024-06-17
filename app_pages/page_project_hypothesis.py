import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import ppscore as pps
from src.data_management import load_house_sale_price_data
from src.machine_learning.evaluate import heatmap_corr, heatmap_pps, DisplayCorrAndPPS


def page_project_hypothesis_body():
    """Function that displays the content for the hypothesis page"""

    # load data
    df_sp = load_house_sale_price_data()

    # create TotalLivArea
    df_sp['TotalLivArea'] = df_sp['GrLivArea'] + df_sp['TotalBsmtSF']

    # apply correlation and PPS
    df_corr_spearman = df_sp.corr(method="spearman")
    df_corr_pearson = df_sp.corr(method="pearson")

    pps_matrix_raw = pps.matrix(df_sp)
    pps_matrix = pps_matrix_raw.filter(['x', 'y', 'ppscore']).pivot(
        columns='x', index='y', values='ppscore')

    st.write("### Project Hypothesis and Validation")

    # conclusions taken from "02 - SalePrice study" notebook
    st.success(
        f"We suspect key house attributes such as above ground "
        f"living area, number of bedrooms, and overall quality rating have "
        f"a strong positive correlation with the sale price.\n\n"
        f"The Sale Price correlation study supports this hypothesis. \n\n"
    )

    if st.checkbox("Display Correlation plots"):
        st.warning(
            f'* We note from the correlation anaylsis, that good values'
            f' were reported for a large number of variables, therefore we '
            f'have amended the displayed correlation threshold to >0.6  \n'
            f'* In the following Correlation plots and Predictive Power '
            f'Score plot we can see highly correlated variables '
            f'to SalePrice. \n'
            f'* We demonstrate that three features have predicitve powers '
            f'> 0.2 for SalePrice '
            )
        DisplayCorrAndPPS(
            df_corr_pearson=df_corr_pearson,
            df_corr_spearman=df_corr_spearman,
            pps_matrix=pps_matrix,
            CorrThreshold=0.6,
            PPS_Threshold=0.2,
            figsize=(12, 10),
            font_annot=10
            )
