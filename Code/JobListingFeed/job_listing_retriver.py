import numpy as np
from sentence_transformers import SentenceTransformer, util
import pandas as pd
import json

'''
This module is used to retrive job listings, based on the search criteria, from 
a sample database.

Input: title, location, experience
Output: job listings json
'''



def get_job_listing():
    pass

def load_dataset():
    pass

def find_most_similar_titles(query_title, title_embeddings, unique_titles):
    # Encode the query title
    query_embedding = model.encode(query_title, convert_to_tensor=True)
    
    # Compute cosine similarities
    cosine_scores = util.pytorch_cos_sim(query_embedding, title_embeddings)[0]

    # Find the highest scores
    top_results = np.argpartition(-cosine_scores, range(20))[:20]

    # Return the top 20 most similar titles
    return [(unique_titles[index], cosine_scores[index].item()) for index in top_results]

# testing
if __name__ == '__main__':
    # Load the dataset
    dataset = load_dataset()

    # Extract the titles
    titles = [job['title'] for job in dataset]

    # Extract the unique titles
    unique_titles = list(set(titles))

    # Encode the titles
    title_embeddings = model.encode(unique_titles, convert_to_tensor=True)

    # Find the top 20 most similar titles
    similar_titles = find_most_similar_titles('Software Engineer', title_embeddings, unique_titles)

    # Print the result
    print(similar_titles)