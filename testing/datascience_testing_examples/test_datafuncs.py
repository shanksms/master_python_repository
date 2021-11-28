import pytest

from testing.datascience_testing_examples import datafuncs
import numpy as np

def test_min_max_scaler():
    arr = np.array([1, 2, 3])
    tfm = datafuncs.min_max_scaler(arr)
    assert np.allclose(tfm, np.array([0, 0.5, 1]))
    assert tfm.min() == 0
    assert tfm.max() == 1
    with pytest.raises(AttributeError):
        datafuncs.min_max_scaler([])
        #datafuncs.min_max_scaler(2)

