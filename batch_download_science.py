import urllib
import re
import os
from PyPDF2 import PdfFileReader, PdfFileMerger
url0="http://www.sciencemag.org/content/current"
p=re.compile('<a href="(.*?)" rel="full-text.pdf">Full Text \(PDF\)</a>')
os.system("mkdir temp_folder")
os.chdir("./temp_folder")
def gethtml(url):
    sock=urllib.urlopen(url)
    html=sock.read()
    sock.close()
    return html

html=gethtml(url0)
urls=re.findall(p,html)
num=len(urls)
for i in range(num):
    print "wget -O "+str(i)+".pdf http://www.sciencemag.org"
    print urls[i]
    os.system("wget -O "+str(i)+".pdf http://www.sciencemag.org"+urls[i])

#pdf_files=[f for f in os.listdir("./") if f.endswith("pdf")]
merger=PdfFileMerger()
pdf_files=[str(i)+".pdf" for i in range(num)]
for filename in pdf_files:
    try:
        merger.append(PdfFileReader(filename, "rb"))
        print "done!"
    except:
        print "ERROR",i 
os.chdir("../")
merger.write("science_merged_full.pdf")
os.system("rm -rf temp_folder")
