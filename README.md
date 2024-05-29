# ![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

## Template Instructions

Welcome,

This is the Code Institute student template for the Heritage Housing project option in Predictive Analytics. We have preinstalled all of the tools you need to get started. It's perfectly ok to use this template as the basis for your project submissions. Click the `Use this template` button above to get started.

You can safely delete the Template Instructions section of this README.md file,  and modify the remaining paragraphs for your own project. Please do read the Template Instructions at least once, though! It contains some important information about the IDE and the extensions we use.

## How to use this repo

1. Use this template to create your GitHub project repo

2. Log into the cloud-based IDE with your GitHub account.

3. On your Dashboard, click on the Create button

4. Paste in the URL you copied from GitHub earlier

5. Click Create

6. Wait for the workspace to open. This can take a few minutes.

7. Open a new terminal and `pip3 install -r requirements.txt`

11. Open the jupyter_notebooks directory and click on the notebook you want to open.

12. Click the kernel button and choose Python Environments.

Note that the kernel says Python 3.8.18 as it inherits from the workspace so it will be Python-3.8.18 as installed by our template. To confirm this you can use `! python --version` in a notebook code cell.

## Cloud IDE Reminders

To log into the Heroku toolbelt CLI:

1. Log in to your Heroku account and go to *Account Settings* in the menu under your avatar.
2. Scroll down to the *API Key* and click *Reveal*
3. Copy the key
4. In your Cloud IDE, from the terminal, run `heroku_config`
5. Paste in your API key when asked

You can now use the `heroku` CLI program - try running `heroku apps` to confirm it works. This API key is unique and private to you so do not share it. If you accidentally make it public then you can create a new one with *Regenerate API Key*.

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
	- A Correlation study can help in this investigation

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


#### You may deliver an ML system that is capable of reliably predicting the summed sales price of the 4 inherited houses. You may use either conventional ML or Neural Networks to map the relationships between the features and the target. You may consider changing the ML task from Regression to Classification if you find a valid rationale for that. In case you are modelling using conventional ML, with packages like scikit-learn for example, you may conduct an extensive hyperparameter optimization for a given algorithm. You can refer back to the Scikit-learn lesson, Unit Notebook 6: Cross-Validation Search Part 2. At the end of the notebook, you will find a list of hyperparameter options and values to start with, for the family of algorithms we covered in the course.


## ML Business Case

* In the previous bullet, you potentially visualised an ML task to answer a business requirement. You should frame the business case using the method we covered in the course.


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
    
__- Train data - filter data where Churn == 1, then drop the Churn variable. Target: tenure; features: all other variables, but total charges and customerID__

__It is assumed that this model will predict a sale price if the Predict Churn Classifier predicts 1 (yes for churn). If the prospect is online, the prospect will have already provided the input data via a form. If the prospect talks to a salesperson, the salesperson will interview to gather the input data and feed it into the App. The prediction is made on the fly (not in batches).__


### Cluster Analysis
#### Clustering Model
- We want an ML model to cluster similar houses. It is an unsupervised model.
- Our ideal outcome is to provide our client with reliable insight into maximising sale prices for their inherited properties.
- The model success metrics are
	- at least 0.45 for the average silhouette score
	- The ML model is considered a failure if the model suggests from more than 15 clusters (might become too difficult to interpret in practical terms)
- The output is defined as an additional column appended to the dataset. This column represents the cluster's suggestions. It is a categorical and nominal variable represented by numbers starting at 0.
- Heuristics: Currently, there is no approach to grouping similar sale prices
- The training data to fit the model comes from public records. This dataset contains about 1.5 thousand customer records.
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



* List all dashboard pages and their content, either blocks of information or widgets, like buttons, checkboxes, images, or any other items that your dashboard library supports.
* Eventually, during the project development, you may revisit your dashboard plan to update a given feature (for example, at the beginning of the project you were confident you would use a given plot to display an insight but eventually you needed to use another plot type)

## Unfixed Bugs

* You will need to mention unfixed bugs and why they were not fixed. This section should include shortcomings of the frameworks or technologies used. Although time can be a big variable to consider, paucity of time and difficulty understanding implementation is not valid reason to leave bugs unfixed.

## Deployment

### Heroku

* The App live link is: <https://YOUR_APP_NAME.herokuapp.com/>
* Set the runtime.txt Python version to a [Heroku-20](https://devcenter.heroku.com/articles/python-support#supported-runtimes) stack currently supported version.
* The project was deployed to Heroku using the following steps.

1. Log in to Heroku and create an App
2. At the Deploy tab, select GitHub as the deployment method.
3. Select your repository name and click Search. Once it is found, click Connect.
4. Select the branch you want to deploy, then click Deploy Branch.
5. The deployment process should happen smoothly if all deployment files are fully functional. Click the button Open App on the top of the page to access your App.
6. If the slug size is too large then add large files not required for the app to the .slugignore file.

## Main Data Analysis and Machine Learning Libraries

* Here you should list the libraries you used in the project and provide example(s) of how you used these libraries.

## Credits

* In this section, you need to reference where you got your content, media and extra help from. It is common practice to use code from other repositories and tutorials, however, it is important to be very specific about these sources to avoid plagiarism.
* You can break the credits section up into Content and Media, depending on what you have included in your project.

### Content

* The text for the Home page was taken from Wikipedia Article A
* Instructions on how to implement form validation on the Sign-Up page was taken from [Specific YouTube Tutorial](https://www.youtube.com/)
* The icons in the footer were taken from [Font Awesome](https://fontawesome.com/)

### Media

* The photos used on the home and sign-up page are from This Open Source site
* The images used for the gallery page were taken from this other open-source site

## Acknowledgements (optional)


* In case you would like to thank the people that provided support through this project.

