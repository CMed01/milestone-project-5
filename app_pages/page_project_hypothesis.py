import streamlit as st


def page_project_hypothesis_body():
    """Function that displays the content for the hypothesis page"""

    st.write("### Project Hypothesis and Validation")

    # conclusions taken from "02 - SalePrice study" notebook
    st.success(
        f"We suspect key house attributes such as above ground living area, number of bedrooms, "
        f"and overall quality rating have a strong positive correlation with the sale price.\n\n"
        f"The Sale Price correlation study supports that. \n\n"
    )
