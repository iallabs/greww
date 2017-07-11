# Greww Makefile


# Shell
SHELL := /bin/bash
#Project
PROJECT = "Greww"
#Version
RELEASE = "0.0.0"
#Authors
AUTHORS = ""
# Compiler
CXX ?= g++
# CPP files
CGREW_PATH = ""
# Path to source directory
GREWW_PATH := .
# OS machine
OS_TYPE = 'uname -a'
# CPP EXTENSIONS
CPP_EXT = ".cpp"
# CPP Binaries
CPP_BIN = ".so"

# read files function


# This is like bash files

# VENV

#_virtualenv:
#	# create virtual env
#	virtualenv _virtualenv
#	_virtualenv/bin/pip install --upgrade pip
#	_virtualenv/bin/pip install --upgrade setuptools
#
#_use_env:
#	# use virtual env
#	source _virtualenv/bin/activate

# SHARED COMPILE CPP

tobincppfile:
	for f in greww/cgreww/*.$CPP_EXT; do
		filename=$(basename $f)
		nameonly="${filename%.*}"
		binfile=$nameonly$CPP_BIN
		$(CXX) -shared -o $binfile $filename
	done

cleanbincpp:
	rm -rf greww/cgreww/*.so





##### PYTHON

prebuild:
	@echo "Preparing Greww build"
	@echo "Installing requirements"
	pip install -r requirements.txt

configuration:
	echo "Configuring machine"
	#
	# make directions and constants at Shell
	#

setup:
	echo "Setup Greww"
	sudo python setup.py install

test:
	echo "Test Greww"
	python setup.py test

reported_test:
	echo "Test Greww with reports"
	sudo python setup.py rtest


# register:
#	  python setup.py register

clean:
	rm -f MANIFEST
	rm -rf build dist

#deactivate_env:
#	deactivate

#ifneq ($(wildcard test-requirements.txt),)
#	_virtualenv/bin/pip install -r test-requirements.txt
#endif
#	make clean



all: prebuild configuration setup
	

.PHONY: clean
