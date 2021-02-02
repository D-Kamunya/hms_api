install:
	pip3 install -r requirements.txt
test:
	pytest --cov-report term-missing --cov -p no:warnings

migrations:
	python manage.py makemigrations

migrate:
	python3 manage.py migrate

celery:
	celery -A erp_apiv2  worker -B -l info

superuser:
	python manage.py createsuperuser

collectstatic:
	python manage.py collectstatic

serve:
	python3 manage.py runserver

shell:
	python manage.py shell


set_env_vars:
	source venv/bin/activate;


.PHONY: set_env_vars
