#!/usr/bin/env python3
import re
import os
from time import sleep
class GetEmail:
    def getEmailFromIndex(self,filename):
        with open(filename, 'r') as file:
            print("===> get names")  
            return "\n".join(re.findall('div id=".*?" style="" class="ember-view lt-line-clamp lt-line-clamp--single-line org-people-profile-card__profile-title t-black">\n(.*)',file.read())).replace("      ","")
            
    def CleanNames(self , filename,mailSyntax):
        names = self.getEmailFromIndex(filename)
        with open("names.txt",'w') as fileName:
            fileName.write(names)
        fileName.close()    
        os.system("cat names.txt | cut -d \" \" -f1 > firstName.txt")
        os.system("cat names.txt |cut -d \" \" -f2,3,3,4 > Last.txt")
        print("===> make first and last name")  
        sleep(.5)
        oldLastname = open("Last.txt","r").readlines()
        newLastName = open("newLastName.txt","w")
        
        print("===> clean names ")  
        for i in range(len(oldLastname)):
            if(len(oldLastname[i]) <= 3):
                L = oldLastname[i][3:].replace(',','').replace(',','').replace("\n","").replace("'","").replace("-","").replace("bin","").replace("Bin","").replace("AL ","Al").replace("Al ","Al").replace("Ba ","ba").replace("ba ","ba").replace("Abo ","abo").replace("abo ","abo")
                newLastName.write(f"{L}\n")
            else:
                if("." in oldLastname[i]):
                    L = oldLastname[i][3:].replace(',','').replace(',','').replace("\n","").replace("'","").replace("-","").replace("bin","").replace("Bin","").replace("AL ","Al").replace("Al ","Al").replace("Ba ","ba").replace("ba ","ba").replace("Abo ","abo").replace("abo ","abo")
                    newLastName.write(f"{L}\n")
                else:
                    L = oldLastname[i].replace(',','').replace(',','').replace("\n","").replace("'","").replace("-","").replace("bin","").replace("Bin","").replace("AL ","Al").replace("Al ","Al").replace("Ba ","ba").replace("ba ","ba").replace("Abo ","abo").replace("abo ","abo")
                    newLastName.write(f"{L}\n") 
        os.system("rm -rf lastname.txt && cat newLastName.txt | cut -d \" \" -f1 > lastname.txt")                               
        sleep(1)  
           

    def makeMail(self,mailSyntax):            
            print("===> create mails ...")
            firstName = open("firstName.txt",'r').readlines()
            lastName = open('lastname.txt','r') .readlines()
            with open("Emails.txt",'w')as Emails:
                for i in range(len(firstName)):
                    first = firstName[i][0].replace(" ","").replace("\n","") ########## ====> first char in first name
                    last = lastName[i].replace(" ","").replace("\n","")      ########## ====> Last name
                    Emails.write(f"{first}.{last}@{mailSyntax}\n")  
            Emails.close()
            self.cleanUp()        
    def cleanUp(self):
        os.popen("rm -rf newLastName.txt Last.txt firstName.txt firstName.txt Last.txt names.txt lastname.txt ")    
        print("===> clean file")            
def main():
    email = "test.com"
    start = GetEmail()
    start.CleanNames("index.html",email)  
    os.system("cat newLastName.txt | cut -d \" \" -f1 > lastname.txt")          
    start.makeMail(email) 
if "__main__" == __name__:
    main()