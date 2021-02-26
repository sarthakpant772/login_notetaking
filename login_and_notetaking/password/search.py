checkname=open("user_Name.txt",'r')
checkpassword=open("user_password.txt",'r')
class search_name:
    user_number=0
    n=0
    def __init__(self,name):
        self.name=name                         
    def checkforspace(self):
        ret=True
        for l in self.name:
            if(l==" "):
                ret=False
        if(ret==False):
            print("\nusername cannot have spaces")
            return ret
        else:
            return ret
    