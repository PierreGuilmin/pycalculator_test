#!/bin/bash

# exit the script if any command returns a non-zero status
set -e

if [[ "$TRAVIS_OS_NAME" == "osx" ]] || [[ "$TRAVIS_OS_NAME" == "linux" ]] ; then
    # see https://conda.io/docs/user-guide/tasks/use-conda-with-travis-ci.html

    # install Miniconda
    echo "Installing Miniconda..."
    if [[ "$TRAVIS_OS_NAME" == "osx" ]]; then
        wget https://repo.continuum.io/miniconda/Miniconda3-latest-MacOSX-x86_64.sh -O miniconda.sh
    else
        wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh -O miniconda.sh
    fi
    bash miniconda.sh -b -p "$HOME/miniconda3"

else
    # see https://conda.io/docs/user-guide/install/windows.html#installing-in-silent-mode

    # install Miniconda
    echo "Installing Miniconda..."
    wget https://repo.continuum.io/miniconda/Miniconda3-latest-Windows-x86_64.exe -O miniconda.exe
    start /wait "" miniconda.exe /InstallationType=JustMe /AddToPath=0 /RegisterPython=0 /S /D=%UserProfile%\Miniconda3
fi

    # configure Miniconda
    echo "Configuring Miniconda..."
    conda config --set always_yes true --set changeps1 false

    # update Miniconda
    echo "Updating Miniconda..."
    conda update conda
    conda info -a
