.PHONY: init
init:
	alembic init migrations


check:
	black .
	isort . --line-length 120
	flake8 .