from time import time

from bottle import *
from pprint import pprint
from modern_python_course_examples.algebra import area_circle
import os


secret = 'The quick brown fox jumped over the'
file_template = '''\
<h1>list of files in <em>congress_data</em></h1>
<hr>
<ol>
    % for file in files:
        <li><a href="files/{{file}}">{{file}} /> </li>
    %
</ol>
'''

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
    last_visit = request.get_cookie('last_visit', 'Unknown', secret=secret) # browser by default sends the cookie set by server
    # on the other hand, curl does not send the cookie by default. curl "http://localhost:8080/area?radius=10"
    print(f'last visit time {last_visit}')
    response.set_header('Vary', 'Accept') # always do this for content negotiation. Thumb rule, if you are checking for
    # any header down below, it should be tagged with Vary as above
    response.set_cookie('last_visit', time.ctime(), secret=secret)
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

@route('/files')
def show_files():
    response.set_header('Vary', 'Accept')
    files = os.listdir('congress_data')
    print(f'printing files {files}')
    if 'text/html' not in request.headers.get('Accept', '*/*'):
       return dict(files=files)
    return template(file_template, files=files)


@route('/files/<filename>')
def serve_one_file(filename):
    return static_file(filename, './congress_data')


if __name__ == '__main__':
    run(host='localhost', port=8080)