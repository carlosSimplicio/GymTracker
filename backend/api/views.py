from http import HTTPStatus
from django.http import HttpResponse

# Create your views here.

def hello(_):
  return HttpResponse('hello', status=HTTPStatus.OK)