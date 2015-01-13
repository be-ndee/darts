run:
	python3 darts/manage.py runserver 8020

watch:
	sass --watch darts/assets/css/main.scss:darts/assets/css/main.min.css --style compressed

bower:
	python3 darts/manage.py bower install

lang_make:
	python3 darts/manage.py makemessages -a

lang_compile:
	python3 darts/manage.py compilemessages
