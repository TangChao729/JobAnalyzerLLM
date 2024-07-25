## With marqo database setup, we are ready to search through the job listings.

### backend workflow

1. Client sends a search request to the server.
   (data type: json object, example: {"title": "software engineer", "location": "san francisco", "resume": "I am a software engineer with 5 years of experience in python and java."})

2. Server processes the request, turn it into a marqo query, and sends it to the marqo database.
   (data type: jsonified string)

3. Marqo database processes the query and returns the results to the server.
   (data type: json object, with similarity score)

4. Server fetches job listings, along with user's search query, process them into a OpenAI API call, waiting for the response.
   (data type: )

5. Server receives the response and sends it back to the client.
   (data type: )

### backend code structure

1. `app.py`: main file for the backend server.
2. `marqo.py`: marqo database connection and query processing.
3. `openai.py`: OpenAI API call.
4. `job_listing.py`: job listing fetching and processing.
5. `utils.py`: utility functions.
6. `config.py`: configuration file.
7. `requirements.txt`: python package requirements.
8. `README.md`: backend documentation.
