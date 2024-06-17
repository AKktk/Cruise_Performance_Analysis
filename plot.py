import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
# Function to plot distribution of all features
def feature_distribution(df):
    columns_to_plot = [col for col in df.columns if col not in ['Start Time', 'End Time', 'Vessel Name']]
    
    # Create a histogram for each column
    for col in columns_to_plot:
        plt.figure(figsize=(10, 6))
        df[col].hist(bins=30, alpha=0.75, color='blue')
        plt.title(f'Distribution of {col}')
        plt.xlabel(col)
        plt.ylabel('Frequency')
        plt.grid(False)
        plt.show()



def trend_plot(hourly_data, daily_data, weekly_data, monthly_data, feature):
    # Create subplots
    fig, axs = plt.subplots(2, 2, figsize=(14, 10))

    # Filter hourly data to the first 7 days
    hourly_slice = hourly_data.loc[hourly_data.index[0] : hourly_data.index[2] + pd.Timedelta(days=1)]
    daily_slice = daily_data.loc[daily_data.index[0] : daily_data.index[4] + pd.Timedelta(days=30)]

    # Plot hourly data
    axs[0, 0].scatter(hourly_slice.index, hourly_slice[feature], s= 5, color='b')
    axs[0, 0].set_title(f'Hourly {feature} For 1 entire Day')
    axs[0, 0].set_xlabel('Time')
    axs[0, 0].set_ylabel(feature)
    axs[0, 0].tick_params(axis='x', rotation=45)

    # Plot daily data
    axs[0, 1].plot(daily_slice.index, daily_slice[feature], marker='o', linestyle='-', color='b')
    axs[0, 1].set_title(f'Daily {feature} For 30 Days')
    axs[0, 1].set_xlabel('Time')
    axs[0, 1].set_ylabel(feature)
    axs[0, 1].tick_params(axis='x', rotation=45)

    # Plot weekly data
    axs[1, 0].plot(weekly_data.index, weekly_data[feature], marker='o', linestyle='-', color='b')
    axs[1, 0].set_title(f'Weekly {feature}')
    axs[1, 0].set_xlabel('Time')
    axs[1, 0].set_ylabel(feature)

    # Plot monthly data
    axs[1, 1].plot(monthly_data.index, monthly_data[feature], marker='o', linestyle='-', color='b')
    axs[1, 1].set_title(f'Monthly {feature}')
    axs[1, 1].set_xlabel('Time')
    axs[1, 1].set_ylabel(feature)

    # Adjust layout
    plt.tight_layout()
    plt.show()

# Pairplot function for feature comparison
def pair_plot(hourly_data, daily_data, weekly_data, monthly_data, feature1, feature2):
    # Create subplots
    fig, axs = plt.subplots(2, 2, figsize=(14, 10))

    # Filter hourly data to the first 7 days
    hourly_slice = hourly_data.loc[hourly_data.index[0] : hourly_data.index[2] + pd.Timedelta(days=1)]
    daily_slice = daily_data.loc[daily_data.index[0] : daily_data.index[4] + pd.Timedelta(days=30)]

    # Plot hourly data
    axs[0, 0].scatter(hourly_slice[feature2], hourly_slice[feature1], s= 5, color='g')
    axs[0, 0].set_title(f'Hourly {feature1} vs {feature2} For 1 entire Day')
    axs[0, 0].set_xlabel(feature2)
    axs[0, 0].set_ylabel(feature1)
    axs[0, 0].tick_params(axis='x', rotation=45)

    # Plot daily data
    axs[0, 1].scatter(daily_slice[feature2], daily_slice[feature1], s= 5, color='g')
    axs[0, 1].set_title(f'Daily {feature1} vs {feature2} For 30 Days')
    axs[0, 1].set_xlabel(feature2)
    axs[0, 1].set_ylabel(feature1)
    axs[0, 1].tick_params(axis='x', rotation=45)

    # Plot weekly data
    axs[1, 0].scatter(weekly_data[feature2], weekly_data[feature1], s= 5, color='g')
    axs[1, 0].set_title(f'Weekly {feature1} vs {feature2}')
    axs[1, 0].set_xlabel(feature2)
    axs[1, 0].set_ylabel(feature1)

    # Plot monthly data
    axs[1, 1].scatter(monthly_data[feature2], monthly_data[feature1], s= 5, color='g')
    axs[1, 1].set_title(f'Monthly {feature1} vs {feature2}')
    axs[1, 1].set_xlabel(feature2)
    axs[1, 1].set_ylabel(feature1)

    # Adjust layout
    plt.tight_layout()
    plt.show()

# Function to plot a contour plot
# def contour_plot(daily_data):
#     # Create a contour plot
#     # Extract latitude and longitude data
#     latitudes = daily_data['Latitude (Degrees)']
#     longitudes = daily_data['Longitude (Degrees)']

#     # Create a grid of latitude and longitude values
#     lat_grid, lon_grid = np.meshgrid(np.linspace(latitudes.min(), latitudes.max(), 100),
#                                      np.linspace(longitudes.min(), longitudes.max(), 100))

#     # Interpolate the data to create a contour plot
#     # values = np.sqrt((lat_grid - latitudes.mean())**2 + (lon_grid - longitudes.mean())**2)
#     values = np.linspace(daily_data['Propulsion Power (MW)'].min(), daily_data['Propulsion Power (MW)'].max(), 100)

#     # Create the contour plot
#     plt.figure(figsize=(10, 6))
#     contour = plt.contourf(lon_grid, lat_grid, values, cmap='viridis')
#     plt.colorbar(contour)
#     plt.title('Contour Plot of Latitude and Longitude')
#     plt.xlabel('Longitude')
#     plt.ylabel('Latitude')
#     plt.show()