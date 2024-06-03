import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import streamlit as st
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error


def regression_performance(X_train, y_train, X_test, y_test,pipeline):
  """
  # Gets train/test sets and pipeline and evaluates the performance
  - for each set (train and test) call regression_evaluation()
  which will evaluate the pipeline performance
  """

  st.write("Model Evaluation \n")
  st.write("* Train Set")
  regression_evaluation(X_train,y_train,pipeline)
  st.write("* Test Set")
  regression_evaluation(X_test,y_test,pipeline)



def regression_evaluation(X,y,pipeline):
  """
  # Gets features and target (either from train or test set) and pipeline
  - it predicts using the pipeline and the features
  - calculates performance metrics comparing the prediction to the target
  """
  prediction = pipeline.predict(X)
  st.write('R2 Score:', r2_score(y, prediction).round(3))
  st.write('Mean Absolute Error:', mean_absolute_error(y, prediction).round(3))
  st.write('Mean Squared Error:', mean_squared_error(y, prediction).round(3))
  st.write('Root Mean Squared Error:', np.sqrt(mean_squared_error(y, prediction)).round(3))
  st.write("\n")
