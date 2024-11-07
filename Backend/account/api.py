from django.http import JsonResponse
from rest_framework.decorators import api_view, authentication_classes, permission_classes 

#to override the auth a permission with the new model we created for the user and with the auth app

@api_view(['POST']) #decorator that says we're expacting some data from an api, type post
def signup(request):
    data = request.data #assegna i dati della richiesta a una variabile
    message = 'success'
    return JsonResponse({'status': message})