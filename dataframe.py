"""code for data frame testing"""
import pandas as pd
import numpy as np

def read_data():
    """code for reading data"""
    address = "http://www-bcf.usc.edu/~gareth/ISL/Auto.csv"
    data = pd.read_csv(address, sep=",", header=0, na_values=['?'])
    data = data.dropna()
    data.replace([np.inf, -np.inf], np.nan).dropna(axis=1)
    data["horsepower"] = data["horsepower"].astype(int)
    data = data[["mpg", "horsepower", "year"]]
    return data

DATA_ORIGINAL = read_data()


def test_create_dataframe(data_frame, data=DATA_ORIGINAL):
    """ code for checking the given conditions"""
    result = True
    # Condition 1: There are at least 10 rows in the DataFrame
    if len(data_frame.index) < 10:
        result = False
        print("Length of data frame isn't enough", result)
    # Condition 2: The DataFrame contains only the columns that you specified
    elif (np.any(data.columns != data_frame.columns) and result):
        result = False
        raise ValueError("Sorry, column names are not the same")
    # Condition 3: The columns contain the correct data type
    elif (np.any(data_frame.dtypes != data.dtypes) and result):
        result = False
        print("Sorry, column data types don't match", result)
    else:
        print("Is the given data frame correct?", result)
    return result

# In case you want to test, here is a test case. Just remove the "#":
# new_data = data.rename(columns = {"mpg": "XYZ"})
# test_create_dataframe(new_data)
