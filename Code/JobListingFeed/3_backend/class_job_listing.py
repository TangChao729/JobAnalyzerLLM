import numpy as np
from sentence_transformers import SentenceTransformer, util
import pandas as pd
from collections import defaultdict
import re

class JobListingService:
    def __init__(self):
        self.model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
        self.job_dataset = self.load_dataset()
        self.clean_location(self.job_dataset)
        self.title_embeddings, self.unique_titles, self.title_to_job_ids = self.prepare_embeddings()

    def load_dataset(self):
        job_dataset_path = '../../../Data/job_listing_kaggle_dataset/job_postings.csv'
        job_dataset = pd.read_csv(job_dataset_path)
        return job_dataset

    def clean_location(self, job_dataset):
        # Define the regex pattern to match "city, state" or "United States"
        pattern = re.compile(r"[a-zA-Z\s]*,[A-Z]*|[Uu]nited [Ss]tates")

        # Create a new column to store the cleaned location
        job_dataset['cleaned_location'] = None

        # create a new column to store the cleaned location
        for i in range(len(job_dataset)):
            location = job_dataset['location'][i]
            if not pattern.match(location):
                location = 'United States'
            
            # create a new column to store the cleaned location
            job_dataset.loc[i, 'cleaned_location'] = location

    def prepare_embeddings(self):
        # Your code to prepare embeddings
        # Create a mapping from titles to a list of job IDs
        title_to_job_ids = defaultdict(list)
        for i in range(len(self.job_dataset)):
            title = self.job_dataset['title'][i]
            job_id = self.job_dataset['job_id'][i]
            title_to_job_ids[title].append(job_id)

        # Assume `unique_titles` is a list of unique job titles from your dataset
        unique_titles = list(set(self.job_dataset['title']))  # Remove duplicates

        # Generate embeddings for all unique titles
        title_embeddings = self.model.encode(unique_titles, convert_to_tensor=True)

        return title_embeddings, unique_titles, title_to_job_ids

    def find_most_similar_titles(self, query_title, top_n=20):
        # Encode the query title
        query_embedding = self.model.encode(query_title, convert_to_tensor=True)
        
        # Compute cosine similarities
        cosine_scores = util.pytorch_cos_sim(query_embedding, self.title_embeddings)[0]

        # Find the highest scores
        top_indices = np.argpartition(-cosine_scores, range(top_n))[:top_n]

        # Retrieve the corresponding titles and their job IDs
        similar_titles_and_ids = [(self.unique_titles[index], self.title_to_job_ids[self.unique_titles[index]], cosine_scores[index].item()) for index in top_indices]

        return similar_titles_and_ids

