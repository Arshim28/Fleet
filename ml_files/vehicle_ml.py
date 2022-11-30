import pandas as pd
import numpy as np
from sklearn.metrics import explained_variance_score
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import MinMaxScaler

vehicle_df=pd.read_csv("vehicle.csv")
x_cols=['CAPACITY', 'BATTERY_HEALTH', 'BATTERY_VOLTAGE', 'TYRE_PRESSURE', 'FUEL_LEVEL', 'OIL_LEVEL',  'LAST_SERVICE_MILES', 'NEXT_SERVICE_MILES']
y_col="SAFETY_SCORE"

vehicle_df[x_cols[0]]=vehicle_df[x_cols[0]].replace(["STD", "XL LARGE", "LARGE"], [0, 1, 2])
vehicle_df[x_cols[1]]=vehicle_df[x_cols[1]].replace(["AVERAGE", "GOOD"], [0, 1])

scaler=MinMaxScaler()
vehicle_df[x_cols]=scaler.fit_transform(vehicle_df[x_cols])

X_df=vehicle_df[x_cols]
Y_df=vehicle_df[y_col]/100

vehicle_linear_model=LinearRegression()
vehicle_linear_model.fit(X_df, Y_df)

Y_pred=vehicle_linear_model.predict(X_df)*100

print(explained_variance_score(vehicle_df[y_col], Y_pred))
