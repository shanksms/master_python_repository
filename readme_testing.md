# Python testing related information

### Resources
[ pycon datascience testing ] (https://www.youtube.com/watch?v=0ysyWk-ox-8&t=852s)
[ pycon datascience testing git code ] (https://github.com/ericmjl/data-testing-tutorial) 
[ Writing tests for legacy code] (https://www.youtube.com/watch?v=LDdUuoI_lIg)
[ datascience testing] (https://www.youtube.com/watch?v=yACtdj1_IxE)

### Testing loop
1. Write test for a function
2. Write the function
3. Execute pytest
4. Go back to step 1

### how does pytest discovers tests 
Here’s a brief overview of the naming conventions to keep your test code discoverable by pytest:

Test files should be named test_<something>.py or <something>_test.py.
Test methods and functions should be named test_<something>.
Test classes should be named Test<Something>.


### expecting exception in pytest
```python
import pytest
with pytest.raises(TypeError):
    # this piece of code will throw TypeError exception
    pass

with pytest.raises(TypeError) as exc_info:
    # this piece of code will throw TypeError exception
    exception_msg = exc_info.value.args[0]
    pass

```