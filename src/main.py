from sklearn.datasets import load_boston
import pandas as pd
import warnings
import seaborn as sns
import matplotlib.pyplot as plt
from .eda import boston_info

with warnings.catch_warnings():
    warnings.filterwarnings("ignore")

    boston_dataset = load_boston()

# data: contains the information for various houses
# target: prices of the house
# feature_names: names of the features
# DESCR: describes the dataset


boston_df = pd.DataFrame(boston_dataset.data, columns=boston_dataset.feature_names)
boston_df["MEDV"] = boston_dataset.target
############## EDA (Exploratory data analysis) ################
# extracting the dataset description in a txt file.
boston_info(boston_dataset.DESCR)
fig = sns.pairplot(boston_df)
fig.savefig("distribution.png")
correlation_matrix = boston_df.corr().round(2)
# annot = True to print the values inside the square
plt.figure(figsize=(16, 9))
fig_heatmap = sns.heatmap(data=correlation_matrix, annot=True)
plt.savefig("correlation.png")
