from oauth2_provider.views.generic import ProtectedResourceView
from django.http import HttpResponse

# Create your views here.
class ApiEndpoint(ProtectedResourceView):
    def get(self, request, *args, **kwargs):
        return HttpResponse('Hola - OAuth2')
