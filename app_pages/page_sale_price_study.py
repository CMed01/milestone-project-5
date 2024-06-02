import streamlit as st
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns
import pandas as pd
from src.data_management import load_house_sale_price_data



sns.set_style('whitegrid')

def page_sale_price_study_body():

    # load data
    df_saleprice = load_house_sale_price_data()

    # hard copied from churned customer study notebook
    vars_to_study = ['1stFlrSF','GarageArea','GarageFinish','GarageYrBlt','GrLivArea','KitchenQual','OverallQual','TotalBsmtSF','YearBuilt','YearRemodAdd']

    st.write("### House Sale Price Study")

    st.info(
        f"The client is interested in discovering how the house attributes correlate with"
        f"the sale price. Therefore, the client expects data visualisations of the correlated"
        f" variables against the sale price to show that.")

    # inspect data
    if st.checkbox("Inspect Customer Base"):
        st.write(
            f"* The dataset has {df_saleprice.shape[0]} rows and {df_saleprice.shape[1]} columns, "
            f"find below the first 10 rows.")

        st.write(df_saleprice.head(10))

    st.write("---")

    # Correlation Study Summary
    st.write(
        f"* A correlation study was conducted in the notebook to better understand how "
        f"the variables are correlated to House sale prices (SalePrice). \n"
        f"The most correlated variable are: **{vars_to_study}**"
    )

    # Text based on "02 - Churned Customer Study" notebook - "Conclusions and Next steps" section
    st.info(
        f"The correlations and plots interpretation converge.\n"
        f"* Larger floor space (GrLivArea, 1stFlrSF, GarageArea and TotalBsmtSF) " 
        f"is associated with a higher SalePrice\n"
        f"* Combined TotalLivArea, which includes above and below ground correlates " 
        f"stronger to a higher SalePrice.\n"
        f"* GrLivArea has the highest individual correlation to a higher SalePrice.\n"
        f"* Newer built properties (YearBuilt) are higher in SalePrice.\n"
        f"* Recently built garages and refurbishments (GarageYrBlt, YearRemodAdd) are associated "
        f"with a higher SalePrice\n"
        f"* Higher overall quality houses (OveralQual) are associated with a higher SalePrice\n"
        f"* Higher quality kitchens and garages also contribute (less strong correlation) to a "
        f"higher SalePrice (GarageFinish and KitchenQual)\n"
    )

    # Code copied from "02 - Churned Customer Study" notebook - "EDA on selected variables" section
    df_eda = df_saleprice.filter(vars_to_study + ['SalePrice'])

    # Individual plots per variable
    if st.checkbox("Variable per SalePrice"):
        sale_price_per_variable(df_eda)

    # Individual plots per variable
    if st.checkbox("TotalLivArea per SalePrice"):
        liv_total_area_variable(df_eda)

    
def plot_regression(df, col, target_var, alpha_scatter=0.5):
    fig, axes = plt.subplots(figsize=(8, 5))
    sns.regplot(data=df, x=col, y=target_var, scatter_kws={'alpha': alpha_scatter}, line_kws={'color': 'red'})
    plt.title(f"{col} vs {target_var}", fontsize=20, y=1.05)
    plt.xlabel(col)
    plt.ylabel(target_var)
    st.pyplot(fig)  # st.pyplot() renders image, in notebook is plt.show()


def plot_boxplot(df, col, target_var):
    fig, axes = plt.subplots(figsize=(8, 5))
    sns.boxplot(data=df, x=col, y=target_var)
    plt.title(f"{col} vs {target_var}", fontsize=20, y=1.05)
    plt.xlabel(col)
    plt.ylabel(target_var)
    st.pyplot(fig)  # st.pyplot() renders image, in notebook is plt.show()


def sale_price_per_variable(df):
    target_var = 'SalePrice'
    vars_to_study_numerical = ['1stFlrSF','GarageArea', 'GarageYrBlt', 'GrLivArea',  'TotalBsmtSF', 'YearBuilt', 'YearRemodAdd']
    vars_to_study_categorical = ['GarageFinish','KitchenQual', 'OverallQual']

    for col in vars_to_study_numerical:
        plot_regression(df, col, target_var)
        print("\n\n")

    for col in vars_to_study_categorical:
        plot_boxplot(df, col, target_var)
        print("\n\n")

def liv_total_area_variable(df):
    target_var = 'SalePrice'
    df['TotalLivArea'] = df['GrLivArea'] + df['TotalBsmtSF']
    plot_regression(df, 'TotalLivArea', target_var)