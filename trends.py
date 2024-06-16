# Function to resample the data to a new time step
def resample(data):
    import pandas as pd
    # Convert the 'Start time' column to a datetime object
    data['Start Time'] = pd.to_datetime(data['Start Time'])

    # Set 'Start time' as the index
    data.set_index('Start Time', inplace=True)

    # Resample the data
    hourly_df = data.resample('H').mean()
    daily_df = data.resample('D').mean()
    weekly_df = data.resample('W').mean()
    monthly_df = data.resample('M').mean()

    return hourly_df, daily_df, weekly_df, monthly_df