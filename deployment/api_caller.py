import requests

VITE_LOCALHOST="http://host.docker.internal:8000"



def fetch_task_counts(auth_token, workforce_id):
    headers = {
        "Authorization": auth_token
    }
    url = f"{VITE_LOCALHOST}/api-sileo/v4/hqzen/task-count/filter/?workforce_id={workforce_id}"
    response = requests.get(url, headers=headers)

    return response.json()