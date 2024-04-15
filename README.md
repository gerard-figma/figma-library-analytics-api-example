## Figma Library Analytics API Examples

A simple Python script demonstrating the Figma Library Analytics API to extract data to a CSV. In a more mature data pipeline, this could instead be inserted directly into a Data Warehouse such as Snowflake or BigQuery.


## Prerequisites

To use the Figma Library Analytics API  workflow, you must be a full member of an Enterprise org in Figma. 


## Usage

Define three environment variables in your .env file (or at the top of the file if you're ok with that)
- API_TOKEN: This is your unique Figma Personal Access Token
- FIGMA_URL: This is the APIs base URL - 'https://api.figma.com/v1/analytics/libraries/' (Check before release)
- FILENAME: The filename you wish to connect to

Addtionally, define the start and end dates in the script.

Then run `python3 extract-library-data.py` on the command line. 

By default this will create four CSV files in `output/` for the given date range:
 -actions by componant  
 -actions by team
 -usages by component
 -usages by file
