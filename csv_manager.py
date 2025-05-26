import pandas as pd 
import os

file_route =  'data/expenses.csv'

#we create the columns we are gonna use for our dicionary
expenses_columns = ['id', 'name', 'amount', 'category', 'time', 'description']


#I created a initiator to verify if the file to save the expenses exists, in case this file doesn't exists it creates one

def initiator():
    if not os.path.exists(file_route):
        #converts the diccionary into a dataframe and then into csv file using pandas 
        pd.DataFrame(columns=expenses_columns).to_csv(file_route, index=False)
        


#reads the archive to see the actual data
def read_csv():
   return pd.read_csv(file_route)


#this def is to save new data

def save_data(dict_on_main):
    df = read_csv()
    #establish a new index 
    new_id = df['id'].max() + 1 if not df.empty else 1
    dict_on_main['id'] = new_id
    new = pd.DataFrame([dict_on_main])
    new =  new[expenses_columns]
    finished_df = pd.concat([df,new], ignore_index=True)
    finished_df.to_csv(file_route, index=False)
    

    

    



