import PyPDF2


temp = PyPDF2.PdfFileReader(open("norse.pdf", mode="rb"))
watermark = PyPDF2.PdfFileReader(open("turned.pdf", mode="rb"))
output =PyPDF2.PdfFileWriter()

for i in range(temp.getNumPages()):
    page= temp.getPage(i)
    page.mergePage(watermark.getPage(0))
    output.addPage(page)

with open("halala.pdf", mode= "wb") as watermarked:
    output.write(watermarked)