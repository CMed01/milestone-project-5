import matplotlib.pyplot as plt
import numpy as np
import ppscore as pps
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


def heatmap_corr(df, threshold, figsize=(20, 12), font_annot=8):
    """ To display correlation heatmaps """
    if len(df.columns) > 1:
        mask = np.zeros_like(df, dtype=np.bool)
        mask[np.triu_indices_from(mask)] = True
        mask[abs(df) < threshold] = True

        fig, axes = plt.subplots(figsize=figsize)
        sns.heatmap(df, annot=True, xticklabels=True, yticklabels=True,
                    mask=mask, cmap='plasma',
                    annot_kws={"size": font_annot}, ax=axes,
                    linewidth=0.5
                    )
        axes.set_yticklabels(df.columns, rotation=0)
        plt.ylim(len(df.columns), 0)
        st.pyplot(fig)


def heatmap_pps(df, threshold, figsize=(20, 12), font_annot=8):
    """ To display PPS heatmap """
    if len(df.columns) > 1:
        mask = np.zeros_like(df, dtype=np.bool)
        mask[abs(df) < threshold] = True
        fig, ax = plt.subplots(figsize=figsize)
        ax = sns.heatmap(df, annot=True, xticklabels=True, yticklabels=True,
                         mask=mask, cmap='rocket_r',
                         annot_kws={"size": font_annot},
                         linewidth=0.05, linecolor='grey')
        plt.ylim(len(df.columns), 0)
        st.pyplot(fig)


def DisplayCorrAndPPS(df_corr_pearson, df_corr_spearman,
                      pps_matrix, CorrThreshold, PPS_Threshold,
                      figsize=(20, 12), font_annot=8):
    """ To display correlation and PPS heatmaps """
    st.write("\n")
    
    st.write("*** Heatmap: Spearman Correlation ***")
    heatmap_corr(df=df_corr_spearman, threshold=CorrThreshold,
                 figsize=figsize, font_annot=font_annot)

    st.write("\n")
    st.write("*** Heatmap: Pearson Correlation ***")
    heatmap_corr(df=df_corr_pearson, threshold=CorrThreshold,
                 figsize=figsize, font_annot=font_annot)

    st.write("\n")
    st.write("*** Heatmap: Power Predictive Score (PPS) ***")
    st.write(
      f'PPS threshold set to >0.2'
      f"The score ranges from 0 (no predictive power) to 1 (perfect "
      f"predictive power) \n")
    heatmap_pps(df=pps_matrix, threshold=PPS_Threshold, figsize=figsize,
                font_annot=font_annot)
