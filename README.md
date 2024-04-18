## Figma Library Analytics API Examples

A simple Python script demonstrating the Figma Library Analytics API to extract data to a CSV. In a more mature data pipeline, this could instead be inserted directly into a Data Warehouse such as Snowflake or BigQuery.


## Prerequisites

To use the Figma Library Analytics API  workflow, you must be a full member of an Enterprise org in Figma. 

You'll also need to install the following Python packages using `pip`:  
`pip3 install requests`  
`pip3 install python-dotenv`  
`pip3 install pandas`


## Usage

Define two environment variables in your .env file(see [Python dotenv](https://pypi.org/project/python-dotenv/) if you're new to this)
- **FIGMA_ACCESS_TOKEN:** This is your unique Figma Personal Access Token. It can be generated from Settings-Account-Personal access tokens. You will need to generate a new token to inherit the new `Library Analytics` permissions.
- **FILE_KEY:** The file key you wish to connect to. This is found in the Figma URL after `file/`

Addtionally, define the start and end dates in the script. Figma stores 365 days worth of data.

Then run `python3 extract-library-data.py` on the command line. 

By default this will create four CSV files in `output/` for the given date range:
 -actions by componant  
 -actions by team
 -usages by component
 -usages by file
