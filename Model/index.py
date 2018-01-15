import xlrd, os
from tkinter import *

class Index:

	def __init(self):
		self.path = None

	def makeWithOneColumn(self, index, col1, worksheet):
			entry1 = worksheet.cell(index, col1).value	 				   
			os.makedirs(self.path+entry1)

	def makeWithTwoColumn(self, index, col1, col2, worksheet):
			entry1 = worksheet.cell(index, col1).value
			entry2 = worksheet.cell(index, col2).value
			os.makedirs(self.path+entry1+", "+entry2)

	def makeWithThreeColumn(self, index, col1, col2, col3, worksheet):
			entry1 = worksheet.cell(index, col1).value
			entry2 = worksheet.cell(index, col2).value
			entry3 = worksheet.cell(index, col3).value
			os.makedirs(self.path+entry1+", "+entry2+", "+entry3)

	def makeFolder(self, ExFile):
		workbook = xlrd.open_workbook(ExFile.name)
		worksheet = workbook.sheet_by_index(0)
		if len(ExFile.columns) == 1:
			for index in range(1,len(worksheet.col(0))):
				self.makeWithOneColumn(index, ExFile.columns[0],worksheet)
		elif len(ExFile.columns) == 2:
			for index in range(1,len(worksheet.col(0))):
				self.makeWithTwoColumn(index, ExFile.columns[0], ExFile.columns[1], worksheet)
		elif len(ExFile.columns) == 3:
			for index in range(1,len(worksheet.col(0))):
				self.makeWithTwoColumn(index, ExFile.columns[0], ExFile.columns[1], ExFile.columns[2], worksheet)                        