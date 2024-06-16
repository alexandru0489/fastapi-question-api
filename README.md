# FastAPI Questions API

## Overview
This API allows querying and managing a database of questions for use in questionnaires.

### Endpoints
- **GET /questions/**: Retrieve a list of questions.
- **POST /questions/**: Create a new question (admin only).

### Authentication
Basic authentication is used with the following users:
- alice: wonderland
- bob: builder
- clementine: mandarine

Admin user:
- username: admin
- password: 4dm1N

### Running the API
1. Install dependencies: `pip3 install -r requirements.txt`
2. Start the server: `uvicorn app.main:app --reload`
3. Test the API: `./test_api.sh`
