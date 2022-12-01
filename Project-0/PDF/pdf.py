import sys
import PyPDF2


inputs = sys.argv[1:]

def pdf_merger(pdf_list):
   merger = PyPDF2.PdfFileMerger()
   for pdf in pdf_list:
      print(pdf)
      merger.append(pdf)
   merger.write('S-pdf.pdf')


pdf_merger(inputs)





















# with open ("norse.pdf", mode= "rb") as text:
#    reader = PyPDF2.PdfFileReader(text)
#    turn =reader.getPage(56)
#    turn.rotateCounterClockwise(90)
#    writer = PyPDF2.PdfFileWriter()
#    writer.addPage(turn)
#    # print(text.read())
#    with open("turned.pdf", mode= "wb") as text1:
#       writer.write(text1)