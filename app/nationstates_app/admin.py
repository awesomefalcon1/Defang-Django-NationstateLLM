from django.contrib import admin
from .models import Issue, IssueOption


class IssueOptionInline(admin.TabularInline):
    model = IssueOption
    extra = 0


@admin.register(Issue)
class IssueAdmin(admin.ModelAdmin):
    list_display = ['issue_id', 'title', 'created_at']
    list_filter = ['created_at']
    search_fields = ['title', 'description', 'issue_id']
    inlines = [IssueOptionInline]


@admin.register(IssueOption)
class IssueOptionAdmin(admin.ModelAdmin):
    list_display = ['issue', 'option_number', 'text']
    list_filter = ['issue']
    search_fields = ['text']
