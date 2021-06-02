import pandas as pd
import dateutil.parser
import isodate
import os
import easygui
import re
cwd = os.getcwd()

def loading_recipes(path):
    'function to load the recipes json file'
    try:
        recipes = pd.read_json(path, lines=True)
        print('the recipes were imported')
        return recipes
    except:
        print('error with the imporing of the recipes')
        return None

def get_difficulty(df,cwd):
    'gets the difficutly level'
    for key, value in df['TotalTime'].iteritems():
        if value > 0:
            if value > 60:
                df.at[key, 'difficulty'] = 'Hard'
            elif value > 30:
                df.at[key, 'difficulty'] = 'Medium'
            elif value > 0:
                df.at[key, 'difficulty'] = 'Easy'
        else:
          df.at[key, 'difficulty'] = 'Unkown'

    df.to_csv(os.path.join(cwd, 'chilies_and_difficutly.csv')) 
    return df



def main():
    'this is the main function to store all the necessary transformations'
    print('Please select the file with the recipes')
    path = easygui.fileopenbox()
    recipes = loading_recipes(path)
    cwd = os.getcwd()
    chilies = recipes[recipes['ingredients'].str.contains(r'chil(?!$)')]
    for index, duration in chilies['prepTime'].iteritems():
      if not duration.strip():
        chilies['prepTime'][index] = 0
      else:
        dur=isodate.parse_duration(duration)
        chilies['prepTime'][index] = int(dur.total_seconds()//60)

    for index, duration in chilies['cookTime'].iteritems():
      if not duration.strip():
        chilies['cookTime'][index] = 0
      else:
        dur=isodate.parse_duration(duration)
        chilies['cookTime'][index] = int(dur.total_seconds()//60)

    chilies['TotalTime'] = chilies['cookTime'] + chilies['prepTime']
    chilies_with_diff = get_difficulty(chilies,cwd)

#executes the above code
if __name__ == "__main__":
    main()