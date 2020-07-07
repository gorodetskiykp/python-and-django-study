from unittest.mock import MagicMock

pd = MagicMock()

def Series(data):
    return MagicMock()

def sort_values(ascending, inplace):
    return MagicMock()
    
def sort_index(ascending, inplace):
    return MagicMock()

mock_series = MagicMock()
mock_series.sort_values = MagicMock(spec = sort_values)
mock_series.sort_index = MagicMock(spec = sort_index)

pd.Series.mock_return_value = MagicMock(spec = Series)