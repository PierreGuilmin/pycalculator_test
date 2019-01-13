#!/bin/bash

# This script installs and setups conda on a Travis CI Windows, Linux or Mac OSX virtual machine.
#
# References
# ----------
# https://conda.io/docs/user-guide/tasks/use-conda-with-travis-ci.html
# https://conda.io/docs/user-guide/install/macos.html#install-macos-silent
# https://conda.io/docs/user-guide/install/windows.html#installing-in-silent-mode
# https://chocolatey.org/packages/miniconda3

# exit the script if any command returns a non-zero status
set -e

if [[ "$TRAVIS_OS_NAME" == "osx" ]] || [[ "$TRAVIS_OS_NAME" == "linux" ]] ; then

    # install Miniconda
    echo "Installing Miniconda..."
    if [[ "$TRAVIS_OS_NAME" == "osx" ]]; then
        DOWNLOAD_LINK="https://repo.continuum.io/miniconda/Miniconda3-latest-MacOSX-x86_64.sh"
    else
        DOWNLOAD_LINK="https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh"
    fi
    wget "$DOWNLOAD_LINK" -O miniconda3.sh
    bash miniconda3.sh -b -p "$HOME/miniconda3"

else
    #choco install miniconda3 --params="'/InstallationType:JustMe /AddToPath:1 /RegisterPython:0'"
    choco install miniconda3 --params="'/AddToPath:1'"

fi

# configure Miniconda
echo "Configuring Miniconda..."
conda config --set always_yes true --set changeps1 false

# update Miniconda
echo "Updating Miniconda..."
conda update conda
conda info -a
