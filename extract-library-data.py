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
# TODO: Let's default to today, today-365
start_date = '2024-09-01'
end_date = '2025-04-05'


# COMPONENTS
def component_actions_by_component():
    params = "/component/actions?group_by=component&start_date=" + start_date + "&end_date=" + end_date + "&order=asc"
    url     = base_url + file_key + params
    cursorurl = url
    headers = {'X-FIGMA-TOKEN' : figma_access_token}
    response = requests.get(url, headers=headers)
    # print(url)

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
    output.to_csv("output/component/component_actions_by_component.csv", encoding='utf-8',  index=False)

def component_actions_by_team():
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

    output.to_csv("output/component/component_actions_by_team.csv", encoding='utf-8',  index=False)

def component_usages_by_component():
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
    output.to_csv("output/component/component_usages_by_component.csv", encoding='utf-8',  index=False)

def component_usages_by_file():
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
    output.to_csv("output/component/component_usages_by_file.csv", encoding='utf-8',  index=False)


# VARIABLES
def variable_actions_by_variable():
    params = "/variable/actions?group_by=variable&start_date=" + start_date + "&end_date=" + end_date + "&order=asc"
    url     = base_url + file_key + params
    cursorurl = url
    headers = {'X-FIGMA-TOKEN' : figma_access_token}
    response = requests.get(url, headers=headers)
    print(url)

    output = pd.DataFrame()

    # This API paginates at 1000 rows, looping over it if result is >999
    while url:  
        json_data = response.json()
        normalisedRows = pd.json_normalize(json_data['rows'], meta=['week', 'variable_key', 'variable_name', 'detachments','insertions', 'collection_key', 'collection_name'])
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
    output.to_csv("output/variable/variable_actions_by_variable.csv", encoding='utf-8',  index=False)

def variable_actions_by_team():
    params = "/variable/actions?group_by=team&start_date=" + start_date + "&end_date=" + end_date + "&order=asc"
    url     = base_url + file_key + params
    cursorurl = url
    headers = {'X-FIGMA-TOKEN' : figma_access_token}
    response = requests.get(url, headers=headers)
    print(url)

    output = pd.DataFrame()

    # This API paginates at 1000 rows, looping over it if result is >999
    while url:  
        json_data = response.json()
        normalisedRows = pd.json_normalize(json_data['rows'], meta=['week', 'variable_key', 'variable_name', 'detachments','insertions', 'collection_key', 'collection_name'])
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
    output.to_csv("output/variable/variable_actions_by_team.csv", encoding='utf-8',  index=False)




def variable_usages_by_variable():
    params = "/variable/usages?group_by=variable&start_date=" + start_date + "&end_date=" + end_date + "&order=asc"
    url     = base_url + file_key + params
    cursorurl = url
    headers = {'X-FIGMA-TOKEN' : figma_access_token}
    response = requests.get(url, headers=headers)
    print(url)

    output = pd.DataFrame()

    # This API paginates at 1000 rows, looping over it if result is >999
    while url:  
        json_data = response.json()
        normalisedRows = pd.json_normalize(json_data['rows'], meta=['files_using', 'teams_using', 'usages' 'variable_key', 'variable_name', 'collection_key', 'collection_name'])
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
    output.to_csv("output/variable/variable_usages_by_variable.csv", encoding='utf-8',  index=False)




def variable_usages_by_file():
    params = "/variable/usages?group_by=file&start_date=" + start_date + "&end_date=" + end_date + "&order=asc"
    url     = base_url + file_key + params
    cursorurl = url
    headers = {'X-FIGMA-TOKEN' : figma_access_token}
    response = requests.get(url, headers=headers)
    print(url)

    output = pd.DataFrame()

    # This API paginates at 1000 rows, looping over it if result is >999
    while url:  
        json_data = response.json()
        normalisedRows = pd.json_normalize(json_data['rows'], meta=['usages' 'team_name', 'file_name', 'workspace_name'])
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
    output.to_csv("output/variable/variable_usages_by_file.csv", encoding='utf-8',  index=False)




# STYLES
def style_actions_by_style():
    params = "/style/actions?group_by=style&start_date=" + start_date + "&end_date=" + end_date + "&order=asc"
    url     = base_url + file_key + params
    cursorurl = url
    headers = {'X-FIGMA-TOKEN' : figma_access_token}
    response = requests.get(url, headers=headers)
    print(url)

    output = pd.DataFrame()

    # This API paginates at 1000 rows, looping over it if result is >999
    while url:  
        json_data = response.json()
        normalisedRows = pd.json_normalize(json_data['rows'], meta=['style_key', 'week', 'detachments','insertions', 'style_name', 'style_type' ])
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
    output.to_csv("output/style/style_actions_by_style.csv", encoding='utf-8',  index=False)


def style_actions_by_team():
    params = "/style/actions?group_by=team&start_date=" + start_date + "&end_date=" + end_date + "&order=asc"
    url     = base_url + file_key + params
    cursorurl = url
    headers = {'X-FIGMA-TOKEN' : figma_access_token}
    response = requests.get(url, headers=headers)
    print(url)

    output = pd.DataFrame()

    # This API paginates at 1000 rows, looping over it if result is >999
    while url:  
        json_data = response.json()
        normalisedRows = pd.json_normalize(json_data['rows'], meta=['week', 'detachments','insertions', 'team_name', 'workspace_name'])
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
    output.to_csv("output/style/style_actions_by_team.csv", encoding='utf-8',  index=False)





def style_usages_by_style():
    params = "/style/usages?group_by=style&start_date=" + start_date + "&end_date=" + end_date + "&order=asc"
    url     = base_url + file_key + params
    cursorurl = url
    headers = {'X-FIGMA-TOKEN' : figma_access_token}
    response = requests.get(url, headers=headers)
    print(url)

    output = pd.DataFrame()

    # This API paginates at 1000 rows, looping over it if result is >999
    while url:  
        json_data = response.json()
        normalisedRows = pd.json_normalize(json_data['rows'], meta=['files_using', 'teams_using', 'usages' 'style_key', 'style_name', 'style_type'])
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
    output.to_csv("output/style/style_usages_by_style.csv", encoding='utf-8',  index=False)




def style_usages_by_file():
    params = "/style/usages?group_by=file&start_date=" + start_date + "&end_date=" + end_date + "&order=asc"
    url     = base_url + file_key + params
    cursorurl = url
    headers = {'X-FIGMA-TOKEN' : figma_access_token}
    response = requests.get(url, headers=headers)
    print(url)

    output = pd.DataFrame()

    # This API paginates at 1000 rows, looping over it if result is >999
    while url:  
        json_data = response.json()
        normalisedRows = pd.json_normalize(json_data['rows'], meta=['usages' 'team_name', 'file_name', 'workspace_name'])
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
    output.to_csv("output/style/style_usages_by_file.csv", encoding='utf-8',  index=False)





def main():
    component_actions_by_component()
    component_actions_by_team()
    component_usages_by_component()
    component_usages_by_file()
    variable_actions_by_variable()
    variable_actions_by_team()
    variable_usages_by_variable()
    variable_usages_by_file()
    style_actions_by_style()
    style_actions_by_team()
    style_usages_by_style()
    style_usages_by_file()

if __name__ == "__main__":
    main()






