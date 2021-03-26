import pandas as pd
import datetime

from availreport import Availreport

#########

# Removes character from every row of a column of a dataframe
def remove_char_from_column(dataframe, dataframe_column, character):
	try:
		dataframe[dataframe_column] = dataframe[dataframe_column].map(lambda x: x.rstrip(character))
		return True
	except:
		print("ERROR: function remove_percent() ran into an error")
		return False

#TODO: 
def make_dfcolumn_float(dataframe, dataframe_column):
	try:
		dataframe[dataframe_column] = dataframe[dataframe_column].astype(float)
		return True
	except:
		print("ERROR: function remove_percent() ran into an error")
		return False


#TODO: 
def sel_dfrow_by_substring(dataframe, dataframe_column, substring):
	try: 
		sub_dataframe = dataframe[dataframe[dataframe_column].str.contains(substring)]
		return sub_dataframe
	except: 
		print("ERROR: function sel_dfrow_by_substring() ran into an error")
		exit()	
	


#########

print("")
print("Starting availability report creation...")
print("")


csv_file = 'avail.csv'

col_list = ['HOST_NAME',
			' SERVICE_DESCRIPTION', 
			' PERCENT_TOTAL_TIME_OK', 
			' PERCENT_TOTAL_TIME_CRITICAL', 
			' TIME_OK_SCHEDULED', 
			' TIME_OK_UNSCHEDULED']

# avail_pd = pd.read_csv(csv_file, sep=',', usecols=col_list) 
# avail_pd = pd.read_csv(csv_file, sep=',', usecols=col_list) 

avail_pd = Availreport(col_list, 'avail.csv', ',')

avail_pd.print_all()

avail_pd.create_dataframe()



'''
for column in col_list:
	if 'PERCENT' in column:
		if False == remove_char_from_column(avail_pd, column, '%'):
			print("ERROR: Could not remove percent from column " + column)
		if False == make_dfcolumn_float(avail_pd, column):
			print("ERROR: Could not convert sting to float in column " + column)
'''

cycletime_avail = sel_dfrow_by_substring(avail_pd, ' SERVICE_DESCRIPTION', "cycle")




print(avail_pd)

print(avail_pd.dtypes)

#datetime.fromtimestamp(2677362)