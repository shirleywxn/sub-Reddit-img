import urllib
import urllib2

def download_alien():
    URL=raw_input("Enter Valid Sub-Reddit URL: ")
    webpage=urllib2.urlopen(URL)
    data=webpage.read()
    webpage.close()
    alien=data.find("id='header-img'")
    URLbegin=alien+data[alien:].find('src="')+5
    URLlen=data[URLbegin:].find('"')
    imgURL=data[URLbegin:URLbegin+URLlen]
    
    pic = urllib.urlopen(imgURL)
    filename="sub-Reddit-img.jpg"    
    output = open(filename,"wb")
    output.write(pic.read())
    output.close()
    
    
    
    
    
    
    
    