import os
from django.conf import settings
from django.core.management import execute_from_command_line
from django.http import HttpResponse
from django.urls import path
settings.configure(
    DEBUG=True,
    SECRET_KEY='x',
    ROOT_URLCONF=__name__,
    ALLOWED_HOSTS=['*'],
)

def upload(request):
    return HttpResponse("""
        <h1>Django in Docker</h1>
        <form method='post' enctype='multipart/form-data'>
            <input type='file'><button>Upload</button>
        </form>
    """)

urlpatterns = [path('', upload)]

execute_from_command_line(['manage.py', 'runserver', '0.0.0.0:8000'])
