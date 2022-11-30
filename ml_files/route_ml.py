import pandas as pd
import numpy as np
from sklearn.metrics import explained_variance_score
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import MinMaxScaler

route_df=pd.read_csv("route.csv")
x_cols=['RAIN', 'TEMP', 'PRESSURE', 'WIND_SPEED', 'WIND_DIRECTION']
y_col="AVG_RISK_SCORE"

scaler=MinMaxScaler()
route_df[x_cols]=scaler.fit_transform(route_df[x_cols])

X_df=route_df[x_cols]
Y_df=route_df[y_col]/100

route_linear_model=LinearRegression()
route_linear_model.fit(X_df, Y_df)

Y_pred=route_linear_model.predict(X_df)*100

print(explained_variance_score(route_df[y_col], Y_pred))
