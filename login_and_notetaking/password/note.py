class note:
    def __init__(self,name):
        self.name=name
    def write_notes(self):
        f=open(self.name+".txt",'a')
        f.close()
        f=open(self.name+".txt",'r+')
        f.write(self.name+" Notes\n")
        print("\nlogin success!!!!!\nhere are your notes\n")
        print(f.read())
        t="true"
        while(t=="true" or t=="True"):
            a=input("\nadd a new note\n")
            f.write(a+"\n")
            t=input("\ndo you want to add more type true else false\n")
        f.close()
        return 0

    