import pandas as pd
from sklearn.preprocessing import MinMaxScaler

# Imprt sklzarn.preprocesing standardScaler 

def get_normalised_data(data):
    """
    Normalises the data values using MinMaxScaler from sklearn
    :param data: a DataFrame with columns as ['ndex','Open','Close','Volume']
    :return: a DataFrame with normalised value for all the columns expect index
    """

    # Initialize a scaler, then apply it to the features.
    scaler = MinMaxScaler()
    numercial = ['Open','Close','Volume']
    data[numercial] = scaler.fit_transform(data[numercial])
    return data

def remove_data(data):
    """
    Remove column from the data
    : param data: a record of all the stock pirces with columns as ['Date', 'Open', 'High', 'Low', 'Close', 'Volume']
    : Return: a DataFrame with columns as ['index', 'Open', 'Close', 'Volume']

    """
    # Define through the stock data objects backwards and store factors we want to keep:
    item = []
    open = []
    close = []
    volume = []
    
    # Loop through the stock data objects backwards and store factors we want to keep
    i_counter = 0

    for i in range(len(data) - 1, -1,-1):
        item.append(i_counter)
        open.append(data['Open'][i])
        close.append(data['Close'][i])
        volume.append(data['Volume'][i])
        i_counter += 1

    # Create a data frame for stock data
    