from django.contrib import admin
from .models import Question

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id','subject','content','date')
    search_fields=['subject','id']
    
admin.site.register(Question, QuestionAdmin)

