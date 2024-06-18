# Function to pick the vessel for analysis {1,2}
def pick_vessel(df, vessel):
    dfv = df[df['Vessel Name']==vessel]
    return dfv  

# Function to impute based on time series
def impute_time_series(dfv, columns, method='linear'):
    for col in columns:
        dfv.loc[:, col] = dfv[col].interpolate(method = method)
    return dfv

# Function to drop unnecessary columns for time series forecasting
def drop_columns(data, columns):
    data = data.drop(columns=columns)
    return data