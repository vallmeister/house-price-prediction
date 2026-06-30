import pandas as pd




class Preprocessor:

    def load_train_data(self):
        return pd.read_csv('../data/train.csv', index_col=0)

    def load_test_data(self):
        return pd.read_csv('../data/train.csv', index_col=0)

    def get_imputed_train_data(self):
        data = self.load_train_data()

        data["PoolQC"] = data["PoolQC"].fillna("None")

        return data