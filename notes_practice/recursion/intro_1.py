
# While th fn is not finished exceuting , it will remain in Stack 
# When the Fn is Finished Exueting , it is removd from Stack and Flow of Program return where it was called 

def msg():
    print("Hello Dileep")
    msg1()

def msg1():
    print("Hello Dileep")
    msg2()
def msg2():
    print("Hello Dileep")
    msg3()
def msg3():
    print("Hello Dileep")

msg() # Afunction calls Another Function



