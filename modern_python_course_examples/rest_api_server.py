from time import time

from bottle import *
from pprint import pprint
from modern_python_course_examples.algebra import area_circle

@route('/')
def welcome():
    pprint(dict(request.headers))
    # content negotiations
    if 'text/html' in request.headers.get('Accept', '*/*'):
        response.content_type = 'text/html'
        return '<h1>Howdy</h1>'

    response.content_type= 'text/plain'
    return 'hello'


@route('/now')
def time_service():
    print('in the time service')
    response.content_type = 'text/plain'
    # cache the response at user side or ngnix for 1 second
    response.set_header('Cache-Control', 'max-age=5')
    return time.ctime()

@route('/upper/<word>')
def upper_case(word):
    response.content_type = 'text/plain'
    return word.upper()

@route('/area')
def area_circle_service():
    pprint(dict(request.query))
    try:
        radius = float(request.query.get('radius', 0.0))
    except ValueError as exc:
        return exc.args[0]
    _area = area_circle(radius)
    pprint(f'area { _area}')
    if 'text/html' in request.headers.get('Accept', '*/*'):
        response.content_type = 'text/html'
        # when you hit from browser, below is returned
        return f'<h1>{_area}</h1>'
    # when you hit curl, below is returned. content type is text/plain. curl  "http://localhost:8080/area?radius=10"
    return dict(area=_area, radius=radius, path=request.path)


if __name__ == '__main__':
    run(host='localhost', port=8080)