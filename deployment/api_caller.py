import requests
import urllib.parse

VITE_LOCALHOST="http://host.docker.internal:8000"
VITE_LOCALHOST="http://0.0.0.0:8000"



def fetch_task_counts(auth_token, workforce_id):
    headers = {
        "Authorization": auth_token
    }
    url = f"{VITE_LOCALHOST}/api-sileo/v4/hqzen/task-count/filter/?workforce_id={workforce_id}"
    response = requests.get(url, headers=headers)

    return response.json()

def fetch_shift_logs(auth_token, employment_id, shift_start):
    encoded_datetime = urllib.parse.quote(shift_start)
    headers = {
        "Authorization": auth_token
    }
    url = f"{VITE_LOCALHOST}/api-sileo/v4/timelogging/time-log/filter/?employment_id={employment_id}&shift_start={encoded_datetime}"
    response = requests.get(url, headers=headers)

    return response.json()


# print(fetch_shift_logs(
#     auth_token="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl9wayI6MTM1OTc0NCwiZXhwIjoxNzM3NzEzMzcwfQ.3rj_Rfg2qAAlwMIh_u004Ykl1eptVSqP-tIjUk4FKr8",
#     employment_id="7047",
#     shift_start="2025-01-17T00:00:00+08:00"
# ))
