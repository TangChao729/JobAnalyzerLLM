from openai import OpenAI
class GPTAgent:
    def __init__(self):
        self.default_key_path = './credentials/gpt_key.txt'
        try:
            self.reset_keys()
        except Exception as e:
            raise ValueError(f"Error initializing GPT Agent: {e}")
        
    #TODO: adding history to the generate_response method
    #TODO: adding count / limit to the generate_response method
    def generate_response(self, user_info, similar_job_description):
        completion = self.client.chat.completions.create(
        model="gpt-4o",
        response_format={ "type": "json_object" },
        messages=[
            {"role": "system", 
            "content": 
            '''
            You are a professional assistant, skilled in helping users improve their skills 
            by comparing user's resume and actual job listings. You provide information such 
            as what are the user's strengths when comparing with job listings, and what are 
            the user's weaknesses when comparing. You then provide suggestions on how the user 
            should improve themselves to meet the job requirements.
            Please respond in JSON format with the following structure: {\"Intro\": \"...\",\"Strengths\": \"...\",\"Weaknesses\": \"...\",\"Suggestions for Improvement\": \"...\",\"Conclusion\": \"...\"}
            '''
            },
            {"role": "user", 
            "content": 
            f"""
            Hi GPT, I have these experiences {user_info}. 
            Here is a list of possible matching job descriptions that I found: {similar_job_description}
            """
            },
        ]
        )

        #TODO: check response and return with Response object and status code
        return completion.choices[0].message.content

    def reset_keys(self, api_key=None):
        if api_key is None:
            with open(self.default_key_path, 'r') as f:
                api_key = f.read().strip()
        
        self.client = OpenAI(api_key=api_key)
        


