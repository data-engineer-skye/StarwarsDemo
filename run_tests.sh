#!/bin/bash

# Set the virtual environment name
venv_dir="starwars_venv"

echo "Initializing."
python3 -m venv "$venv_dir" && source "$venv_dir/bin/activate"
echo "Using Venv: $(which python3)"

echo "Installing requirements."
pip3 install -r requirements.txt

echo "Starting tests for test_api folder"
pytest test_api

echo "Deactivating the virtual environment"
deactivate

echo "Script completed."



