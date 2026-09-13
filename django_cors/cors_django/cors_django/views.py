from django.http import JsonResponse


def hello_no_cors(request):
    print("[DJANGO] GET /api/no-cors/hello")
    return JsonResponse({
        "message": "Привет с эндпоинта БЕЗ CORS (Django)!",
        "path": "/api/no-cors/hello",
    })


def hello_cors(request):
    print("[DJANGO] GET /api/cors/hello")
    return JsonResponse({
        "message": "Привет с эндпоинта С CORS (Django)!",
        "path": "/api/cors/hello",
    })