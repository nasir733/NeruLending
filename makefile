
run:
	./manage.py runserver


git-save:
	git add .
	git commit -am "update"

migrations:
	python manage.py makemigrations
	python manage.py migrate

update:
	git push heroku-release & git push heroku-holliday & git push heroku & git push prof

applymigrations:
	heroku run python manage.py migrate --app getdinerotoday & heroku run python manage.py migrate --app hollidayconsulting & heroku run python manage.py migrate --app sawcorp & heroku run python manage.py migrate --app professorhoneyscreditlenging

bashgdt:
	heroku run bash --app getdinerotoday