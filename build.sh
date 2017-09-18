#!/bin/bash

GREWW_PATH="$PWD"
GREWW_VERSION="0.0.1"
GREWW_CACHE="$GREWW_PATH/cache"

function expmk () {
    export GREWW_PATH
    export GREWW_VERSION
    export GREWW_CACHE
}

function make_babtu_cfg () {
    python3 ial-pkg-sos.py --clone skmvs -p
    python3 ial-pkg-sos.py --build skmvs -bo export-vars
}

function make_cache () {
    if [ ! -d $GREWW_CACHE ]; then
        mkdir GREWW_CACHE
    fi
}

function build_skmvs_env () {
    GREWW_BUILD_ENV="$GREWW_PATH/build_env.py"
    python3 $GREWW_BUILD_ENV
}

function make_py_package () {
    GREWW_PY_SETUP="$GREWW_PATH/setup.py"
    python3 $GREWW_PY_SETUP install
}

function test_py_package () {
    GREWW_PY_SETUP="GREWW_PATH/setup.py"
    python3 $GREWW_PY_SETUP test
}

cmd=$1
option=$2

if [ "$cmd" = "build" ]; then
    if [ "$option" = "--no-setup" ]; then
        expmk
        build_skmvs_env
    elif [ "$option" = "--new-cache" ]; then
        expmk
        build_skmvs_env
        rm -rf $GREWW_CACHE
        make_cache
        make_py_package
    else
        expmk
        build_skmvs_env
        make_py_package
    fi
fi

if [ "$cmd" = "test" ]; then
    test_py_package
fi
