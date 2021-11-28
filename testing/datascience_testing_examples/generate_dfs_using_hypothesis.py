from hypothesis import strategies as st
from hypothesis.extra.pandas import data_frames, column

cols = [column('customer', dtype=int, unique=True, elements=st.integers(min_value=0, max_value=100_000)),
        column('price', dtype=float),
        column('prob_return', dtype=float, elements=st.floats(min_value=0, max_value=1))]
df = data_frames(cols).example()
print(df)