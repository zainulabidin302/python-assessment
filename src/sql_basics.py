"""Assignment 1: Python Basics
"""
from pandas import DataFrame

def group_by_and_aggregate(df: DataFrame):
    """Given a pandas dataframe, group by the column 'customer_id' and
    aggregate the column 'amount' by sum. Moreover, filter the resulting
    dataframe to only include rows where the sum of 'amount' is greater
    than 100.
    
    Args:
        DataFrame: a pandas dataframe with customer_id and amount columns
    Returns:
        DataFrame: a pandas dataframe
    """
    # TODO: implement this function
    pass

def join_dataframes(df1: DataFrame, df2: DataFrame):
    """Given two pandas dataframes, join them on the column 'customer_id'.
    The resulting dataframe should remove rows for which there is no match
    on both dataframes.
    
    Args:
        df1: a pandas dataframe with customer_id and amount columns
        df2: a pandas dataframe with customer_id and amount columns
    Returns:
        int: index of the center of array
    """
    # TODO: implement this function
    pass