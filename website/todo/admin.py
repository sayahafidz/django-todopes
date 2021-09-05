from django.contrib import admin
from .models import Todo
# Register your models here.

# kustomisasi django admin


class TodoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'status',)


admin.site.register(Todo, TodoAdmin)
