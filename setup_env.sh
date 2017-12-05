#!/usr/bin/env bash
# Create a virtual environment
PY36=$(ls /usr/bin/|grep -c python3.6)
ENV="env"

if [ ${PY36} -gt 0 ]; then
    python3 -m venv ${ENV}
else
    virtualenv ${ENV}
fi

# Activate virtual environment
source ${ENV}/bin/activate

# Install requirements
pip3 install -r requirements.txt

