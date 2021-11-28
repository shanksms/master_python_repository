import pandas as pd
import numpy as np
from pandas.util.testing import (
    assert_frame_equal,
    assert_series_equal,
    assert_index_equal
)


df1 = pd.DataFrame(
    {
        'channel': ['email', 'paid_search', 'display', 'email'],
        'customer': [1, 4, 4, 3],
        'order': [1010, 2050, 2050, 3232]
    }
)

df2 = pd.DataFrame(
    {
        'channel': ['email', 'paid_search', 'display', 'email'],
        'customer': [1, 4, 4, 3],
        'order': [1010, 2050, 2050, 3232]
    }
)


assert ~df1.duplicated().any()
assert_frame_equal(df1, df2,
                   check_dtype=False, #
                   check_like=True, # order of columns does not matter
                   check_less_precise=4) # check till 4 decimal points
