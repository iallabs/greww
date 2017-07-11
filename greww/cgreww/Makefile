# CGrew Makefile


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

# VENV

_virtualenv:
	# create virtual env
	virtualenv _virtualenv
	_virtualenv/bin/pip install --upgrade pip
	_virtualenv/bin/pip install --upgrade setuptools

_use_env:
	# use virtual env
	source _virtualenv/bin/activate

binarizecppfile:
	@

runtests:
	@

cleanbincpp:
	rm -rf greww/cgreww/*.so

clean:
	rm -f MANIFEST
	rm -rf build dist


.PHONY: clean
