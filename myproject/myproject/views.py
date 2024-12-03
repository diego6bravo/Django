from django.http import HttpResponse, HttpResponseNotFound

def handler404(request, exception):
    return HttpResponse('PAILA!!!! esta página no existe perrito')

