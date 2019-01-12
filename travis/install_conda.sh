#!/bin/bash

# exit the script if any command returns a non-zero status
set -e

if [[ "$TRAVIS_OS_NAME" == "osx" ]] || [[ "$TRAVIS_OS_NAME" == "linux" ]] ; then
    # see https://conda.io/docs/user-guide/tasks/use-conda-with-travis-ci.html

    # install Miniconda
    echo "Installing Miniconda..."
    if [[ "$TRAVIS_OS_NAME" == "osx" ]]; then
        curl https://repo.continuum.io/miniconda/Miniconda3-latest-MacOSX-x86_64.sh -o miniconda.sh
    else
        wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh -O miniconda.sh
    fi
    bash miniconda.sh -b -p "$HOME/miniconda3"
    export PATH="$HOME/miniconda3/bin:$PATH"

    # configure Miniconda
    echo "Configuring Miniconda..."
    conda config --set always_yes true --set changeps1 false

    # update Miniconda
    echo "Updating Miniconda..."
    conda update conda
    conda info -a

else
    echo "Oups..."
    exit 1
fi
