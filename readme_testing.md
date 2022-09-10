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

### marking tests in pytest
```python
import pytest

@pytest.mark.smoke
def test_list_raises():
    pass

@pytest.mark.smoke
def test_get_raises():
    pass

```
now, you can run above tests with following command
```shell script
pytest -v m 'smoke' test_api_exceptions.py
```
we can combine multiple markers with 'and' keyword
```shell script
pytest -v m 'smoke and get' test_api_exceptions.py
```

### skipping tests and failing tests
we can skip test by decorating test function with @pytest.mark.skip(reason='misunderstood the API')
@pytest.mark.xfail will expect a test to fail

### parameterize tests
```python
task_ids = ['Task({},{},{})'.format(t.summary, t.owner, t.done)
 	            for t in tasks_to_try]
 	
 	
 	@pytest.mark.parametrize('task', tasks_to_try, ids=task_ids)
 	def test_add_5(task):
 	    """Demonstrate ids."""
 	    task_id = tasks.add(task)
 	    t_from_db = tasks.get(task_id)
 	    assert equivalent(t_from_db, task)
```
To compromise, we can use the ids optional parameter to parametrize() to make our own identifiers for each task data set. 
The ids parameter needs to be a list of strings the same length as the number of data sets. However, 
because we assigned our data set to a variable name, tasks_to_try, we can use it to generate ids:

### pytest fixtures
Now that you’ve seen the basics of pytest, let’s turn our attention to fixtures, which are essential 
to structuring test code for almost any non-trivial software system. Fixtures are functions that are run by pytest 
before (and sometimes after) the actual test functions. The code in the fixture can do whatever you want it to. 
You can use fixtures to get a data set for the tests to work on. You can use fixtures to get a system into a known state
before running a test. Fixtures are also used to get data ready for multiple tests.

```python
import pytest
@pytest.fixture()
def some_data():
    """Return answer to ultimate question."""
    return 42


def test_some_data(some_data):
    """Use fixture return value in a test."""
    assert some_data == 42
```

### property based testing.versus example based testing
[hypothesis testing](https://hypothesis.readthedocs.io/en/latest/quickstart.html)
example based testing
1. difficult to maintain
2. Tedious to write
3. Some times, lots of repetitions
4. Too much of detail oriented

property based testing
1. Focus on high level requirement
2. properties define behaviour
3. Randomly generated inputs


### doc test
The doctest module is one of the most useful modules within Python. It allows you to combine documenting your code with tests to make sure that it keeps working as it is supposed to.  
```python
def square(n: int) -> int:
    '''

    >>> square(2)
    4
    >>> square(3)
    9
    >>> square('x')
    Traceback (most recent call last):
    TypeError: can't multiply sequence by non-int of type 'str'
    '''
    return n * n

if __name__ == '__main__':
    import doctest
    doctest.testmod()

```
Perhaps you have noticed from the preceding examples that the syntax is very similar to the regular Python console, and that is because it is. The doctest input is nothing more than the output of  
a regular Python shell session. This is what makes testing with this module so intuitive; simply write the code in the Python console and copy the output into a docstring to get tests. Here is an example:  

#### Automatic arguments using fixtures
The py.test fixture system is one of the most magical features of py.test. It magically executes a fixture function with the same name as your arguments. Let’s create a basic fixture to demonstrate this:  
```python
import pytest

@pytest.fixture
def name():
    return 'Rick'

def test_something(name):
    assert name == 'Rick'
```

When the test_something() test is executed, the name argument will be filled with the output from the name() function automatically.  
Because arguments are automatically filled by fixtures, the naming of the arguments becomes very important, as fixtures can easily collide with other fixtures.  
To prevent collisions, the scope is set to function by default. However, class, module, and session are also valid options for the scope. There are several fixtures available by default,  
some of which you will use often, and others most likely never. A complete list can always be generated with the following command:  
#### Custom fixtures
Bundled fixtures are quite useful, but within most projects, you will want to create your own fixtures to make things easier. Fixtures make it trivial to repeat code that is needed more often.  
You are most likely wondering how this is different from a regular function, context wrapper, or something else, but the special thing about fixtures is that they themselves can accept fixtures as well. So, if your function needs the pytestconfig variables, it can ask for them without needing to modify the calling functions.  

You can create a fixture out of anything that would be useful to reuse. The basic premise is simple enough: a function with the pytest.fixture decorator, which returns a value that will be passed along as an argument. Also, the function can take parameters and fixtures just as any test can.  

The only notable variation is pytest.yield_fixture. This fixture variation has one small difference: the actual test will be executed at the yield (more than one yield results in errors) and the code before/after functions as setup/teardown code, which is useful for things like database connections and file handles.  
A basic example of a fixture and a yield_fixture looks like this:  
```python
import pytest

@pytest.yield_fixture
def some_yield_fixture():
    with open(__file__ + '.txt', 'w') as fh:
        # Before the function
        yield fh
        # After the function

@pytest.fixture
def some_regular_fixture():
    # Do something here
    return 'some_value_to_pass_as_parameter'

def some_test(some_yield_fixture, some_regular_fixture):
    some_yield_fixture.write(some_regular_fixture)
```

