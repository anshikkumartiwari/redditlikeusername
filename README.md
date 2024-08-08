##Random pronounceable and cool username generator

This flask API generates generates a 4 letter pronounceable word, takes a word from the common words given to genrate 
one jja and one jjb type word form the external Datamuse API and then a adds 3 digits to complete the username.

## Endpoints

### GET /generate-username

Sending a GET request to this endpoint will return a JSON response containing a generated username.

#### Response

- `200 OK` on success
  ```json
  {
    "username": "womoBoldSwan123"
  }

- `200 OK` on failure
  ```json
  {
    "error": "Failed to fetch words from Datamuse API"
  }



Id you are running on your machine, the API will be accessible at http://localhost:5000/generate-username.
