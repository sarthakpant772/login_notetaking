from password import password
from note import note
from search import search_name

class check:
    def __init__(self,num):
        # 1 for login 2 for signup
        self.num=num
    def login(self):
        username=input("\nenter user name\t")
        passw=input("\nenter your password\t")
        
        red=open("user_Name.txt",'r')
        check2=red.read()
        check2= check2.split()
        if username in check2:
            index=check2.index(username)+2
            if passw == check2[index]:
                print("login success!!!!!")
                no=note(username)
                no.write_notes()
            else:
                print("\nlogin failed plese login again\n")
                self.login()
        else:
            print("\nusername not found please signup")
            self.signup()            
        
    def signup(self):
        value=True
        check="true"
        while(value):
            if(check=="true" or check=="True"):
                username=input("\nenter your username\t")
                passw=input("\nenter your password\t")
                checkU=search_name(username)
                checkSpace=checkU.checkforspace()
                if(checkSpace):
                    red=open("user_Name.txt",'r')
                    f=red.read()
                    f=f.split()
                    if username in f:
                        check=input("\nyour username already taken \nif you want to enter another detail then type true else false\t")
                    else:
                        print("\n read")
                        saving=password(username,passw)
                        saving.save()
                    red.close()  
                    check=input("\nif you want to enter another detail then type true else false\t")
                check=input("\nif you want to enter another detail then type true else false\t")      
            else:
                value=False
        
                   
                
    
    