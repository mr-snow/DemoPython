from django.contrib import admin

import todoapp

from todoapp.models import Task

admin.site.register(Task)
