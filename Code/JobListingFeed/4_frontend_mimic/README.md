# A CLI text based user interface for the job search

app.py to start the CLI interface.


prompt message 1: "choose from the following options: 
1. search and analyze
2. exit"

if 1:
    prompt message 1.1: "choose from the following options:
    1. type in your experience
    2. read from a file"

    if 1:
        prompt message 1.1.1: "please type in your experience, qualification, skills, and desired job title"
        upon enter, send the input to the server for processing, using search endpoint

    if 2:
        prompt message 1.1.2: "please type in the file path"
        upon enter, read the file, send the input to the server for processing, using search endpoint

    display the search results
    prompt message 1.1.3: "below are the job listings that match your search query.
    1. job_1 content
    2. job_2 content
    3. ...
    "

    prompt message 1.1.4: "choose from the following options:
    1. read more about a job, type in the job number
    2. analyse the job listings

    if 1:
        showing the job content
        upon enter, return to prompt message 1.1.4

    if 2:
        upon enter, send the job listings to the server for processing, using compare endpoint

        display the analysis results

if 2: 
    prompt message 1.2: "exit the program"

