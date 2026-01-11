from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from .models import Issue, IssueOption
from .scraper import IssuesDatabaseScraper
import json


def issue_list(request):
    """List all issues"""
    issues = Issue.objects.all()[:100]  # Limit to first 100 for performance
    context = {
        'issues': issues
    }
    return render(request, 'nationstates_app/issue_list.html', context)


def issue_detail(request, issue_id):
    """View details of a specific issue"""
    issue = get_object_or_404(Issue, issue_id=issue_id)
    options = issue.options.all()
    context = {
        'issue': issue,
        'options': options
    }
    return render(request, 'nationstates_app/issue_detail.html', context)


@require_http_methods(["POST"])
def sync_issues_api(request):
    """API endpoint to trigger issue sync"""
    from .scraper import sync_issues_to_database
    
    try:
        result = sync_issues_to_database()
        return JsonResponse({
            'success': True,
            'total': result['total'],
            'created': result['created'],
            'updated': result['updated']
        })
    except Exception as e:
        return JsonResponse({
            'success': False,
            'error': str(e)
        }, status=500)


def issues_api(request):
    """API endpoint to get issues as JSON"""
    issues = Issue.objects.all()
    data = []
    
    for issue in issues:
        options = [{'number': opt.option_number, 'text': opt.text} 
                  for opt in issue.options.all()]
        data.append({
            'id': issue.issue_id,
            'title': issue.title,
            'description': issue.description,
            'options': options
        })
    
    return JsonResponse({'issues': data}, safe=False)
