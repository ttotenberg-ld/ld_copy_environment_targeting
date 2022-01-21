from utils.apiHandler import checkRateLimit as api_call
import json


'''
Set your LaunchDarkly instance information here
'''
API_KEY = "YOUR_API_KEY"
PROJECT_KEY = "YOUR_PROJECT_KEY"
SOURCE_ENVIRONMENT = "SOURCE_ENVIRONMENT_KEY" # The environment we're copying FROM
DESTINATION_ENVIRONMENT = "DESTINATION_ENVIRONMENT_KEY" # The environment we're copying TO


'''
Define API call information
'''
flag_list_url = f'/flags/{PROJECT_KEY}'

flag_copy_body = json.dumps({
  "source": {
    "key": SOURCE_ENVIRONMENT
  },
  "target": {
    "key": DESTINATION_ENVIRONMENT
  },
  "includedActions": [
    "updateOn",
    "updatePrerequisites",
    "updateTargets",
    "updateRules",
    "updateFallthrough",
    "updateOffVariation"
  ]
})


def get_flag_list():
    response = api_call("GET", flag_list_url, API_KEY, {}).json()
    response_list = response['items']
    number_of_flags = len(response_list)
    flag_list = []

    for i in range(number_of_flags):
        flag_list.append(response['items'][i]['key'])
    
    return flag_list


def copy_all_flag_targets():

    flag_list = get_flag_list()

    for i in flag_list:
        flag_copy_url = f'/flags/{PROJECT_KEY}/{i}/copy'

        print(f"Trying at url {flag_copy_url}")
        response = api_call("POST", flag_copy_url, API_KEY, flag_copy_body)
        print(f"Successfully copied settings for {i}")

if __name__ == "__main__":
    copy_all_flag_targets()