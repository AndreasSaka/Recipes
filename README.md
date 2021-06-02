## OPSBI_python_test

Contains simple transformations of data related to recipes


## Requirements

The user is required to install the following
>!pip install isodate
>!pip install python-dateutil
>!pip install easygui

## Libraries
>import json
>import pandas as pd
>import dateutil.parser
>import isodate
>import easygui

## Run the file
Before executing the newrecipes.py it is necessary to execute the setup.py.

	1) Navigate with the cmd to the folder with the my test files.
	
	2) Run in the cmd python setup.py 
	
	3) Run in the cmd python newrecipes.py
	
This .py file is used to perform transformations on the recipes .json file.
The .py file can be runned from cmd with the command python newrecipes.py
The user will be prompted to select the recipes.json from the file they have saved it with a gui.
The outcome will be stored in the users default folder.