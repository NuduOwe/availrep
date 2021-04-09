import pandas as pd
import json
import datetime

import matplotlib.pyplot as plt
from PIL import Image
from pdfReport import PDF

# from availreport import Availreport

#########

def function_error(func_name):
	print("[ ERROR ] : function " + func_name + "() ran into an error \n")

# Loads a json-file
def import_services(json_file):
    try:
        with open(json_file, "r") as jsonfile:
        	data = json.load(jsonfile)
        	print("Configuration read in successfully...\n")
        	return data
    except:
        function_error(import_services.__name__)
        print("config-file " + json-file + " could not be imported")
        exit()

# Removes character from every row of a column of a dataframe
def remove_char_from_column(dataframe, dataframe_column, character):
	try:
		dataframe[dataframe_column] = dataframe[dataframe_column].map(lambda x: x.rstrip(character))
		return True
	except:
		print("ERROR: function remove_percent() ran into an error")
		return False

# Makes all values in dataframe column floats 
def make_dfcolumn_float(dataframe, dataframe_column):
	try:
		dataframe[dataframe_column] = dataframe[dataframe_column].astype(float)
		return True
	except:
		function_error(make_dfcolumn_float.__name__)
		return False


# Returns a dataframe where a defined string is found in a defined dataframe column
def select_dfrow_by_substring(dataframe, dataframe_column, substring):
	try: 
		sub_dataframe = dataframe[dataframe[dataframe_column].str.contains(substring)]
		return sub_dataframe
	except: 
		function_error(select_dfrow_by_substring.__name__)
		exit()

# Returns a dataframe where the dataframe columns equal the keys of json-config file
def create_services_dframe(dataframe, dataframe_column, config_json):
	try:
		print("Creating report from configuration... \n")
		
		services_dframe = pd.DataFrame(columns=list(dataframe.columns))
		
		for service in config_json:
			services_dframe = services_dframe.append(select_dfrow_by_substring(dataframe, dataframe_column, service))
		
		return services_dframe
	except:	
		function_error(create_services_dframe.__name__)
		exit()
		
	
# Makes all values of type int64 in a dataframe column to timedelta time
def convert_int64secs_to_time(dataframe, dataframe_column):
	try: 
		dataframe[dataframe_column] = dataframe[dataframe_column].apply(lambda x: datetime.timedelta(seconds=x))
		return True
	except:
		function_error(convert_int64secs_to_time.__name__)
		return False
		
'''
TODO:

* Should be able to add, sub, multi, div
* Column-name should be argument

'''
'''
def calculate_columns(dataframe, result,  column1, column2):
	print("Dataframe: : " + dataframe)
	print("Operation: " + operation)
	print("Result: " + result)
	
	dataframe[result] = dataframe.apply(lambda x: x[column1] + x[column2], axis=1)
	
	
	try: 
		if operation == 'add':
			dataframe[result] = dataframe.apply(lambda x: x[column1] + x[column2], axis=1)
		if operation == 'sub':
			dataframe[result] = dataframe.apply(lambda x: x[column1] - x[column2], axis=1)
		if operation == 'mul':
			dataframe[result] = dataframe.apply(lambda x: x[column1] * x[column2], axis=1)
		if operation == 'div':
			dataframe[result] = dataframe.apply(lambda x: x[column1] / x[column2], axis=1)
			
	except:
		function_error(calculate_columns.__name__)
	'''

#########

print("\nStarting availability report creation...\n")


csv_file = 'avail.csv'
percent = '%'
pic_directory = 'Pictures'

# import configuration
services = import_services('service_config.json')

view = [' SERVICE_DESCRIPTION',
			' TOTAL_TIME_OK',
			' TOTAL_TIME_CRITICAL', 
			' PERCENT_TOTAL_TIME_OK',  
			' PERCENT_TIME_OK_SCHEDULED', 
			]

avail_pd = pd.read_csv(csv_file, sep=',', usecols=view) 

for column in view:
	if 'PERCENT' in column:
		if False == remove_char_from_column(avail_pd, column, percent):
			print("ERROR: Could not remove percent from column " + column)
		if False == make_dfcolumn_float(avail_pd, column):
			print("ERROR: Could not convert sting to float in column " + column)
	else:
		if 'TIME' in column:
			if False == convert_int64secs_to_time(avail_pd, column):
				print("ERROR: Could not convert time in column " + column)

services_avail = create_services_dframe(avail_pd, ' SERVICE_DESCRIPTION', services)

# calculate_columns(services_avail, 'SUMME', ' TOTAL_TIME_OK', ' TOTAL_TIME_CRITICAL')

#https://stackoverflow.com/questions/32137396/how-do-i-plot-only-a-table-in-matplotlib
fig, ax =plt.subplots(figsize=(12,4))
ax.axis('tight')
ax.axis('off')
the_table = ax.table(cellText=services_avail.values,colLabels=services_avail.columns,loc='center')

#TODO: pathname building "DIR" + "month" + .png

image_path = (pic_directory + "\\" + "availability-report" + "_" + "april2021" + ".png")

plt.savefig(image_path)

pdf_body_image = Image.open(image_path, mode="r")


## DEBUG

print(services_avail)

print(avail_pd.dtypes)



#########

# TODO: use availreport.py

#avail_pd = Availreport(col_list, 'avail.csv', ',')

#avail_pd.print_all()

#avail_pd.create_dataframe()

#########


# PDF stuff

pdf = PDF()
pdf.print_page(image_path)
# TODO: filename    
pdf.output('SalesRepot.pdf', 'F')

