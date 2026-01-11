"""
Scraper to parse the NationStates issues database from http://www.mwq.dds.nl/ns/results/
"""
import requests
from bs4 import BeautifulSoup
import re
from typing import List, Dict, Optional


class IssuesDatabaseScraper:
    """Scraper for the NationStates issues database"""
    
    BASE_URL = "http://www.mwq.dds.nl/ns/results/"
    
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        })
    
    def fetch_page(self) -> Optional[str]:
        """Fetch the issues database page"""
        try:
            response = self.session.get(self.BASE_URL, timeout=30)
            response.raise_for_status()
            return response.text
        except requests.RequestException as e:
            print(f"Error fetching page: {e}")
            return None
    
    def parse_issues(self, html_content: str) -> List[Dict]:
        """
        Parse issues from the HTML content.
        Returns a list of dictionaries with issue_id and title.
        The page format is: #NUMBER Title
        """
        soup = BeautifulSoup(html_content, 'html.parser')
        issues = []
        seen_ids = set()
        
        # Get all text content from the page
        text_content = soup.get_text()
        
        # Pattern to match issue entries: #NUMBER Title
        # The pattern matches: # followed by digits, then whitespace, then the title
        # Stops at the next #NUMBER or end of string
        pattern = r'#(\d+)\s+([^\n#]+?)(?=\n#\d+|\n\n|$)'
        
        matches = re.finditer(pattern, text_content, re.MULTILINE)
        
        for match in matches:
            issue_id = int(match.group(1))
            title = match.group(2).strip()
            
            # Skip if we've already seen this issue_id
            if issue_id in seen_ids:
                continue
            
            # Clean up the title (remove extra whitespace, newlines)
            title = re.sub(r'\s+', ' ', title)
            title = title.strip()
            
            # Skip empty titles
            if not title:
                continue
            
            issues.append({
                'issue_id': issue_id,
                'title': title
            })
            seen_ids.add(issue_id)
        
        # Also check for links and other HTML elements that might contain issue titles
        for element in soup.find_all(['a', 'li', 'p', 'div', 'span']):
            text = element.get_text().strip()
            if text.startswith('#'):
                match = re.match(r'#(\d+)\s+(.+)', text)
                if match:
                    issue_id = int(match.group(1))
                    title = match.group(2).strip()
                    
                    # Avoid duplicates
                    if issue_id not in seen_ids and title:
                        issues.append({
                            'issue_id': issue_id,
                            'title': title
                        })
                        seen_ids.add(issue_id)
        
        # Sort by issue_id
        issues.sort(key=lambda x: x['issue_id'])
        
        return issues
    
    def scrape_all_issues(self) -> List[Dict]:
        """Fetch and parse all issues from the database"""
        html_content = self.fetch_page()
        if not html_content:
            return []
        
        return self.parse_issues(html_content)


def sync_issues_to_database():
    """
    Management command helper to sync issues from the website to the database.
    This should be called from a Django management command.
    """
    from .models import Issue, IssueOption
    
    scraper = IssuesDatabaseScraper()
    issues_data = scraper.scrape_all_issues()
    
    created_count = 0
    updated_count = 0
    
    for issue_data in issues_data:
        issue, created = Issue.objects.update_or_create(
            issue_id=issue_data['issue_id'],
            defaults={
                'title': issue_data['title']
            }
        )
        
        if created:
            created_count += 1
        else:
            updated_count += 1
    
    return {
        'total': len(issues_data),
        'created': created_count,
        'updated': updated_count
    }
