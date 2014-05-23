import sys
from controllers import runserver
from tests import *

"""A simple REST web service that detects the language of an input string

   To run the service use [run] option

   To run tests use [test] option
"""

if __name__ == "__main__":
    if len(sys.argv) == 2:
        if sys.argv[1] == 'run':
            app = get_app(globals())
            runserver(app, 8000)
        elif sys.argv[1] == 'test':
            run_tests()
    else:
        print """Usage: language_detector.py [options]

OPTIONS:
  run       Run the application
  test      Run tests
"""