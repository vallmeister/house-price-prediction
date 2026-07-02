from sklearn.base import BaseEstimator, TransformerMixin


class MissingImputer(BaseEstimator, TransformerMixin):

    def __init__(self, columns, fill_value="None"):
        self.columns = columns
        self.fill_value = fill_value

    def transform(self, X):
        X = X.copy()
        for col in self.columns:
            X[col] = X[col].fillna(self.fill_value)
        return X

    def fit(self, X, y=None):
        return self


class ColumnDropper(BaseEstimator, TransformerMixin):

    def __init__(self, columns):
        self.columns = columns

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        X = X.copy()
        return X.drop(columns=self.columns, errors="ignore")


class RowDropper(BaseEstimator, TransformerMixin):

    def __init__(self, columns):
        self.columns = columns

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        X = X.copy()
        return X.dropna(subset=self.columns)
