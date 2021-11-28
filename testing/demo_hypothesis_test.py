from hypothesis import given
from hypothesis import strategies as st
from hypothesis.extra.pandas import data_frames, column

def backwards_all_caps(text):
    return text[::-1].upper()

@given(st.text())
def test_backwards_allcaps(input_text):
    modified = backwards_all_caps(input_text)
    print(modified)
    assert input_text.upper() == ''.join(reversed(modified))





