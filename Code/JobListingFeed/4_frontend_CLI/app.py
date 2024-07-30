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
        user_experience, response = send_search_request(user_experience)
        handle_search_response(user_experience, response)
    elif choice == '2':
        file_path = input("Please type in the file path: ")
        try:
            with open("./dummy_resume/" + file_path + ".txt", 'r') as file:
                user_experience = file.read()
                user_experience, response = send_search_request(user_experience)
                handle_search_response(user_experience, response)
        except FileNotFoundError:
            print("File not found, please try again.")
            search_and_analyze()
    else:
        print("Invalid choice, please try again.")
        search_and_analyze()

def send_search_request(user_experience):
    search_payload = {"query": {"description": user_experience}}
    response = requests.post(f"{API_URL}/search", headers={"Content-Type": "application/json"}, data=json.dumps(search_payload))
    return user_experience, response

def handle_search_response(user_experience, response):
    if response.status_code == 200:
        search_results = response.json()['hits']
        print("Below are the job listings that match your search query:")
        for idx, job in enumerate(search_results, start=1):
            print(f"{idx}. {job.get('description')}")
        further_action(user_experience, search_results)
    else:
        print("An error occurred during the search. Please try again.")
        main_menu()

def further_action(user_experience, job_listings):
    print("Choose from the following options:")
    print("1. Read more about a job")
    print("2. Analyze the job listings")
    print("3. Go back to the main menu")
    choice = input("Enter your choice: ")
    if choice == '1':
        job_number = input("Enter the job number: ")
        try:
            job_number = int(job_number)
            if 1 <= job_number <= len(job_listings):
                print(f"Job {job_number} content: {job_listings[job_number - 1].get('description')}")
                further_action(user_experience, job_listings)
            else:
                print("Invalid job number, please try again.")
                further_action(user_experience, job_listings)
        except ValueError:
            print("Invalid input, please enter a number.")
            further_action(user_experience, job_listings)
    elif choice == '2':
        response = send_compare_request(user_experience, job_listings)
        handle_compare_response(response)
    elif choice == '3':
        main_menu()
    else:
        print("Invalid choice, please try again.")
        further_action(user_experience, job_listings)

def send_compare_request(user_experience, job_listings):
    compare_payload = {"user_info": user_experience,"similar_job_description": job_listings}
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