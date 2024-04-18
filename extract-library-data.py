import requests
import json
from dotenv import load_dotenv
import os
import pandas as pd

# Set env variables, using .env here
load_dotenv()
figma_access_token = os.getenv("FIGMA_ACCESS_TOKEN")
file_key = os.getenv("FILE_KEY") # something like '6p8e19mTHzCJfRfShcRH9K'

# Endpoint
base_url = 'https://api.figma.com/v1/analytics/libraries/'


# Set the dates 
start_date = '2024-01-01'
end_date = '2024-04-05'


# Actions by Component
def actions_by_component():
    params = "/actions?group_by=component&start_date=" + start_date + "&end_date=" + end_date + "&order=asc"
    url     = base_url + file_key + params
    cursorurl = url
    headers = {'X-FIGMA-TOKEN' : figma_access_token}
    response = requests.get(url, headers=headers)

    output = pd.DataFrame()

    # This API paginates at 1000 rows, looping over it if result is >999
    while url:  
        json_data = response.json()
        normalisedRows = pd.json_normalize(json_data['rows'], meta=['week', 'component_key', 'component_name', 'detachments','insertions'])
        output = pd.concat([output, normalisedRows])

        # check for another page and get it; if not, exit the loop
        if json_data['next_page']:
            cursorurl = url + "&cursor=" + json_data['cursor']
            print("Requesting next page: " + cursorurl)
            response = requests.get(cursorurl, headers=headers)
        else:
            print("No new data. we're done")
            url = ''

    # Export to CSV
    output.to_csv("output/actions_by_component.csv", encoding='utf-8',  index=False)

def actions_by_team():
    params = "/actions?group_by=team&start_date=" + start_date + "&end_date=" + end_date + "&order=asc"
    url     = base_url + file_key + params
    cursorurl = url
    headers = {'X-FIGMA-TOKEN' : figma_access_token}
    response = requests.get(url, headers=headers)
    output = pd.DataFrame()

    while url:  
        json_data = response.json()
        normalisedRows = pd.json_normalize(json_data['rows'], meta=['week', 'team_name', 'workspace_name', 'detachments','insertions'])
        output = pd.concat([output, normalisedRows])

        # check for another page and get it; if not, exit the loop
        if json_data['next_page']:
            cursorurl = url + "&cursor=" + json_data['cursor']
            print("Requesting next page: " + cursorurl)
            response = requests.get(cursorurl, headers=headers)
        else:
            print("No new data. we're done")
            url = ''

    output.to_csv("output/actions_by_team.csv", encoding='utf-8',  index=False)

def usages_by_component():
    params = "/usages?group_by=component&start_date=" + start_date + "&end_date=" + end_date + "&order=asc"
    url     = base_url + file_key + params
    cursorurl = url
    headers = {'X-FIGMA-TOKEN' : figma_access_token}
    response = requests.get(url, headers=headers)
    output = pd.DataFrame()

    # This API paginates at 1000 rows, looping over it if result is >999
    while url:  
        json_data = response.json()
        normalisedRows = pd.json_normalize(json_data['components'], meta=['component_key', 'component_name', 'num_instances', 'num_teams_using','num_files_using'])
        output = pd.concat([output, normalisedRows])

        # check for another page and get it; if not, exit the loop
        if json_data['next_page']:
            cursorurl = url + "&cursor=" + json_data['cursor']
            print("Requesting next page: " + cursorurl)
            response = requests.get(cursorurl, headers=headers)
        else:
            print("No new data. we're done")
            url = ''

    # Export to CSV
    output.to_csv("output/usages_by_component.csv", encoding='utf-8',  index=False)

def usages_by_file():
    params = "/usages?group_by=file&start_date=" + start_date + "&end_date=" + end_date + "&order=asc"
    url     = base_url + file_key + params
    cursorurl = url
    headers = {'X-FIGMA-TOKEN' : figma_access_token}
    response = requests.get(url, headers=headers)

    output = pd.DataFrame()

    # This API paginates at 1000 rows, looping over it if result is >999
    while url:  
        json_data = response.json()
        normalisedRows = pd.json_normalize(json_data['files'], meta=['team_name', 'workspace_name', 'file_name', 'num_instances'])
        output = pd.concat([output, normalisedRows])

        # check for another page and get it; if not, exit the loop
        if json_data['next_page']:
            cursorurl = url + "&cursor=" + json_data['cursor']
            print("Requesting next page: " + cursorurl)
            response = requests.get(cursorurl, headers=headers)
        else:
            print("No new data. we're done")
            url = ''

    # Export to CSV
    output.to_csv("output/usages_by_file.csv", encoding='utf-8',  index=False)


def main():
    actions_by_component()
    actions_by_team()
    usages_by_component()
    usages_by_file()


if __name__ == "__main__":
    main()






