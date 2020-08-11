SRC_PATH=./json_search
MAIN_SCRIPT=server.py

clean-pyc:
	find . -name '*.pyc' -exec rm --force {} +
	find . -name '*.pyo' -exec rm --force {} +

# Run project
run:
	# NOTE: 
	# This will make a second make instance and run project through poetry.
	# If using own venv and using exported requirements.txt please use
	# 'make run-no-poetry' or replace below function with 'make run-no-poetry'
	make run-poetry

# Run project through poetry
run-poetry:
	poetry run python $(SRC_PATH)/$(MAIN_SCRIPT)

run-no-poetry:
	python $(SRC_PATH)/$(MAIN_SCRIPT)

# Install dependenciess through poetry
configure-poetry:
	poetry install

# Install dependencies through pip
configure-pip:
	python3 -m pip install -r requirements.txt

# Run tests
test:
	make clean-pyc
	pytest

# Export requirements.txt from Poetry
export-requirements:
	poetry run python -m pip freeze > requirements.txt

# Built with docker. did not spend time on this, probably not working well
build-docker:
	docker build .
