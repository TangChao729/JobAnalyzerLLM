from class_job_listing import JobListingService

if __name__ == '__main__':
    job_listing_service = JobListingService()

    query_title = "Data Scientist"
    # Example usage
    similar_titles_and_ids = job_listing_service.find_most_similar_titles(query_title, top_n=5)

    # Print the results
    for title, job_ids, score in similar_titles_and_ids:
        print(f"Title: {title}, Job IDs: {job_ids}, Similarity: {score}")