##Example of running this script:
##python process_data.py disaster_messages.csv disaster_categories.csv DisasterResponse.db

import sys
import pandas as pd
from sqlalchemy import create_engine


def load_data(messages_filepath, categories_filepath):
    '''Read in input csv files'''
    messages = pd.read_csv(messages_filepath)
    categories = pd.read_csv(categories_filepath)
    df = messages.merge(categories, on = 'id')
    return df


def clean_data(df):
    '''Split Categoties column into seperate category columns.
    Then convert category values to just numbers 0 or 1.
    Then concatenate new category matrix and remove duplicate rows.
    '''
    #create a dataframe of the 36 individual category columns
    categories = df.categories.str.split(';', expand = True)
    #Use first row to get all categories and update column names
    row = categories.iloc[0]
    category_colnames = [x.split('-')[0] for x in row]
    # rename the columns of `categories`
    categories.columns = category_colnames
    
    #Convert category valies to numbers: 0 and 1.
    for column in categories:
        categories[column] = categories[column].str.split('-').str[1]
        categories[column] = pd.to_numeric(categories[column])

    #Replace 2 to 1
    categories.replace(2,1, inplace = True)   

    # drop the original categories column from `df` and concatenate category matrix
    df.drop(columns=['categories'], inplace=True)
    df = pd.concat([df, categories], axis=1)

    #Remove duplicate rows
    df.drop_duplicates(inplace=True)

    return df



def save_data(df, database_filename):
    '''Save the cleaned dataset into an sqlite database'''
    engine = create_engine('sqlite:///' + database_filename)
    df.to_sql('DisasterResponse', engine, index=False, if_exists = 'replace')


def main():
    if len(sys.argv) == 4:

        messages_filepath, categories_filepath, database_filepath = sys.argv[1:]

        print('Loading data...\n    MESSAGES: {}\n    CATEGORIES: {}'
              .format(messages_filepath, categories_filepath))
        df = load_data(messages_filepath, categories_filepath)

        print('Cleaning data...')
        df = clean_data(df)
        
        print('Saving data...\n    DATABASE: {}'.format(database_filepath))
        save_data(df, database_filepath)
        
        print('Cleaned data saved to database!')
    
    else:
        print('Please provide the filepaths of the messages and categories '\
              'datasets as the first and second argument respectively, as '\
              'well as the filepath of the database to save the cleaned data '\
              'to as the third argument. \n\nExample: python process_data.py '\
              'disaster_messages.csv disaster_categories.csv '\
              'DisasterResponse.db')


if __name__ == '__main__':
    main()
