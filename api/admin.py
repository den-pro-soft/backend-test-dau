from django.contrib import admin
from api.models import Question, Answer

admin.site.register(Answer)
admin.site.register(Question)