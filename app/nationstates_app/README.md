# NationStates Django Integration

This Django app integrates the NationStates LLM functionality with Django and provides a web interface for managing and viewing issues from the NationStates database.

## Features

- **Issue Database Integration**: Scrapes and stores issues from http://www.mwq.dds.nl/ns/results/
- **BeautifulSoup Scraper**: Parses the issues database website to extract issue titles
- **Django Models**: Stores issues and their options in the database
- **Web Interface**: View issues list and details
- **API Endpoints**: RESTful API for accessing issues data
- **Management Command**: Command-line tool to sync issues from the database

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run migrations:
```bash
python manage.py migrate
```

3. Sync issues from the database:
```bash
python manage.py sync_issues
```

## Usage

### Web Interface

- **Issue List**: Visit `/nationstates/` to see all issues
- **Issue Detail**: Visit `/nationstates/issue/<issue_id>/` to see issue details
- **Sync Issues**: Click the "Sync Issues from Database" button on the issue list page

### API Endpoints

- `GET /nationstates/api/issues/` - Get all issues as JSON
- `POST /nationstates/api/sync/` - Trigger issue sync from database

### Management Command

```bash
python manage.py sync_issues
```

This command will:
1. Fetch the issues database page
2. Parse all issues using BeautifulSoup
3. Store them in the Django database

## Models

### Issue
- `issue_id`: Integer, unique identifier for the issue
- `title`: CharField, the issue title
- `description`: TextField, optional description
- `created_at`: DateTime, when the issue was created in the database
- `updated_at`: DateTime, when the issue was last updated

### IssueOption
- `issue`: ForeignKey to Issue
- `option_number`: Integer, the option number
- `text`: TextField, the option text
- `created_at`: DateTime, when the option was created

## Integration with NationStates LLM

The NationStates LLM modules are integrated in `nationstates_app/modules/`:
- `gptnation.py`: Contains the `Gptnation` class for interacting with the NationStates API
- `nations.py`: Contains the list of nations to manage

## Scraper

The scraper (`scraper.py`) uses BeautifulSoup to parse the HTML from the issues database website. It:
1. Fetches the page from http://www.mwq.dds.nl/ns/results/
2. Parses the HTML to extract issue titles in the format `#NUMBER Title`
3. Returns a list of dictionaries with `issue_id` and `title`

## Admin Interface

The Django admin interface is available at `/admin/` where you can:
- View and edit issues
- View and edit issue options
- Manage the database directly
