# Our Model

As the data we were dealing with was randomly generated, our best bet was a straightforward Linear Regression, after all. However, we did quite a bit of exploratory data analysis, judging our data by a correlation heatmap for each of our csv files, plotting CDFs (Cumulative Density Functions) for all relevant features, and trying out fairly sophisticated models such as the Random Forest Regressor, Decision Tree Regressor, and Lasso, for our data. All of this can be seen in the Jupyter notebook "EDA_and_ML.ipynb".

Finally, post a bit of data cleaning, we implemented a simple linear regression (code in "Linear_Reg.ipynb"), and paired it with our server-client FL model to provide an end-to-end solution. The FL code was written with the module Flower, connecting two clients with the server for the purpose of this demonstration. The clients read their code from edited csv files (with columns removed), which are located in the same directories as their corresponding python scripts.

We put all of this functionality behind a basic front-end wrapper, which calls the appropriate bash scripts that run the server-client system for testing purposes.

# Testing the model

We've written a basic interactive terminal front-end, which can be run via the following steps.

1. Run the commands "chmod u+x driver.sh", "chmod u+x vehicle.sh" and "chmod u+x route.sh" from the project directory.
2. Run the file main.py via the command "python3 main.py", and follow the instructions output in the file.

The outputs on the terminal that opens up corresponds to the accuracy scores of the model. As we've implemented Federated Learning (using the module flower in Python), we do not obtain the data from the client side at all, but only the model's parameters itself. After every training round, we print the current coefficients of our linear regression as well, to see the progress. As the data is randomly generated (during testing, at least), the r2_score of our model is not very high, as can be expected.
