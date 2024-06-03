from sklearn.base import BaseEstimator, TransformerMixin


class Create_TotalLivArea_Transformer(BaseEstimator, TransformerMixin):
    """Create custom class to create new feature 'TotalLivArea'"""
    def fit(self, X, y=None):
        return self
    
    def transform(self, X):
        X = X.copy()
        X['TotalLivArea'] = X['GrLivArea'] + X['TotalBsmtSF']
        return X


class Drop_Cols_Transformer(BaseEstimator, TransformerMixin):
    """Create custom class to drop features in data cleaning""" 
    def __init__(self, columns):
        self.columns = columns
    
    def fit(self, X, y=None):
        return self
    
    def transform(self, X):
        return X.drop(columns=self.columns)
        