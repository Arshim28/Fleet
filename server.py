import numpy as np
import pandas as pd
import flwr as fl
from sklearn.metrics import r2_score
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split

import warnings
warnings.filterwarnings("ignore")

def set_initial_parameters(model, num_features):
    num_outputs=1
    model.coef_=np.zeroes((num_features, ))

def fit_round(server_round: int):
    return {"server_round": server_round}

def set_model_params(model, params):
    """Sets the parameters of a sklean LogisticRegression model."""
    model.coef_ = params
    return model

def get_evaluate_fn(model):

    driver_df=pd.read_csv("driver.csv")
    x_cols=['AGE', 'NUMBER_OF_TRIPS', 'REWARD_POINTS', 'MILES_IN_URBAN', 'CORNERING', 'SPEEDING', 'SEATBELT', 'DISTRACTION']
    y_col="SAFETY_SCORE"

    scaler=MinMaxScaler()
    driver_df[x_cols]=scaler.fit_transform(driver_df[x_cols])

    X_df=driver_df[x_cols]
    Y_df=driver_df[y_col]/100

    X_train, X_test, Y_train, Y_test=train_test_split(X_df, Y_df, test_size=0.3)

    driver_linear_model=LinearRegression()
    driver_linear_model.fit(X_df, Y_df)

    """Return an evaluation function for server-side evaluation."""

    

    # The `evaluate` function will be called after every round
    def evaluate(server_round, parameters, config):
        
        # Update model with the latest parameters
        set_model_params(model, parameters)
        loss = r2_score(Y_test, model.predict(X_test))
        accuracy = model.score(X_test, Y_test)
        return loss, {"accuracy": accuracy}

    return evaluate

if __name__=="__main__":
    model=LinearRegression()
    set_initial_parameters(model, 8)
    strategy = fl.server.strategy.FedAvg(
        min_available_clients=2,
        evaluate_fn=get_evaluate_fn(model),
        on_fit_config_fn=fit_round
    )
    fl.server.start_server(
        server_address="0.0.0.0:8080",
        strategy=strategy,
        config=fl.server.ServerConfig(num_rounds=5),
    )

