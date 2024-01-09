# Job Analyzer LLM
![Build Status](https://img.shields.io/badge/Status-Active-green.svg)

## Description
* <img src="JAL.png" alt="drawing" width="100"/>
This project aims to provide a tool/service that provide a list of ideal job requirements/qualifications for a given job title. Some other features include:
- Provide a list of skills that are most relevant to the job title
- Comparing the job requirements/qualifications of two different job titles
- Given a list of skills, provide a list of job titles that are most relevant to the skills
- Analyze the given job title's career growth/path

## High Level Design
![High Level Design](Job%20Analyser.png)


## Key Components
* Guided User Input: User input but limited to a set of options, i.e. job title, skills, etc. This can be replaced by another LLM that can refine the user input.
  > * Web UI
  > * Input: Limit the user input to a set of options, with words limit, etc.
  > * Output: JSON object that contains the user input.

* Prompt Generator: Prompt templates. 
  > * TXT file

* Refined Prompt: Prompt templated filled with user input.
  > * Input: JSON object that contains the user input, and prompt template.
  > * Output: A long string that contains the user input.

* Web-crawler: Crawl job postings from job sites based on the user input.
  > * A web crawler that use several job sites as data sources.
  > * Input: Job title, location, etc.
  > * Output: A list of job postings.

* Matching classifier: Classify the job postings based on the user input.
  > * A binary classifier that can classify the job postings based on the user input.
  > * Input: A list of job postings, user input job title
  > * Output: A list of job postings that are relevant to the user input.

* Fetched Job Ads: A list of job ads that are relevant to the user input.
  > * A list of job postings that are relevant to the user input.

* JAL: Job Analyzer LLM takes the refined prompt and fetched job ads as input and output a list of job requirements/qualifications.
  > * A fine-tuned LLaMa 7b model that takes the refined prompt and fetched job ads as input and output a list of job requirements/qualifications.

* RAG & Cached DB: Additional data sources that can be used to further refine the job requirements/qualifications, and store the results for future use. For example, data drilling down to the job requirements/qualifications of a specific company.
  > * Additional features to be further explored.

