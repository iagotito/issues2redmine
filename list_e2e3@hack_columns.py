#!/usr/bin/env python3
# Python script to list the columns in a given project ID

import sys
from atdumpmemex import list_memex_columns

project_id = "011:ProjectNext3594"

print(f'Project ID: {project_id}')
list_memex_columns(project_id)