import pandas as pd
import numpy as np

# function to compute KPIs for the dataframe
def compute_kpis(df):
    fuel_efficiency_list = []
    fuel_consumption = df['Main Engine 1 Fuel Flow Rate (kg/h)'] + df['Main Engine 2 Fuel Flow Rate (kg/h)'] + df['Main Engine 3 Fuel Flow Rate (kg/h)'] + df['Main Engine 4 Fuel Flow Rate (kg/h)']
    for index, row in df.iterrows():
        fuel_consumption = row['Main Engine 1 Fuel Flow Rate (kg/h)'] + row['Main Engine 2 Fuel Flow Rate (kg/h)'] + row['Main Engine 3 Fuel Flow Rate (kg/h)'] + row['Main Engine 4 Fuel Flow Rate (kg/h)']
        speed_through_water = abs(row['Speed Through Water (knots)'])
        if speed_through_water > 0:
            fuel_efficieny = fuel_consumption/speed_through_water
            fuel_efficieny = min(fuel_consumption, 5000)
        else:
            fuel_efficieny = 25
        fuel_efficiency_list.append(fuel_efficieny)
    
    df['Fuel Consumption per nautical mile'] = fuel_efficiency_list

    df['Total Power Consumed (MW)'] = df['Power Galley 1 (MW)'] + df['Power Galley 2 (MW)'] + df['Power Service (MW)'] + df['HVAC Chiller 1 Power (MW)'] + df['HVAC Chiller 2 Power (MW)'] + df['HVAC Chiller 3 Power (MW)'] + \
        df['Scrubber Power (MW)'] +df['Propulsion Power (MW)'] + df['Bow Thruster 1 Power (MW)'] + df['Bow Thruster 2 Power (MW)'] + df['Bow Thruster 3 Power (MW)'] + df['Stern Thruster 1 Power (MW)'] + df['Stern Thruster 2 Power (MW)']
    df['Power Specific Fuel Consumption (kg/h/(MW))'] = ((df['Boiler 1 Fuel Flow Rate (L/h)'] + df['Boiler 2 Fuel Flow Rate (L/h)'] + df['Incinerator 1 Fuel Flow Rate (L/h)'])*0.85 + \
        (df['Main Engine 1 Fuel Flow Rate (kg/h)'] + df['Main Engine 2 Fuel Flow Rate (kg/h)'] + df['Main Engine 3 Fuel Flow Rate (kg/h)'] + df['Main Engine 4 Fuel Flow Rate (kg/h)'])) / df['Total Power Consumed (MW)']
    # Similar to the very commonly used fuel efficiency or brake specific fuel consumption (BSFC). It is used to assess the efficiency of any engine that burns fuel and produces rotational power, typically internal combustion engines.
    # Assuming Fuel in Boiler and Incinerator to be Diesel and the density to be 0.85 kg/litre.

    return df

