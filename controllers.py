from wsgiservice import *
import guess_language


@mount('/')
class LanguageDetector(Resource):
    """Resource to be served with WsgiService
       Accepts POST requests, for other methods raises error 501 Not Implemented error
    """

    KNOWN_METHODS = ['POST']
    EXTENSION_MAP = [('.json', 'application/json')]

    def POST(self):
        """Detects the language of an input string

        :returns: a json with an information about the language of the input string or an empty dict
        """

        response = {}
        text = self.request.POST.get('text')
        if text:
            response['language'] = guess_language.guessLanguage(text)

        return response


def runserver(app, port):
    """Runs a WSGI server that serves a given app on the specified port

    :param app: an app to be served

    :param port: a port that will be used to serve the app
    """

    from wsgiref.simple_server import make_server
    print "Running on port {0}".format(port)
    make_server('', port, app).serve_forever()
