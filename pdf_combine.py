import PyPDF2


# Call PdfMerger() method that returns merger object and it does not take any argument
merger = PyPDF2.PdfMerger()

# Set a array of two files(combining these two)
file_names = ["firstPdf.pdf", "secondPdf.pdf"]

# Iterate over the list then append the list to merger object
for file_name in file_names:
  merger.append(file_name) 

# Now write the merger object in new pdf file(combinedPdf.pdf)
merger.write("combinedPdf.pdf")
