import pandas as pd
import numpy as np
from sklearn.metrics import explained_variance_score
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import MinMaxScaler

import warnings
warnings.filterwarnings("ignore")

driver_df=pd.read_csv("driver.csv")
x_cols=['AGE', 'NUMBER_OF_TRIPS', 'REWARD_POINTS', 'MILES_IN_URBAN', 'CORNERING', 'SPEEDING', 'SEATBELT', 'DISTRACTION']
y_col="SAFETY_SCORE"

scaler=MinMaxScaler()
driver_df[x_cols]=scaler.fit_transform(driver_df[x_cols])

X_df=driver_df[x_cols]
Y_df=driver_df[y_col]/100

driver_linear_model=LinearRegression()
driver_linear_model.fit(X_df, Y_df)

Y_pred=driver_linear_model.predict(X_df)*100

print(explained_variance_score(driver_df[y_col], Y_pred))
