#!/bin/bash

# Check if the correct number of arguments are provided
if [ "$#" -ne 7 ]; then
    echo "Usage: $0 <API_KEY> <ENGAGEMENT_ID> <SCAN_TYPE> <FILE_PATH> <DOJO_INSTANCE_URL>"
    exit 1
fi

# Assign input arguments to variables
API_KEY=$1
ENGAGEMENT_ID=$2
SCAN_TYPE=$3
FILE_PATH=$4
DOJO_INSTANCE_URL=$5
PRODUCT_NAME=$6
ENGAGEMENT_NAME=$7

# Perform the curl command
curl -X POST "${DOJO_INSTANCE_URL}/api/v2/reimport-scan/" \
-H "Authorization: Token ${API_KEY}" \
-H "Content-Type: multipart/form-data" \
-F "product_name=${PRODUCT_NAME}" \
-F "engagement=${ENGAGEMENT_ID}" \
-F "scan_type=${SCAN_TYPE}" \
-F "engagement_name=${ENGAGEMENT_NAME}"
-F "file=@${FILE_PATH}"

# Check if the curl command was successful
if [ $? -eq 0 ]; then
    echo "Report successfully uploaded to DefectDojo."
else
    echo "Failed to upload report to DefectDojo."
    exit 1
fi
