from wsgiservice import *
import guess_language


@mount('/')
class Documents(Resource):

    EXTENSION_MAP = [('.json', 'application/json')]

    def POST(self):
        """Detect the language of an input string"""

        response = {}
        text = self.request.POST.get('text')
        if text:
            response['language'] = guess_language.guessLanguage(text)

        return response

app = get_app(globals())

if __name__ == "__main__":
    from wsgiref.simple_server import make_server
    print "Running on port 8000"
    make_server('', 8000, app).serve_forever()
