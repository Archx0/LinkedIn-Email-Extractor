#!/usr/bin/env python3
import re
import os
from time import sleep
class GetEmail: 
    
    def getEmailFromIndex(self,filename):
        with open(filename, 'r') as file:
            print("===> get names")  
            return "\n".join(re.findall('div id=".*?" style="" class="ember-view lt-line-clamp lt-line-clamp--single-line org-people-profile-card__profile-title t-black">\n(.*)',file.read())).replace("      ","")
            
    def CleanNames(self, filename, mailSyntax):
        
        names = self.getEmailFromIndex(filename)
        
        with open("names.txt", "w") as write_all_names:
            write_all_names.write(names)
        write_all_names.close()
        with open("names.txt", "r") as read_all_name:
            full_names = read_all_name.read().splitlines()
            first_names = [name.split()[0] for name in full_names]
            last_names = [re.split(r"\s+", name, maxsplit=1)[1] for name in full_names]
       

        for i in range(len(last_names)):
            last_names[i] = re.sub(r"[A-Z]+®|™+[a-zA-Z]|[a-zA-Z]+™|®+[a-zA-Z]", "", last_names[i],flags=re.IGNORECASE).strip()
            last_names[i] = re.sub(r"\s*,.*|\s-.*", "", last_names[i]).strip()
            last_names[i] = re.sub(r"[A-Z]", lambda match: match.group(0).lower(), last_names[i])
            last_names[i] = re.sub(r"\b-?\s*bin\w*\s*|\s*-\s*", "", last_names[i], flags=re.IGNORECASE)
            last_names[i] = re.sub(r"al ", "al", last_names[i]).strip()
            last_names[i] = re.sub(r"[^a-zA-Z\s]", "", last_names[i])
            # first_names[i] = re.sub(r"[A-Z]", lambda match: match.group(0).lower(), first_names[i])

        with open("first_name.txt", "w") as first_names_file:
            first_names_file.write("".join(f"{first_names}\n"))
        first_names_file.close()
        
        with open("last_name.txt", "w") as last_names_file:
            last_names_file.write("".join(f"{last_names}\n"))
        last_names_file.close()
        
        with open('emails.txt','w') as makeEmail:
            for i in range(len(first_names)):
                try:
                    if first_names[i] and last_names[i]:
                        if len(last_names[i].split()) >= 2:
                            makeEmail.write("".join(f"{first_names[i][0]}.{''.join(last_names[i].split()[1:2])}@{mailSyntax}\n"))
                        else:
                            makeEmail.write("".join(f"{first_names[i][0]}.{last_names[i]}@{mailSyntax} \n"))
                    else:
                        continue
                except:
                    print("Error ..")        
        makeEmail.close()
        
        with open('name_and_emails.txt','w') as makeEmailAndName:
            for i in range(len(first_names)):
                try:
                    
                    if first_names[i] and last_names[i]:
                        if len(last_names[i].split()) >= 2:
                            makeEmailAndName.write(f"{last_names[i]}: "+"".join(f"{first_names[i][0]}.{''.join(last_names[i].split()[1:2])}@{mailSyntax}\n"))
                        else:
                            makeEmailAndName.write(f"{last_names[i]}: "+"".join(f"{first_names[i][0]}.{last_names[i]}@{mailSyntax} \n"))
                    else:
                        continue
                except:
                    print("Error ..")        
        makeEmailAndName.close()
        print('email was seve it => on emails.txt')
        self.cleanName()
        
    def cleanName(self):
        os.remove("names.txt")
        os.remove("last_name.txt")
        os.remove("first_name.txt")     
       
def main():
    email = input("write Email domain Ex test.com: ")
    start = GetEmail()
    start.CleanNames("index.html",email)  

if "__main__" == __name__:
    main()
