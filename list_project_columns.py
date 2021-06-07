#!/usr/bin/env python3
# Python script to list the columns in a given project ID

import os, sys, json, requests, yaml

# Color constants
# Reference: https://gist.github.com/chrisopedia/8754917
COLINFO="\033[0;35m"
COLRESET="\033[m"

baseurl = 'https://api.github.com'
headers = {"Content-Type": "application/json", "Accept": "application/vnd.github.inertia-preview+json"}

if len(sys.argv) != 3:
    print("   Usage: " + sys.argv[0] + " my-project-id org_name")
    sys.exit(1)

project_id = sys.argv[1]
org = sys.argv[2]
token = os.environ['GITHUB_API_TOKEN']

def list_project_columns():
    # Get list of all repos in an org
    response = requests.get(baseurl + "/projects/" + project_id + "/columns", 
        headers=headers, 
        auth=(org, token))
    if response.status_code != 200:
        # An error occured
        print(COLINFO + "Error getting project columns : " + str(response.status_code) + " " + response.text
        + COLRESET)

    # Convert repos to YAML
    json_projects = json.loads(response.text)
    #print(json.dumps(json_project, indent=4, sort_keys=True))
    for project in json_projects:
        print(f'{project["id"]} {project["name"]}')
        
list_project_columns()