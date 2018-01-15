from tkinter.filedialog import askopenfilename
from tkinter.filedialog import askdirectory
from Model.ExFile import ExFile
from Model.index import Index


class Controller:
# Returns a filename to be selected for manipulation
	def __init__(self):
		self.file = None
		self.index = Index()

	def getFileName(self):
		filename = askopenfilename(filetypes=[('CSV', '*.csv',), ('Excel', ('*.xls', '*.xlsx'))])
		self.file = ExFile(filename)

	def getDirName(self):
		self.index.path = askdirectory() + "/"

	def Process(self, string1):
		cols = string1.split(",")
		for ch in cols:
			self.file.columns.append(int(ch.strip()) - 1)
		self.Finish()

	def Finish(self):
		self.index.makeFolder(self.file)
		