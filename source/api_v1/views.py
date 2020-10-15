from django.shortcuts import render
import json
from datetime import datetime
from django.http import HttpResponse, HttpResponseNotAllowed, JsonResponse, HttpResponseBadRequest
from django.views.decorators.csrf import ensure_csrf_cookie


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
            print(data)
            answer['answer'] = data['A'] + data['B']
            return JsonResponse(answer)
        except:
            response = JsonResponse({'error': "Division by zero!"})
            response.status_code = 400
            return response


@ensure_csrf_cookie
def json_subtract_view(request, *args, **kwargs):
    if request.method == 'POST':
        answer = {}
        try:
            data = json.loads(request.body)
            print(data)
            answer['answer'] = data['A'] - data['B']
            return JsonResponse(answer)
        except:
            response = JsonResponse({'error': "Division by zero!"})
            response.status_code = 400
            return response


@ensure_csrf_cookie
def json_multiply_view(request, *args, **kwargs):
    if request.method == 'POST':
        answer = {}
        try:
            data = json.loads(request.body)
            print(data)
            answer['answer'] = data['A'] * data['B']
            return JsonResponse(answer)
        except:
            response = JsonResponse({'error': "Division by zero!"})
            response.status_code = 400
            return response


@ensure_csrf_cookie
def json_divide_view(request, *args, **kwargs):
    if request.method == 'POST':
        answer = {}
        try:
            data = json.loads(request.body)
            print(data)
            answer['answer'] = data['A'] / data['B']
            return JsonResponse(answer)
        except:
            response = JsonResponse({'error': "Division by zero!"})
            response.status_code = 400
            return response
