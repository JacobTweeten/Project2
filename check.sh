set -e
set -x

poetry run black --check *.py && poetry run isort --check *.py && poetry run flake8 *.py || exit 1

# Black and flake8 conflict... whenever I run black it makes the lines longer, and whenever I run flake8 it tells me the lines are too long
# Is there a setting I could be using so that black does not make my lines long?

echo "Everything works!"