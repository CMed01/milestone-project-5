import streamlit as st


def page_summary_body():
    """Function that displays the content for the summary page"""

    st.write("### Quick Project Summary")

    # Text based on README file - "Dataset Content" section
    st.info(
        f"**Project Dataset**\n"
        f"The dataset has almost 1.5 thousand rows and represents house sale"
        f"price data for properties in Ames, Iowa. "
        f"Data details properties and their features "
        f"(Floor Area, Basement, Garage, Kitchen, Lot, Porch, Wood Deck, "
        f"Year Built) and its respective sale price for houses "
        f"built between 1872 and 2010."
        )

    # Link to README file, users can access full project documentation
    st.write(
        f"* For additional information, please visit and **read** the "
        f"[Project README file](https://github.com/"
        f"CMed01/milestone-project-5).")

    # Copied from README file - "Business Requirements" section
    st.success(
        f"The project has 2 business requirements:\n"
        f"* 1 - The client is interested in discovering how the house "
        f"attributes correlate with the sale price. "
        f"Therefore, the client expects data visualisations "
        f"of the correlated variables against the sale price to show that.\n"
        f"* 2 - The client is interested in predicting the house sale price "
        f"from her four inherited houses and any other house in Ames, Iowa."
        )
