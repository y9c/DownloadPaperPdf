import urllib
import re
import os
from PyPDF2 import PdfFileReader, PdfFileMerger
url0="http://www.nature.com/nature/current_issue.html"
#url0="http://www.nature.com/nature/supplements/insights/machine-intelligence/index.html"
p=re.compile('<hgroup><h1><a href="(.*?)">.*?</a>')
#p1=re.compile('<a class="box icon pdf(.*?)PDF</a>')
p1=re.compile('href="(.*?\.pdf)"')
os.system("mkdir temp_folder")
os.chdir("./temp_folder")
def gethtml(url):
    sock=urllib.urlopen(url)
    html=sock.read()
    sock.close()
    return html

def completeurls(urls):
    urls_out=[]
    for i in urls:
         if i.startswith("http"):
             urls_out.append(i)
         else:
             urls_out.append("http://www.nature.com"+i)
    return urls_out

html=gethtml(url0)
urls_0=re.findall(p,html)
urls_1=completeurls(urls_0)
print urls_1
urls_2=[]
for i in urls_1:
    html1=gethtml(i)
    urls_2+=re.findall(p1,html1)
urls_3=completeurls(urls_2)
urls_3=list(set(urls_3))
num=len(urls_3)
print urls_3

for i in range(num):
    os.system("wget -O "+str(i)+".pdf "+urls_3[i])
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
merger.write("nature_merged_full.pdf")
os.system("rm -rf temp_folder")
