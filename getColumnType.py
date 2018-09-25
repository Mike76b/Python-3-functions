# -*- coding: utf-8 -*-

"""
The following function was coded to get the types of the data within a column
from a dataframe in Pandas.
"""
def get_column_type(data_frame_name, column_name):
    """
    Input: data_frame_name
           column name <- string
    Output: print the set of values types within the column.
    """
    dtype_column = set()
    for row in data_frame_name[column_name]:
        dtype_column.add(type(row))
    print(dtype_column)
    return None

