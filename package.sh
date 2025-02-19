#!/bin/bash

ZIP_FILE=lambda_package.zip

echo "Creating ZIP package..."
zip -r $ZIP_FILE package lambda_function.py

echo "Lambda package created successfully: $ZIP_FILE"