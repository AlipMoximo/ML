#Import required libraries
import pandas as pd
import openpyxl

# Load excel file.
file_path = ('HIV_Epidemiology_Children_Adolescents_2023 (2).xlsx')

#Load excel file into panda dataframe
df=pd.read_excel(file_path,sheet_name = 'Data')
# print(df.columns)


#Select only data specific to Uganda and Save new 
uganda_df = df[df['Country/Region'] == 'Uganda']
#print(uganda_df.columns)

#clean data.. check for empty fields, check for duplicates and modify the
empty_fields = uganda_df.isna().sum()
duplicate_rows = uganda_df.duplicated().sum()
# print(empty_fields)-> No empty fields from Ugandan selection
print(duplicate_rows)

