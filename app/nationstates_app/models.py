from django.db import models


class Issue(models.Model):
    """Model to store NationStates issues from the database"""
    issue_id = models.IntegerField(unique=True, db_index=True)
    title = models.CharField(max_length=500)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['issue_id']
        verbose_name = 'Issue'
        verbose_name_plural = 'Issues'
    
    def __str__(self):
        return f"#{self.issue_id}: {self.title}"


class IssueOption(models.Model):
    """Model to store options for each issue"""
    issue = models.ForeignKey(Issue, related_name='options', on_delete=models.CASCADE)
    option_number = models.IntegerField()
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['issue', 'option_number']
        unique_together = ['issue', 'option_number']
        verbose_name = 'Issue Option'
        verbose_name_plural = 'Issue Options'
    
    def __str__(self):
        return f"Issue #{self.issue.issue_id} - Option {self.option_number}"
