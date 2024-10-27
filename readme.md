# Clone Repo
# Install Dependencies

# Add the env file with the following
DEBUG=True
SECRET_KEY='django-insecure-(9rp(frl=ag-_vd+(jgnz!ka(5h6254u&09%$wixl)o8736#(z'
CELERY_BROKER_URL=redis://localhost:6379/0
CELERY_RESULT_BACKEND=redis://localhost:6379/0

Run the following commands
python manage.py makemigrations
python manage.py migrate

# Run the Celery worker
celery -A project worker -l info

# Run the Celery beat scheduler
celery -A project beat -l info

# Run the server
python manage.py runserver

# Test APIs using Postman

api/brands/
api/products/

# Django Admin 
first create super user
python manage.py createsuperuser

# Login to admin
http://localhost:8000/admin/

# Create a new brand
For my case I used Apple as the brand name
and used amazon.com as the url
base_url = "https://www.amazon.co.uk"
store_url = "https://www.amazon.co.uk/stores/page/B49C58BF-1F41-4220-8249-B43BD19F919C"
