import streamlit as st
from app_pages.multipage import MultiPage

# load pages scripts
from app_pages.page_project_summary import page_summary_body
from app_pages.page_sale_price_study import page_sale_price_study_body
from app_pages.page_house_priceometer import page_priceometer_body
from app_pages.page_project_hypothesis import page_project_hypothesis_body
from app_pages.page_technical import page_technical_body

app = MultiPage(app_name= "House Priceometer") # Create an instance of the app 

# Add your app pages here using .add_page()
app.add_page("Quick Project Summary", page_summary_body)
app.add_page("House Sale Price Study", page_sale_price_study_body)
app.add_page("Sale Priceometerr", page_priceometer_body)
app.add_page("Project Hypothesis and Validation", page_project_hypothesis_body)
app.add_page("ML: Predict House Sale Price", page_technical_body)

app.run() # Run the  app