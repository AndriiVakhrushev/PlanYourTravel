# Makefile commands
# docs https://svn.python.org/projects/python/trunk/Doc/Makefile

.PHONY: check-tabs install-dev-req flake

# Check your editor
check-tabs:
	cat -e -t -v makefile

install-dev-req:
	pip3 install -r requirements/dev_requirements.txt

flake:
	flake8