#!/bin/bash
cd app
poetry shell

# Run each python script
for filename in *.py; do
    python "$filename"
done


