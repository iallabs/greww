#!/bin/bash

GREWW_PATH="$PWD"
GREWW_VERSION="0.0.5"
GREWW_CACHE="$GREWW_PATH/cache"
GREWW_CONFIG="$GREWW_PATH/pkg/config"
export GREWW_PATH
export GREWW_VERSION
export GREWW_CACHE
export GREWW_CONFIG

function __unset_env () {
    unset GREWW_PATH
    unset GREWW_VERSION
    unset GREWW_CACHE
    unset GREWW_CONFIG
}

function make_cache () {
    if [ ! -d $GREWW_CACHE ]; then
        mkdir $GREWW_CACHE
    fi
}

function make_py_package () {
    GREWW_PY_SETUP="$GREWW_PATH/setup.py"
    sudo python3 $GREWW_PY_SETUP install
    RS=$?
    return RC
}

function test_py_package () {
    GREWW_PY_SETUP="$GREWW_PATH/setup.py"
    coverage run $GREWW_PY_SETUP test
    RS=$?
    return RC
}

function clear_cache () {
    rm -rf $GREWW_CACHE/*
}

cmd=$1
option=$2

if [ "$cmd" = "--build" ]; then
    make_cache
    if [ "$option" = "--clear-cache"]; then
        clear_cache
    fi
    make_py_package
    echo "[ OK ] ... Build success"
    exit 0
elif [ "$cmd" = "--test" ]; then
    test_py_package
    echo "[ OK ] ... End tests"
elif [ "$cmd" = "--test-noscop" ]; then
    __unset_env
    test_py_package
    echo "[ OK ] ... End no scop tests"
elif [ "$cmd" = "--clear-cache" ];then
    clear_cache
    echo "[ OK ] ... Clear cache"
fi
