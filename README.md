# Working with PDF files in Python. 
***
There are lots of packages that work with PDF most popular one is pypdf2. Let's get started:

## 1. Create a new project and open in vscode:
    a. Open the terminal and go to users: cd
    b. Create a directory for the project: mkdir pyPdf
    c. Go to pyPdf directory: cd pyPdf
    d. Open the directory in vscode: code .

## 2. Create virtual environment and install packages:
    a. Open terminal in vscode and install pypdf2 with pipenv: pipenv install PyPDF2
    b. On date 18th Dec, 23 the latest version is 3.0.1

## 3. Start codding:
    a. Create a py file, pdf_rotation.py in the source directory
    b. Select newly created virtual environment for the project in vscode
    b. Import pypdf2 module at the top of the file
```python
        Codes:
                import PyPDF2
```
    c. In this module there are few classes to work with pdf files. Like we have pdfReader, pdfWriter,
       pdfMerger etc. Let's strat with creating PdfReader.
```python
        Codes:
                import PyPDF2

                PyPDF2.PdfReader()
```
        We need to pass a file string in the pdfFileReader() method. The file string is the object that built in open() function returns. Let's say we have a couple of pdf files in the source directory: firstPdf.pdf and secondPdf.pdf so using the open method sytax open("file_name_path", "mode") the second argument is about the mode like read/write and the open function is needed to be read as binary so for this the argument should be "rb". 
```python
        Codes:
                import PyPDF2

                open("firstPdf.pdf", "rb")
                PyPDF2.PdfReader()
```
    d. Now we have the file string object so we are going to use 'with' statement since we open the file and 
       later we need to close it as well, so better use 'with' statement.
```python
        Codes:
                import PyPDF2

                with open("firstPdf.pdf", "rb") as file:
                  PyPDF2.PdfReader(file)
```
    e. And we get pdf file reader object.
```python
        Codes:
                import PyPDF2

                with open("firstPdf.pdf", "rb") as file:
                  reader = PyPDF2.PdfReader(file)
```
    f. Now this reader object has few intersting members. One of this is len(reader.pages) which returns the
       number of pages of the pdf. Let's print and see the number of pages of the firstPdf.pdf
```python
        Codes:
                import PyPDF2

                with open("firstPdf.pdf", "rb") as file:
                  reader = PyPDF2.PdfReader(file)
                  print(len(reader.pages))
```
        OutPut: 1
        So in this pdf there is only a single page.

    g. Also there is a member called pages[] it takes a page index number. Because the index of the first page
       is 0, so when we pass 0 we get first page And this returns a page object.
```python
        Codes:
                import PyPDF2

                with open("firstPdf.pdf", "rb") as file:
                  reader = PyPDF2.PdfReader(file)
                  print(len(reader.pages))
                  page = reader.pages[0]
```    
    h. This page object has few interesting members like rotate. This also has scale a given factor also given
       width and height here is the package document for detail - https://pypi.org/project/PyPDF2/ 
       Here we will going to use rotate method let's rotate 90 clockwise if we set -90 then it rotates anti clockwise:
```python
        Codes:
                import PyPDF2

                with open("firstPdf.pdf", "rb") as file:
                  reader = PyPDF2.PdfReader(file)
                  print(len(reader.pages))
                  page = reader.pages[0]

                  page.rotate(90)
```
    i. So far this set of codes just rotates the page object in memory, this does not modify the original pdf
       So we need to write this is a separate pdf file. For that we need a pdf file writer so;
```python
        Codes:
                import PyPDF2

                with open("firstPdf.pdf", "rb") as file:
                  reader = PyPDF2.PdfReader(file)
                  print(len(reader.pages))
                  page = reader.pages[0]

                  page.rotate(90)

                  writer = PyPDF2.PdfWriter()
                  # We do not pass any arguements this simply creates a writer object.
```
    j. This writer object deals with memory not in file disc. Now we call add_page() method and pass the page
       object here. This method will add this page object at the end of the new pdf.
```python
        Codes:
                import PyPDF2

                with open("firstPdf.pdf", "rb") as file:
                  reader = PyPDF2.PdfReader(file)
                  print(len(reader.pages))
                  page = reader.pages[0]

                  page.rotate(90)

                  writer = PyPDF2.PdfWriter()
                  # We do not pass any arguements this simply creates a writer object.

                  writer.add_page(page)
```
    k. We can also use insert_page() method it takes an index, so if you want to reorder or add the page on a
       specific index to pass the second argument, 0 1 2 3 whatever index. 
```python
        Codes:
                writer.insert_page(page, 3)
```
    l. Also we can use insert_blank_page() method to add a blank page that does not take any arguments.
```python
        Codes:
                writer.insert_blank_page()
```
    m. Now let's back to the add_page() method and finally we need to write this pdf file memory file on disc.
       For that we need another file string so we can use the with statement again to open up another file(the new file where we are going to write) let's say it is rotedtedPdf.pdf and as second argument we need to pass 'wb' the short form of write in binary. 
```python
        Codes:
                import PyPDF2

                with open("firstPdf.pdf", "rb") as file:
                  reader = PyPDF2.PdfReader(file)
                  print(len(reader.pages))
                  page = reader.pages[0]

                  page.rotate(90)

                  writer = PyPDF2.PdfWriter()
                  # We do not pass any arguements this simply creates a writer object.

                  writer.add_page(page)

                  # Use with statement to open a file then call the file string output as output:
                  with open("rotatedPdf.pdf", "wb") as output:
                    # Finaly we call .write() and pass the file string 'output'
                    writer.write(output)
```
        Now save the changes and run the program and you can see the content of firstPdf.pdf is rotated 90 degree.

## 4. Now let's create another script, combine multiple pdfs to a single pdf:
    a. Create a new py file named pdf_combine.py
    b. import PyPDF2

## 5. Strat codding:
    a. Use PdfFileMerger() method to merge multiple pdfs
```python
        Codes:
                import PyPDF2

                PyPDF2.PdfMerger()
```
    b. So let's create a merger object
```python
        Codes:
                import PyPDF2

                merger = PyPDF2.PdfMerger()
```
## 6. Now let's say we have array of file names and we set this to a arry of two stirngs. In real project instead of hard coded array, you can iterate over all the pdfs in a directory. 
```python
        Codes:
                import PyPDF2

                merger = PyPDF2.PdfMerger()
                file_names = ["firstPdf.pdf", "secondPdf.pdf"]
```
## 7. Now iterate over this array and call the merger.append() and pass the file_name.
```python
        Codes:
                import PyPDF2

                merger = PyPDF2.PdfMerger()
                file_names = ["firstPdf.pdf", "secondPdf.pdf"]

                for file_name in file_names:
                  merger.append(file_name)
```
## 8. So up to this point, we are merging the pdfs in memory now we need to write the result on file disc. So we call write() method and pass file object or a string the specifies the name of the file(this will be the new combined pdf file).
```python
        Codes: 
                import PyPDF2

                merger = PyPDF2.PdfMerger()
                file_names = ["firstPdf.pdf", "secondPdf.pdf"]

                for file_name in file_names:
                  merger.append(file_name)

                merger.write("combinedPdf.pdf")
```
        Now save the changes and run the program and see the newly created pdf named combinedPdf.pdf file with the combined one.
