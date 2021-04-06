#!/usr/bin/python
# -*- coding: cp1252 -*-

# coding: utf-8

# In[197]:


import os
import pandas as pd
import sys
import csv
import glob
import shutil
import ntpath



#you don't need this function
def combine_file(*file_input):
    list_of_data = []
   # reader = [csv.reader(file_input)]
    #for i in reader:
       # df = pd.read_csv(i)
       # list_of_data.append(df)

    for file in file_input:
        with open(file, 'rb') as f:
            df = pd.read_csv(f, error_bad_lines= False)
            list_of_data.append(df)





    # convert csv_file to data frame
    #file_in = get_list_csv(file_input)
    #read the file to make it to dataframe
    #list_of_data = [pd.read_csv(file) for file in file_in]

    # zip to look through the both dataframe and the files
    # (dataframe1, file1), (datafram2, file2)...
    # create the new column by df['filename'] = name

    for df, file in zip(list_of_data, file_input):
        file_path = strip_path(file)
        df['filename'] = file_path

    combined = pd.concat(list_of_data)

    
    return combined



 #strip the path from the csv file for filename   
def strip_path(path):
    head, tail = ntpath.split(path)
    return tail or ntpath.basename(head)

def new_csv_file(df, file_out):
    #new_dataframe = combine_file(file_in)
    new_file = df.to_csv(file_out, index= False, encoding='utf-8-sig')
    return new_file


def write_csv(file_out):
    with open(file_out) as f:
        reader = csv.reader(f)
        writer = csv.writer(sys.stdout)
        writer.writerows(reader)
        f.close()

def move_to_new_folder(file_out, original,target):
    new_list = get_list_csv(original)
    for i in new_list:
        if i == file_out:
            return shutil.move(i, target)




def main(argv):
    #file_in = (args[1:])



    # list_file
    #get_list_csv(args[1:])
    # new combined dataframe
  
   
      
    # create combined csv file

    #new_csv_file(args[-1])
    #move_to_new_folder(file_out, original,target)
    #file_in = args[1:2]
    #file_out = args[-1]
    
    file_ins = argv[1:]
    file_out = "new.csv"
    list_of_data = []
    for file  in file_ins:
        with open(file, 'rb') as f:
            df = pd.read_csv(f, error_bad_lines= False)
            list_of_data.append(df)

    for df, file in zip(list_of_data, file_ins):
        file_path = strip_path(file)
        df['filename'] = file_path

    combined = pd.concat(list_of_data)

   # df = combine_file(file_ins)
    new_csv_file(combined ,file_out)
    write_csv(file_out)
    os.remove(file_out)




if __name__ == "__main__":
    main(sys.argv)
#paths where csv are in










