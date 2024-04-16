
from events.Events import *
import random
import time

class QUIC : 

    def _init_(self,s) -> None:
        self.password = "t"
        self.singup = False
        self.login = False
        self.task = False
        self.l = []

    def reset(self, reset_run=True):
        if reset_run:
            self.singup = False
            self.login = False

    def Login(self) :
        time.sleep(1)
        if self.singup == True:   
            self.login = True
            return b"DashBord"
        else: 
            self.login = False
            return b"Error"

    def Loginfailed(slef):
        time.sleep(1)
        slef.login = False
        return b"Login"

    def SignUp(self, only_reset):
        time.sleep(1)
        self.reset(only_reset)
        self.singup = True
        return b"DashBord"
    
    def addtask(self) :
        if self.login == True :
            self.task = True
            return b"addtask"
        else: return b"Error"

    def removetask(self) :
        if self.login == True and self.task == True :
            self.task == False
            return b"removetask"
        else: return b"Error"
    
    def send(self,command):
        try: 
            if isinstance(command,SendLoginEvent) :
                print("Send Login")
                return self.Login()
            elif isinstance(command,SendSignUpEvent):
                print("send Signup")
                return self.SignUp(True)
            elif isinstance(command,Loginfailed):
                print("send Loginfailed")
                return self.Loginfailed()
            elif isinstance(command,addTask):
                print("send addtask")
                return self.addtask()
            elif isinstance(command,RemoveTask):
                print("send removeta")
                return self.removetask()
        except Exception as err:
            print("error")