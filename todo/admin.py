from django.contrib import admin
from .models import Todo


class TodoAdmin(admin.ModelAdmin):
    """
    Read as only field... To see 'created' in the database.
    Could change/custermize what the model interface looks like
    """
    readonly_fields = ('created',)


admin.site.register(Todo, TodoAdmin)
