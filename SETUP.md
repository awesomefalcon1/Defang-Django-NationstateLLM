# Setup Guide

## Virtual Environment

A virtual environment has been created at `venv/`. To use it:

### Activate the virtual environment:

```bash
source venv/bin/activate
```

Or use the helper script:
```bash
source activate_venv.sh
```

### Deactivate when done:

```bash
deactivate
```

## Initial Setup Steps

1. **Activate the virtual environment:**
   ```bash
   cd Defang-Django-NationstateLLM
   source venv/bin/activate
   ```

2. **Navigate to the app directory:**
   ```bash
   cd app
   ```

3. **Run migrations:**
   ```bash
   python manage.py migrate
   ```

4. **Create a superuser (optional, for admin access):**
   ```bash
   python manage.py createsuperuser
   ```

5. **Sync issues from the database:**
   ```bash
   python manage.py sync_issues
   ```

6. **Run the development server:**
   ```bash
   python manage.py runserver
   ```

## Access the Application

- **Main app**: http://localhost:8000/nationstates/
- **Admin panel**: http://localhost:8000/admin/
- **API**: http://localhost:8000/nationstates/api/issues/

## Notes

- The virtual environment must be activated before running any Django commands
- All dependencies are already installed in the virtual environment
- The scraper will fetch issues from http://www.mwq.dds.nl/ns/results/
