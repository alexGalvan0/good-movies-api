from django.http import JsonResponse


def getRoutes(request):

    routs = [
        '/api/token',
        '/api/token/refresh'
    ]
    return JsonResponse(routs, safe=False)