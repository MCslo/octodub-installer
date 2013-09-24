from GetUserInput import GetUserInput
from executeShell import executeShell
from bs4 import BeautifulSoup
#import xml.etree.ElementTree as ET
import os


from os import listdir
from time import sleep


#get and return the current directory you are in
def getPath():
    dir = os.getcwd()
    return dir

#List and return the items/files that are in a directory
def listDirContent():
    pat = getPath() + "\installers"
    content = listdir(pat)
    
    return content




	
def getSetting(para):
	for parameter in para:
		for item in soup.find_all("app"):
			if item.find("exe").contents[0] == parameter:
				sw = item.find("switch").contents[0]
				ex =getPath()+ "\installers\\" + parameter +" "+sw
                print ex
                executeShell(ex)
                
				

#Function to execute external commands (for example a Shell script/line)
#executeShell("dir")

#parsing the config XML

iksemel=open(getPath()+"\install_config.xml")

soup=BeautifulSoup(iksemel)



#tree = ET.parse(iksemel)
#root= tree.getroot()


	


#Get the list of all installers in the installer folder

getPath()
listOfOptions = listDirContent()




#Start gui
choice=GetUserInput(listOfOptions, True).getInput()
blah=choice.split()
getSetting(blah)


