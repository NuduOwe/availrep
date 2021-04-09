import pandas as pd

class Availreport():

	def __init__(self, column_list, data_source, delimiter):
		self._column_list = column_list
		self._data_source = data_source
		self._delimiter = delimiter
		self.__dataframe = []
		
	def print_all(self):
		for x in self._column_list:
			print(x)
		print(self._data_source)
		print(self._delimiter)	
			
	def create_dataframe(self):
		try: 
			self.__dataframe = pd.read_csv(self._data_source, sep=self._delimiter, usecols=self._column_list)
		except: 
			print("ERROR: dataframe could not be read from csv-file")
			traceback.print_exc()
			exit()
		
	# Removes character from every row of a column of a dataframe
	def remove_char_from_column(dataframe_column, character):
		try:
			self.__dataframe[dataframe_column] = self.__dataframe[dataframe_column].map(lambda x: x.rstrip(character))
			return True
		except:
			print("ERROR: function remove_percent() ran into an error")
			return False

	#TODO: think about making float a variable --> change func-name
	def make_dfcolumn_float(dataframe_column):
		try:
			self.__dataframe[dataframe_column] = self.__dataframe[dataframe_column].astype(float)
			return True
		except:
			print("ERROR: function remove_percent() ran into an error")
			return False


	#TODO: 
	def sel_dfrow_by_substring(dataframe_column, substring):
		try: 
			sub_dataframe = self.__dataframe[self.__dataframe[dataframe_column].str.contains(substring)]
			return sub_dataframe
		except: 
			print("ERROR: function sel_dfrow_by_substring() ran into an error")
			traceback.print_exc()
			exit()	