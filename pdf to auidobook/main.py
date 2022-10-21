import pyttsx3 
import pdfplumber
import PyPDF2
file="sample.pdf"
pdffile=open(file,'rb')
pdfreader=PyPDF2.PdfFileReader(pdffile)
pages=pdfreader.numPages
with pdfplumber.open(file) as pdf:
    for i in range(0,pages):
        page=pdf.pages[i]
        text=page.extract_text()
        print(text)
        speaker=pyttsx3.init()
        speaker.say(text)
        speaker.runAndWait()