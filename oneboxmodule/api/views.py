from rest_framework.views import APIView
from rest_framework.response import Response


class OneBoxView(APIView):

    def get(self, request, format=None):
        response_dict = {
            'OneBoxResults': {
                'resultCode': 'success',
                'MODULE_RESULT': {
                    'url': 'http://myurl.com',
                    'Title': 'My Title',
                    'Field': 'Hello World, using an external provider for GSA works!'
                },
                'IMAGE_SOURCE': 'http://i.imgur.com/CZxryL6.png'
            }
        }

        return Response(response_dict)
