# darts
This is a darts app to make games and create easy statistics. It is written in python with the framework django.

## Requirements

- Python 3.4.2
- Django 1.7.2
- Djangobower
- Sass

## Environment

Run server [http://localhost:8020/](http://localhost:8020/)

	$ make run

Let sass watch your scss files

	$ make watch

Install django-bower components

	$ make bower

Make the language-/messagefiles

	$ make lang_make

Compile the language-/messagefiles

	$ make lang_compile

## About the project

### Apps

home: contains only the welcome and help pages
user_management: registrate, login and logout users
score: score points in single mode, that means input your thrown points

## License

See [LICENSE](LICENSE).