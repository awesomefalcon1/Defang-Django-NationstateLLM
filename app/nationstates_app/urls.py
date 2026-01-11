from django.urls import path
from . import views

app_name = 'nationstates_app'

urlpatterns = [
    path('', views.issue_list, name='issue_list'),
    path('issue/<int:issue_id>/', views.issue_detail, name='issue_detail'),
    path('api/issues/', views.issues_api, name='issues_api'),
    path('api/sync/', views.sync_issues_api, name='sync_issues_api'),
]
