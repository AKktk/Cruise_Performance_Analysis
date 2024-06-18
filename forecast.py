# script consisting function for time-series forecasting

import pandas as pd
import numpy as np
from statsmodels.tsa.statespace.sarimax import SARIMAX
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import itertools
import warnings
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import r2_score


def sarimax_forecast(data, kpi, seasonality = 12):
    # Decide the label for the time series
    y = data[kpi]
    X = data.drop(columns=[kpi])

    # split data into train and test sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.15, shuffle=False)

    # Scaling the features
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    # Define the p, d, q, P, D, Q, m parameter ranges
    p = d = q = range(0, 2)
    P = D = Q = range(0, 2)
    m = [seasonality]  # Seasonality is set to 12 for monthly data  

    # Generate all different combinations of p, d, q triplets and seasonal triplets
    pdq = list(itertools.product(p, d, q))
    seasonal_pdq = list(itertools.product(P, D, Q, m))  
    
    # Perform grid search
    best_aic = np.inf
    best_params = None
    warnings.filterwarnings("ignore")

    for param in pdq:
        for seasonal_param in seasonal_pdq:
            try:
                model = SARIMAX(y_train,
                                order=param,
                                seasonal_order=seasonal_param,
                                exog=X_train_scaled)
                results = model.fit(disp=False)

                if results.aic < best_aic:
                    best_aic = results.aic
                    best_params = (param, seasonal_param)

                print(f'SARIMA{param}x{seasonal_param} - AIC:{results.aic}')
            except Exception as e:
                continue

    print(f'Best SARIMA{best_params[0]}x{best_params[1]} - AIC:{best_aic}')

    # Train the best model
    best_model = SARIMAX(y_train, order=best_params[0], seasonal_order=best_params[1], exog=X_train_scaled)
    best_result = best_model.fit()

    # Forecast using the best model
    sarima_forecast = best_result.get_forecast(steps=len(X_test), exog=X_test_scaled)
    sarima_forecast_mean = sarima_forecast.predicted_mean
    sarima_conf_int = sarima_forecast.conf_int()

    # calculate RMSE
    rmse = np.sqrt(np.mean((sarima_forecast_mean - y_test) ** 2))
    print('RMSE: ', rmse)
    
    # r2 score
    r2 = r2_score(y_test, sarima_forecast_mean)
    print('R2 Score: ', r2)

    # plot forecast
    # Plot the forecast
    plt.figure(figsize=(14, 7))
    plt.plot(y_test.index, y_test, label='Actual Data', marker='o', linestyle='-', color='blue')
    plt.plot(y_test.index, sarima_forecast_mean, label='SARIMA Forecast', color='orange')
    plt.fill_between(y_test.index,
                     sarima_conf_int.iloc[:, 0],
                     sarima_conf_int.iloc[:, 1], color='green', alpha=0.3)
    plt.title('SARIMA Forecast')
    plt.legend()
    plt.show()

# function for forecasting with best parameters
def best_forecast(data, kpi, param, seasonal_param):
    # Decide the label for the time series
    y = data[kpi]
    X = data.drop(columns=[kpi])

    # split data into train and test sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.15, shuffle=False)

    # Scaling the features
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    # Train the SARIMA model
    sarima_model = SARIMAX(y_train, order= param, seasonal_order=seasonal_param, exog=X_train_scaled)
    sarima_result = sarima_model.fit()
    #monthly: sarima_results = sarima_model.fit()

    # Forecast
    sarima_forecast = sarima_result.get_forecast(steps=len(X_test), exog=X_test_scaled)
    sarima_forecast_mean = sarima_forecast.predicted_mean
    sarima_conf_int = sarima_forecast.conf_int()

    # calculate RMSE
    rmse = np.sqrt(np.mean((sarima_forecast_mean - y_test) ** 2))
    print('RMSE: ', rmse)
    # r2 score
    r2 = r2_score(y_test, sarima_forecast_mean)
    print('R2 Score: ', r2)

    # plot forecast
    # Plot the forecast
    plt.figure(figsize=(10, 6))
    plt.plot(y_test.index, y_test, label='Actual Data', marker='o', linestyle='-', color='blue')
    plt.plot(y_test.index, sarima_forecast_mean, label='SARIMA Forecast', color='orange')
    plt.fill_between(y_test.index,
                     sarima_conf_int.iloc[:, 0],
                     sarima_conf_int.iloc[:, 1], color='pink', alpha=0.3)
    plt.title('SARIMA Best Forecast')
    plt.legend()
    plt.show()