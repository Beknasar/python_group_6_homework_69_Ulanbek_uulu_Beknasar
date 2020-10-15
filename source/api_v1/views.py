from django.shortcuts import render
import json
from datetime import datetime
from django.http import HttpResponse, HttpResponseNotAllowed, JsonResponse, HttpResponseBadRequest
from django.views.decorators.csrf import ensure_csrf_cookie


def index_view(request):
    return render(request, 'index.html')


def get_token_view(request, *args, **kwargs):
    if request.method == 'GET':
        return HttpResponse()
    return HttpResponseNotAllowed('Only GET request are allowed')


@ensure_csrf_cookie
def json_add_view(request, *args, **kwargs):
    if request.method == 'POST':
        answer = {}
        try:
            data = json.loads(request.body)
            # print(data)
            answer['answer'] = float(data['A']) + float(data['B'])
            return JsonResponse(answer)
        except TypeError:
            response = JsonResponse({'error': "You must input the numbers!"})
            response.status_code = 400
            return response


@ensure_csrf_cookie
def json_subtract_view(request, *args, **kwargs):
    if request.method == 'POST':
        answer = {}
        try:
            data = json.loads(request.body)
            # print(data)
            answer['answer'] = float(data['A']) - float(data['B'])
            return JsonResponse(answer)
        except TypeError:
            response = JsonResponse({'error': "You must input the numbers!"})
            response.status_code = 400
            return response


@ensure_csrf_cookie
def json_multiply_view(request, *args, **kwargs):
    if request.method == 'POST':
        answer = {}
        try:
            data = json.loads(request.body)
            # print(data)
            answer['answer'] = float(data['A']) * float(data['B'])
            return JsonResponse(answer)
        except TypeError:
            response = JsonResponse({'error': "You must input the numbers!"})
            response.status_code = 400
            return response


@ensure_csrf_cookie
def json_divide_view(request, *args, **kwargs):
    if request.method == 'POST':
        answer = {}
        try:
            data = json.loads(request.body)
            # print(data)
            answer['answer'] = float(data['A']) / float(data['B'])
            return JsonResponse(answer)
        except ZeroDivisionError:
            response = JsonResponse({'error': "Division by zero!"})
            response.status_code = 400
            return response
        except TypeError:
            response = JsonResponse({'error': "You must input the numbers!"})
        response.status_code = 400
        return response
