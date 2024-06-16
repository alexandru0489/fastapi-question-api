#!/bin/bash

# Base URL for the API
BASE_URL="http://127.0.0.1:8000"

# Function to check if the server is up and running
# function wait_for_server() {
#   until $(curl --output /dev/null --silent --head --fail $BASE_URL); do
#     printf '.'
#     sleep 1
#   done
#   echo "Server is up and running"
# }

# # Wait for the server to be up and running
# wait_for_server

# Test the create_question endpoint with the provided question data
echo "Inserting test question"
curl -u admin:4dm1N -X 'POST' \
  "$BASE_URL/questions/" \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "question": "Cassandra and HBase are databases",
  "subject": "Databases",
  "correct": "C",
  "use": "Positioning test",
  "responseA": "relational database",
  "responseB": "object-oriented",
  "responseC": "column-oriented",
  "responseD": "graph-oriented"
}'

# Test the create_question endpoint
echo "Testing create_question endpoint"
curl -u admin:4dm1N -X 'POST' \
  "$BASE_URL/questions/" \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "question": "What is the capital of France?",
  "subject": "geography",
  "correct": "Paris",
  "use": "test",
  "responseA": "Paris",
  "responseB": "London",
  "responseC": "Berlin",
  "responseD": "Madrid"
}'