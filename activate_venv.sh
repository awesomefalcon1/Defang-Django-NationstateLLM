#!/bin/bash
# Helper script to activate the virtual environment and navigate to app directory

cd "$(dirname "$0")"
source venv/bin/activate
cd app
echo "Virtual environment activated!"
echo "You are now in: $(pwd)"
echo ""
echo "Useful commands:"
echo "  python manage.py migrate          - Run database migrations"
echo "  python manage.py sync_issues       - Sync issues from database"
echo "  python manage.py runserver         - Start development server"
echo "  python manage.py createsuperuser   - Create admin user"
echo ""
echo "To deactivate, type: deactivate"
