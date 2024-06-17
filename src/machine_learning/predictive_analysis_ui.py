import streamlit as st
from transformers import Drop_Cols_Transformer, Create_TotalLivArea_Transformer


def predict_house_sale_price(X_live, hsp_features, hsp_pipeline):
    """
    Function that takes in a dataframe, custom features and pipeline
    variable

    Execution of function displaye the predicted house price based on
    on the values for selected features
    """

    # from live data, subset features related to this pipeline
    X_live_hsp = X_live[hsp_features]

    # predict
    hsp_prediction = hsp_pipeline.predict(X_live_hsp)

    st.write(f"### The predicted sale price for this property is:")
    hsp_prediction = int(hsp_prediction)
    st.write(f"### ${hsp_prediction}")


def predict_sale_price_inherited(df, hsp_features, hsp_pipeline):
    """
    Function that takes in a dataframe, custom features and pipeline
    variable

    Execution of function displays the predicted house prices of the
    inherited house dataset
    """

    # from inherited data, subset features related to this pipeline
    df_inherited = df[hsp_features]

    # Predict inherited house sale priced
    hsp_inherited_prediction = hsp_pipeline.predict(df_inherited)
    total_sale = 0

    for i, prediction in enumerate(hsp_inherited_prediction, start=1):
        inherited_sale_price = int(prediction)
        total_sale += inherited_sale_price
        st.write(
            f"* The predicted sale price of **Inherited property {i}** "
            f"= ${inherited_sale_price}"
            )

    st.write(
            f"* The total sale price of **All properties** = ${total_sale}"
            )
