import PyPDF2


# Call pdfReader method that takes file stirng
# The open() method retunrs file string so first call the open method
# Open the firstPdf.pdf file with read binary mode
# Better approach to open with 'with' statement as file then pass the file object to the reader method
# And we get a pdf file reader object
with open("firstPdf.pdf", "rb") as file:
  reader = PyPDF2.PdfReader(file)

  # Print the number of pages in the pdf using .pages member
  print(len(reader.pages))

  # Specify the page index from the pdf where want to modify that returns page object
  page = reader.pages[0]

  # Now ratate the page 90 degree clock wise
  page.rotate(90)

  # Create a PdfWriter object using PdfWrite() method(because up to this it deals with pdf in memory
  # Now need to wtire the updaed on ein the new pdf) that returns writer object
  writer = PyPDF2.PdfWriter()

  # Call add_page() method and pass page object 
  # this method will add this page object at the end of the new pdf.
  writer.add_page(page)

  # Now we need a file string again to write there so open the new pdf file with 'with' statement as output
  # then write the output object
  with open("rotatedPdf.pdf", "wb") as ouput:
    writer.write(ouput)
