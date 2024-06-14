import streamlit as st
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns
import pandas as pd
from src.data_management import load_house_sale_price_data


sns.set_style('whitegrid')


def page_sale_price_study_body():
    """Function that displays the content for the sale price study body"""

    # load data
    df_saleprice = load_house_sale_price_data()

    # hard copied from churned customer study notebook
    vars_to_study = [
        '1stFlrSF','GarageArea','GarageFinish','GarageYrBlt','GrLivArea','KitchenQual',
        'OverallQual','TotalBsmtSF','YearBuilt','YearRemodAdd'
        ]

    # Summary body for page
    st.write("### House Sale Price Study")

    st.info(
        f"The client is interested in discovering how the house attributes correlate with"
        f"the sale price. Therefore, the client expects data visualisations of the correlated"
        f" variables against the sale price to show that.")

    # Inspect data
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
        f"The most correlated variable (studied variables) are: **{vars_to_study}**"
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

    # Code copied from "02 - SalePrice Study" notebook - "EDA on selected variables" section
    df_eda = df_saleprice.filter(vars_to_study + ['SalePrice'])

    # Correlations of each variable to sale prirce
    if st.checkbox("Correlation of variables to SalePrice"):
        corr_spearman_eda = df_eda.corr(
            method='spearman')['SalePrice'].sort_values(key=abs, ascending=False)[1:].head(10)
        corr_pearson_eda = df_eda.corr(
            method='pearson')['SalePrice'].sort_values(key=abs, ascending=False)[1:].head(10)
        combined_corr = pd.DataFrame({
            'Pearson': corr_pearson_eda,
            'Spearman': corr_spearman_eda
            })

        st.write(
            f"The following table displays both the Pearson and Spearman correlation "
            f"scores of the studied variables and SalePrice"
            )
        st.write(combined_corr)

    # Individual plots per variable
    if st.checkbox("Variable per SalePrice"):
        st.write(
            f"The following figures display each studied variable plotted against the SalePrice" 
            )
        sale_price_per_variable(df_eda)

    # Addition of new variable
    df_eda['TotalLivArea'] = df_eda['GrLivArea'] + df_eda['TotalBsmtSF']

    # Correlation of new variable
    if st.checkbox("Correlation of variable, after new addition, to SalePrice"):
        st.write(
            f"The following table displays both the Pearson and Spearman correlation "
            f"scores of the studied variables and new 'TotalLivArea' variable "
            f"against SalePrice. \n\n"
            f"Note TotalLivArea is the sum of 'GrLivArea' and 'TotalBsmtSF'"
            )
        corr_spearman_eda_new = df_eda.corr(
            method='spearman')['SalePrice'].sort_values(key=abs, ascending=False)[1:].head(11)
        corr_pearson_eda_new = df_eda.corr(
            method='pearson')['SalePrice'].sort_values(key=abs, ascending=False)[1:].head(11)
        combined_corr = pd.DataFrame({
            'Pearson': corr_pearson_eda_new,
            'Spearman': corr_spearman_eda_new
            })
        st.write(combined_corr)

    # Individual plots per variable
    if st.checkbox("TotalLivArea per SalePrice"):
        st.write(
            f"The following figures display the new variable 'TotalLivArea' plotted against the SalePrice" 
            )
        liv_total_area_variable(df_eda)


# Code copied from "02 - SalePrice Study" notebook - "EDA on selected variables" section
def plot_regression(df, col, target_var, alpha_scatter=0.5):
    """ 
    FUnction for a regression plot on the House Sale Price data
    """
    fig, axes = plt.subplots(figsize=(8, 5))
    sns.regplot(data=df, x=col, y=target_var, scatter_kws={'alpha': alpha_scatter}, line_kws={'color': 'red'})
    plt.title(f"{col} vs {target_var}", fontsize=20, y=1.05)
    plt.xlabel(col)
    plt.ylabel(target_var)
    st.pyplot(fig)  # st.pyplot() renders image, in notebook is plt.show()


def plot_boxplot(df, col, target_var):
    """ 
    FUnction for a boxplot plot on the House Sale Price data
    """
    fig, axes = plt.subplots(figsize=(8, 5))
    sns.boxplot(data=df, x=col, y=target_var)
    plt.title(f"{col} vs {target_var}", fontsize=20, y=1.05)
    plt.xlabel(col)
    plt.ylabel(target_var)
    st.pyplot(fig)  # st.pyplot() renders image, in notebook is plt.show()


def sale_price_per_variable(df):
    """ 
    FUnction to render plot images to the terminal for:
    plot_boxplot() and plot_regression
    """
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
    """ 
    FUnction to calculate a variable detailing the total living area
    below and above ground

    Then displays a regression plot
    """
    target_var = 'SalePrice'
    plot_regression(df, 'TotalLivArea', target_var)
