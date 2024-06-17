# House Sale Price Data Analytic Project

The House Priceometer application can be viewed [here](https://house-priceometer-milestone-5-cf39fc0a164e.herokuapp.com/)

## Table of contents

- [Table of contents](#table-of-contents)
- [Dataset Content](#dataset-content)
- [Business Requirements](#business-requirements)
- [Hypothesis and how to validate?](#hypothesis-and-how-to-validate)
- [Business Requirments](#the-rationale-to-map-the-business-requirements-to-the-data-visualisations-and-ml-tasks)
- [ML Business Case](#ml-business-case)
- [Dashboard Design](#dashboard-design-streamlit-app-user-interface)
- [Deployment](#deployment)
- [Data Analysis and ML Libraries](#main-data-analysis-and-machine-learning-libraries)
- [Debugging](#debugging)
- [Credits](#credits)
- [Acknowledgements](#acknowledgements)



## Dataset Content

* The dataset is sourced from [Kaggle](https://www.kaggle.com/codeinstitute/housing-prices-data). We then created a fictitious user story where predictive analytics can be applied in a real project in the workplace.
* The dataset has almost 1.5 thousand rows and represents housing records from Ames, Iowa, indicating house profile (Floor Area, Basement, Garage, Kitchen, Lot, Porch, Wood Deck, Year Built) and its respective sale price for houses built between 1872 and 2010.

|Variable|Meaning|Units|
|:----|:----|:----|
|1stFlrSF|First Floor square feet|334 - 4692|
|2ndFlrSF|Second-floor square feet|0 - 2065|
|BedroomAbvGr|Bedrooms above grade (does NOT include basement bedrooms)|0 - 8|
|BsmtExposure|Refers to walkout or garden level walls|Gd: Good Exposure; Av: Average Exposure; Mn: Minimum Exposure; No: No Exposure; None: No Basement|
|BsmtFinType1|Rating of basement finished area|GLQ: Good Living Quarters; ALQ: Average Living Quarters; BLQ: Below Average Living Quarters; Rec: Average Rec Room; LwQ: Low Quality; Unf: Unfinshed; None: No Basement|
|BsmtFinSF1|Type 1 finished square feet|0 - 5644|
|BsmtUnfSF|Unfinished square feet of basement area|0 - 2336|
|TotalBsmtSF|Total square feet of basement area|0 - 6110|
|GarageArea|Size of garage in square feet|0 - 1418|
|GarageFinish|Interior finish of the garage|Fin: Finished; RFn: Rough Finished; Unf: Unfinished; None: No Garage|
|GarageYrBlt|Year garage was built|1900 - 2010|
|GrLivArea|Above grade (ground) living area square feet|334 - 5642|
|KitchenQual|Kitchen quality|Ex: Excellent; Gd: Good; TA: Typical/Average; Fa: Fair; Po: Poor|
|LotArea| Lot size in square feet|1300 - 215245|
|LotFrontage| Linear feet of street connected to property|21 - 313|
|MasVnrArea|Masonry veneer area in square feet|0 - 1600|
|EnclosedPorch|Enclosed porch area in square feet|0 - 286|
|OpenPorchSF|Open porch area in square feet|0 - 547|
|OverallCond|Rates the overall condition of the house|10: Very Excellent; 9: Excellent; 8: Very Good; 7: Good; 6: Above Average; 5: Average; 4: Below Average; 3: Fair; 2: Poor; 1: Very Poor|
|OverallQual|Rates the overall material and finish of the house|10: Very Excellent; 9: Excellent; 8: Very Good; 7: Good; 6: Above Average; 5: Average; 4: Below Average; 3: Fair; 2: Poor; 1: Very Poor|
|WoodDeckSF|Wood deck area in square feet|0 - 736|
|YearBuilt|Original construction date|1872 - 2010|
|YearRemodAdd|Remodel date (same as construction date if no remodelling or additions)|1950 - 2010|
|SalePrice|Sale Price|34900 - 755000|

## Business Requirements

As a good friend, you are requested by your friend, who has received an inheritance from a deceased great-grandfather located in Ames, Iowa, to  help in maximising the sales price for the inherited properties.

Although your friend has an excellent understanding of property prices in her own state and residential area, she fears that basing her estimates for property worth on her current knowledge might lead to inaccurate appraisals. What makes a house desirable and valuable where she comes from might not be the same in Ames, Iowa. She found a public dataset with house prices for Ames, Iowa, and will provide you with that.

* 1 - The client is interested in discovering how the house attributes correlate with the sale price. Therefore, the client expects data visualisations of the correlated variables against the sale price to show that.
* 2 - The client is interested in predicting the house sale price from her four inherited houses and any other house in Ames, Iowa.

## Hypothesis and how to validate?

- 1 - We suspect key house attributes such as above ground living area, number of bedrooms, and overall quality rating have a strong positive correlation with the sale price
	- A correlation study can help in this investigation

## The rationale to map the business requirements to the Data Visualisations and ML tasks

- **Business Requirement 1:** Data visualisation and correlation study
    - We will inspect the data related to all atributes related to house sale prices
    - We will conduct a correlation study (Pearson and Spearman) to better understand the relationship between all variable and house sale prices
    - We will plot these relationships against house sale prices

#### You may perform a correlation and/or PPS study to investigate the most relevant variables correlated to the sale price. You have to visualize these variables against the sale price, so you can summarize the insights.

- **Business Requirement 2:** Classification, Regression, Cluster and Data Analysis
    - We want to predict house sale prices and build a classifier to support this.
    - We want to predict house attributes that will improve house sale prices. We want to build a regression model or change the ML taks to classification depending on regressor performance. 
    - We want to cluster similar houses to predict from which cluster the sale price will belong
    - We want to understand a cluster profile to present modifiable options to improve future house sale prices.


## ML Business Case

1. What are the business requirements?
    - The client is interested in discovering how house attributes correlate with sale prices. Therefore, the client expects data visualizations of the correlated variables against the sale price.
    - The client is interested in predicting the house sale prices from her 4 inherited houses, and any other house in Ames, Iowa.

2. Is there any business requirement that can be answered with conventional data analysis?
    - Yes, we can use conventional data analysis to investigate how house attributes are correlated with the sale prices.

3. Does the client need a dashboard or an API endpoint?
    - The client needs a dashboard

4. What does the client consider as a successful project outcome?
    - A study showing the most relevant variables correlated to sale price.
    - Also, a capability to predict the sale price for the 4 inherited houses, as well as any other house in Ames, Iowa.
    
5. Can you break down the project into Epics and User Stories?
    - Information gathering and data collection.
    - Data visualization, cleaning, and preparation.
    - Model training, optimization and validation.
    - Dashboard planning, designing, and development.
    - Dashboard deployment and release.

6. Ethical or Privacy concerns?
    - No. The client found a public dataset.

7. Does the data suggest a particular model?
    - The data suggests a regressor where the target is the sale price.

8. What are the model's inputs and intended outputs?
    - The inputs are house attribute information and the output is the predicted sale price.

9. What are the criteria for the performance goal of the predictions?
    - We agreed with the client an R2 score of at least 0.75 on the train set as well as on the test set.

10. How will the client benefit?
    - The client will maximize the sales price for the inherited properties.


### Predict Sale Price
#### Regression Model
- We want an ML model to predict house sale price, based on house attributes. A target variable is a discrete number. We consider a **regression model**, which is supervised __and uni-dimensional (TO CONFIRM THIS).__ 
- Our ideal outcome is to provide our client with reliable insight into maximizing the sales price for their inherited properties.
- The model success metrics are
	- At least 0.75 for R2 score, on train and test set
- The ML model is considered a failure if:
	- The R2 score is < 0.75
    - If the more than 50% of the houses are sold at more than 25% less than the predicted sale price.
- The output is defined as an expected sale price based on the inputted attributes.
- Heuristics: Currently, there is no model to predict sale price in Ames, Iowa
- The training data to fit the model comes from public records. This dataset contains about 1.5 thousand house records.
	- Train data - features: all variables, .... 
    

## Dashboard Design (Streamlit App User Interface)

### Page 1: Quick project summary

A project summary page, showing the project dataset summary and the client's requirements.

### Page 2: Sale Price Study

A page listing your findings related to which features have the strongest correlation to the house sale price.

### Page 3: House Priceometer

A page displaying the 4 houses' attributes and their respective predicted sale price. It should display a message informing the summed predicted price for all 4 inherited houses. You should add interactive input widgets that allow a user to provide real-time house data to predict the sale price.

### Page 4: Project Hypothesis and Validation
A page indicating your project hypothesis(es) and how you validated it across the project.
- Before the analysis, we knew we wanted this page to describe the project hypothesis, the conclusions, and how we validated each. After the data analysis, we can report that:
- 1 - We suspect key house attributes such as above ground living area, number of bedrooms, and overall quality rating have a strong positive correlation with the sale price


### Page 5: Predict Sale Price
A technical page displaying your model performance. If you deployed an ML pipeline, you have to display your pipeline steps.


## Deployment

### Heroku

* The App live link is: [House Priceometer](https://house-priceometer-milestone-5-cf39fc0a164e.herokuapp.com/)
* Set the runtime.txt Python version to a [Heroku-20](https://devcenter.heroku.com/articles/python-support#supported-runtimes) stack currently supported version.
* The project was deployed to Heroku using the following steps.

1. Log in to Heroku and create an App
2. At the Deploy tab, select GitHub as the deployment method.
3. Select your repository name and click Search. Once it is found, click Connect.
4. Select the branch you want to deploy, then click Deploy Branch.
5. The deployment process should happen smoothly if all deployment files are fully functional. Click the button Open App on the top of the page to access your App.
6. If the slug size is too large then add large files not required for the app to the .slugignore file.

## Main Data Analysis and Machine Learning Libraries

### Applications
* [Gitpod](https://www.gitpod.io/) - Cloud based IDE used to develop code for this project
* [Github](https://github.com/) - Repository used for this project
* [Heroku](https://www.heroku.com/) - Used to deploy the website
* [Jupyter Notebooks](https://jupyter.org/) - Used to document the workflow used during this data analytic project
* [Kaggle](https://www.kaggle.com/) - Used to access the dataset used for this project
* [Streamlit](https://streamlit.io/) - Used to visualise the data in a web based application
* [CI Python Linter](https://pep8ci.herokuapp.com/) - Used to format the code meeting PEP8 standard.

### Libraries

The following libraries were used throughout this project to manipulate, analyse and trasnform the data. The data was then passed through machine learning models before being visualised through and web page application.
* [numpy](https://numpy.org/) - version 1.19.5
* [pandas](https://pandas.pydata.org/) - version 1.4.2
* [matplotlib](https://matplotlib.org/) - version 3.3.1
* [seaborn](https://seaborn.pydata.org/) - version 0.11.0
* [ydata-profiling](https://docs.profiling.ydata.ai/latest/) - version 4.4.0
* [plotly](https://plotly.com/) - version 4.12.0
* [ppscore](https://pypi.org/project/ppscore/0) - version 1.2.0
* [scikit-learn](https://scikit-learn.org/stable/) - version 0.24.2
* [feature-engine](https://feature-engine.trainindata.com/en/latest/) - version 1.0.2
* [imbalanced-learn](https://imbalanced-learn.org/stable/) - version 0.8.0
* [xgboost](https://xgboost.readthedocs.io/en/latest/index.html) - version - 1.2.1
* [yellowbrick](https://www.scikit-yb.org/en/latest/) - version 1.3


## Debugging

* Custom data transformers were required to ensure the pipeline cleaned the date effectively. Initially these custom classes were embedded in the respective Jupyter Notebooks.
    * When deploying the streamlit application the custom transformers were not imported into the web application and the error messages were observed.
    * Stack overflow was interrogated and a solution was identified.
    * The custom transformers needed to be contained within a project directory level python file (transformers.py).
    * This high level python could then be imported into both the Jupyter Notebooks and the streamlit web pages and this solved the issue allowing the successful deployment of the ML pipeline within the streamlit web app.

## Credits

* This code was based on the Code Institute Walkthrough Project 2 - Churnometer project. Code was adapated to fit the requirements of this project and referenced through the Jupyter Notebooks.
* The documentation for the libraries used supported the develeopment of this project

## Acknowledgements

* I would like to thank my mentor Princess Ijege for his support and wisdom throughout this project.
* I would like to thank the Code Institute tutor and student support team who were extremly supportive and responsive with all queries and problems I encountered during this project.
