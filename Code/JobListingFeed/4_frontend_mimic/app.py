import requests
import json

API_URL = "http://localhost:8888"

def main_menu():
    print("Choose from the following options:")
    print("1. Search and analyze")
    print("2. Exit")
    choice = input("Enter your choice: ")
    if choice == '1':
        search_and_analyze()
    elif choice == '2':
        print("Exiting the program.")
        exit()
    else:
        print("Invalid choice, please try again.")
        main_menu()

def search_and_analyze():
    print("Choose from the following options:")
    print("1. Type in your experience")
    print("2. Read from a file")
    choice = input("Enter your choice: ")
    if choice == '1':
        user_experience = input("Please type in your experience, qualification, skills, and desired job title: ")
        response = send_search_request(user_experience)
        handle_search_response(response)
    elif choice == '2':
        file_path = input("Please type in the file path: ")
        try:
            with open(file_path, 'r') as file:
                user_experience = file.read()
                response = send_search_request(user_experience)
                handle_search_response(response)
        except FileNotFoundError:
            print("File not found, please try again.")
            search_and_analyze()
    else:
        print("Invalid choice, please try again.")
        search_and_analyze()

def send_search_request(user_experience):
    search_payload = {"query": user_experience}
    response = requests.post(f"{API_URL}/search", headers={"Content-Type": "application/json"}, data=json.dumps(search_payload))
    return response

def handle_search_response(response):
    if response.status_code == 200:
        search_results = response.json()
        print("Below are the job listings that match your search query:")
        for idx, job in enumerate(search_results.get('jobs', []), start=1):
            print(f"{idx}. {job}")
        further_action(search_results.get('jobs', []))
    else:
        print("An error occurred during the search. Please try again.")
        main_menu()

def further_action(job_listings):
    print("Choose from the following options:")
    print("1. Read more about a job")
    print("2. Analyze the job listings")
    choice = input("Enter your choice: ")
    if choice == '1':
        job_number = input("Enter the job number: ")
        try:
            job_number = int(job_number)
            if 1 <= job_number <= len(job_listings):
                print(f"Job {job_number} content: {job_listings[job_number - 1]}")
                further_action(job_listings)
            else:
                print("Invalid job number, please try again.")
                further_action(job_listings)
        except ValueError:
            print("Invalid input, please enter a number.")
            further_action(job_listings)
    elif choice == '2':
        response = send_compare_request(job_listings)
        handle_compare_response(response)
    else:
        print("Invalid choice, please try again.")
        further_action(job_listings)

def send_compare_request(job_listings):
    compare_payload = {"similar_jobs": job_listings}
    response = requests.post(f"{API_URL}/compare", headers={"Content-Type": "application/json"}, data=json.dumps(compare_payload))
    return response

def handle_compare_response(response):
    if response.status_code == 200:
        compare_results = response.json()
        print("Analysis results:")
        print(json.dumps(compare_results, indent=4))
    else:
        print("An error occurred during the analysis. Please try again.")
    main_menu()

if __name__ == "__main__":
    main_menu()