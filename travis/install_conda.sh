#!/bin/bash

# This script installs conda on a Travis CI Windows, Linux or Mac OSX virtual machine.
#
# References
# ----------
# https://conda.io/docs/user-guide/tasks/use-conda-with-travis-ci.html
# https://conda.io/docs/user-guide/install/macos.html#install-macos-silent
# https://conda.io/docs/user-guide/install/windows.html#installing-in-silent-mode

# exit the script if any command returns a non-zero status
set -e

if [[ "$TRAVIS_OS_NAME" == "osx" ]] || [[ "$TRAVIS_OS_NAME" == "linux" ]] ; then

    # install Miniconda
    echo "Installing Miniconda..."
    if [[ "$TRAVIS_OS_NAME" == "osx" ]]; then
        wget https://repo.continuum.io/miniconda/Miniconda3-latest-MacOSX-x86_64.sh -O miniconda3.sh
    else
        wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh -O miniconda3.sh
    fi
    bash miniconda3.sh -b -p "$HOME/miniconda3"

else
    choco install miniconda3

    # install Miniconda
    # echo "Installing Miniconda..."
    # Miniconda3-4.5.12-Windows-x86_64.exe  
    # wget -nv https://repo.continuum.io/miniconda/Miniconda3-latest-Windows-x86_64.exe -O miniconda3.exe
    # echo "Start..."
    # start /wait "" .\miniconda3.exe /InstallationType=JustMe /AddToPath=0 /RegisterPython=0 /S /D=.\
    # echo "Done!"

fi

# configure Miniconda
echo "Configuring Miniconda..."
conda config --set always_yes true --set changeps1 false

# update Miniconda
echo "Updating Miniconda..."
conda update conda
conda info -a
