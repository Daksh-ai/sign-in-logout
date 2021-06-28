class user:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
    def Platform(self):
        self.plot=input("Enter the platform")
        return "Platform:{}".format(self.plot)
    def email(self):
        return "Email:{}{}@Gmail.com".format(self.fname,self.lname)
    def plat(self):
        return "Platform:{}".format(self.plot)
    def u_name(self):
        self.a=input("Enter the user name")
        return self.a
    def passwd(self):
        self.passwd=input("Enter the password")
        return self.passwd
    def phone(self):
        self.phone_no=int(input("Enter The phone Number"))
        return self.phone_no
        
if __name__ == '__main__':
    
    b=user(input("Enter the first Name"),input("Enter the last Name"))

    a=int(input("1:Sign in Account\n2:login Account"))
    print(b.Platform())

    if a==1:
        f=open("code1.txt","a")
        f.write(input("Enter the first Name\n"))
        f.write("\n")
        f.write(input("Enter the last Name\n"))
        f.write("\n")
        f.write(input("Enter the password\n"))
        f.write("\n")
        f.close()
        print("Sign in Account Sucessfully!")
        input("PRESS ANY KEY TO EXIT")
        
    elif a==2:
        m=int(input("1:email\n 2:phone number\n3:username"))
        if m==1:
            print(b.email())
            print(b.passwd())
            print("LOGIN SUCESSFULLY!")
        elif m==2:
            print(b.phone())
            print(b.passwd())
            print("LOGIN SUCESSFULLY!")
        elif m==3:
            print(b.u_name)
            print(b.passwd())
            print("LOGIN SUCESSFULLY!")
    
        
    