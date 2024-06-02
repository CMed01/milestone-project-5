import streamlit as st
import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin

# Create custom class to create new feature 'TotalLivArea'
class Create_TotalLivArea_Transformer(BaseEstimator, TransformerMixin):
    def fit(self, X, y=None):
        return self
    
    def transform(self, X):
        X = X.copy()
        X['TotalLivArea'] = X['GrLivArea'] + X['TotalBsmtSF']
        return X


# Create custom class to drop features in data cleaning'
class Drop_Cols_Transformer(BaseEstimator, TransformerMixin):
    def __init__(self, columns):
        self.columns = columns
    
    def fit(self, X, y=None):
        return self
    
    def transform(self, X):
        return X.drop(columns=self.columns)