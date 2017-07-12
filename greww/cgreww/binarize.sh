#!/bin/bash

# this script make cpp binaries under the same direction
#FIXME: Cleanup & same direction writing
#

CPP_EXTENSION=".cpp"
BIN_CPP_EXTENSION=".so"


CppBin () {
    g++ -shared -o $1 $2
}

SmartCppBin () {
    namef=$1
    filename=$(basename $namef)
    nameonly="${filename%.*}"
    if [ $2 ]; then
        binfile="$2/$nameonly$BIN_CPP_EXTENSION"
        echo "Making ............ $binfile"
    else
        binfile="$nameonly/$BIN_CPP_EXTENSION"
    fi
    CppBin $binfile $namef
}


tobincppdirectory () {
	for f in $1/*$CPP_EXTENSION; do
      echo ""
      echo "binarizing $f"
			SmartCppBin $f $2
	done
}

cleanupbinaries () {
    echo ""

}


if [ -d "$1" ]; then
    echo "found $1"
    echo "Start binarisation"
    tobincppdirectory $1
else
    echo "Directory not found"
fi

LIB="$1/lib"
TESTS="$1/tests"

if [ -e $LIB ]; then
  echo "found $LIB"
  echo "Start binarisation"
  tobincppdirectory $LIB $LIB
else
  echo "$LIB not found"
fi

if [ -e $TESTS ]; then
  echo "found $TESTS"
  echo "Start binarisation"
  tobincppdirectory $TESTS $TESTS
else
  echo "$TESTS not found"
fi


exit 0
