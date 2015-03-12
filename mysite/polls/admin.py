from django.contrib import admin
from polls.models import Question, Choice
# Register your models here.
#admin.site.register(Question)

#class ChoiceInline(admin.StackedInline):
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    #fields = ['pub_date','question_text']
    fieldsets = [('Quesion',{'fields':['question_text']}),('Date information',{'fields':['pub_date'],'classes':['collapse']}),]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']

class ChoiceAdmin(admin.ModelAdmin):
    fieldsets = [('Quesion',{'fields':['question']}),('Choice',{'fields':['choice_text','votes'],'classes':['collapse']}),]
    



admin.site.register(Question, QuestionAdmin)
#admin.site.register(Choice, ChoiceAdmin)
