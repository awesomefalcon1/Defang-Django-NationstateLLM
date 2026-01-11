"""
Django management command to sync issues from the NationStates database.
Usage: python manage.py sync_issues
"""
from django.core.management.base import BaseCommand
from nationstates_app.scraper import sync_issues_to_database


class Command(BaseCommand):
    help = 'Sync issues from the NationStates database website'

    def handle(self, *args, **options):
        self.stdout.write('Fetching issues from NationStates database...')
        
        result = sync_issues_to_database()
        
        self.stdout.write(
            self.style.SUCCESS(
                f'Successfully synced {result["total"]} issues: '
                f'{result["created"]} created, {result["updated"]} updated'
            )
        )
