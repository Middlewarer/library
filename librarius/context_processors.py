from datetime import datetime
from .models import Book
import random

def current_time(request):
    time = datetime.now().strftime('%d.%m.%Y %H:%M')

    return {
        'current_time': time,
    }