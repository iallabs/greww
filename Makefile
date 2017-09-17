# Greww Makefile

# Shell
SHELL := /bin/bash
#Project
PROJECT = "Greww"
#Version
RELEASE = "0.0.1"
#Authors
AUTHORS = ""
# Path to source directory
GREWW_PATH := .
# OS machine
OS_TYPE = 'uname -a'

##### PYTHON

prebuild:
	@echo "Preparing Greww build"
	@echo "Installing requirements"
	pip install -r requirements.txt

setup:
	echo "Setup Greww"
	sudo python setup.py install

test:
	echo "Test Greww"
	python setup.py test


# register:
#	  python setup.py register

clean:
	rm -f MANIFEST
	rm -rf build dist

all: prebuild configuration setup


.PHONY: clean
