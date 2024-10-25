from django.shortcuts import render, redirect
from django.http import JsonResponse
import requests

def index(request):
    text = {
        'welcome_message': 'чета там Space'
    }

    return JsonResponse({
        'message': text,
        'tools_link': '/tool/',
    })



def tool(request):
    text = {
        'tool_description': 'хуйня с тулами '
    }

    return JsonResponse({
        'tools': TOOLS
    })