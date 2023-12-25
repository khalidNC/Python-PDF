import PyPDF2
import os

'''
Terget is to:
- get all the pdf files from the directory path
- iterate over the iterable
- then append it to merger object
'''
# Call PdfMerger() method that returns merger object and it does not take any argument
merger = PyPDF2.PdfMerger()

# path module has expanduser() method to get absulate path of the directory assuming the directory is in user directory
# and the path directory retrns directory_path object
# this object is not iterable directly since it has only a path
diretory_path = os.path.expanduser("~/pyPdf/reports")

# use os.listdir() method it returns a list out of a directory itmes. So we get a list of all pdf files name in the directory
# then iterate over the list as: for item in items:
# then need to get all the file's paths in string to do use os path module join() method, it returns file_path object in string
# Then finally append the string in merger object

for file_name in os.listdir(diretory_path):
  file_path = os.path.join(diretory_path, file_name)
  merger.append(file_path)

# Now write the merger object in new pdf file(combinedPdf.pdf)
merger.write("abba_report_2023.pdf")
# Then close the function
merger.close()
