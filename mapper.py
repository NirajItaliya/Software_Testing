
from events import *
from events.Events import *
# s = Scapy()


def QuicInputMapper(alphabet, s):
    match alphabet:
        case "Login":
            x = s.send(SendLoginEvent())
        case "SignUp":
            x = s.send(SendSignUpEvent())
        case "Loginfailed":
            x = s.send(Loginfailed())
        case "addTask":
            x = s.send(addTask())
        case "removeTask":
            x = s.send(RemoveTask())
        case default:
            pass
    return x


def QuicOutputMapper(data):
    output = ""
    if data == b"Login":
        output = "Login"
    elif data == b"DashBord" :
        output = "DashBord"
    elif data == b"Error":
        output = "ERROR"
    elif data == b"addtask":
        output = "AddTask"
    elif data == b"removetask":
        output = "RemoveTask"
    else:
        output = "ERROR"
    return output