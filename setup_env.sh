#!/usr/bin/env bash
# Create a virtual environment
virtualenv env

# Activate virtual environment
source env/bin/activate

# Install requirements
pip install -r requirements.txt




##!/usr/bin/env bash
#PY36=$(ls /usr/bin/|grep -c python3.6)
#ENV="env"
#
#if [ ${PY36} -gt 0 ]; then
#    python3 -m venv ${ENV}
#else
#    virtualenv ${ENV}
#fi
#
#source ${ENV}/bin/activate
#pip3 install -r requirements.txt