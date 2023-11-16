from django.contrib import admin

# Register your models here.
from .models import Choice, Question


class ChoiceInline(admin.TabularInline):
    # class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["question_text"]}),
        ("Date information", {"fields": ["pub_date"], "classes": ["collapse"]}),
    ]
    inlines = [ChoiceInline]
    list_display = ["question_text", "pub_date", "was_published_recently"]
    # Adding a filter by date
    list_filter = ["pub_date"]
    # Adding a search field:
    search_fields = ["question_text"]


admin.site.register(Question, QuestionAdmin)

# To add a choice adding form, unique for a question, use:
# admin.site.register(Choice)
