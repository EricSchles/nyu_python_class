def greeting(name):
    if name !='':
        print("Hello "+name)
    else:
        print("Hello there")

def greeting_two(name=''):
    if name != '':
        print("Hello "+name)
    else:
        print("Hello there")
        
#greeting("Eric")
#greeting("")
greeting_two()
greeting_two("Eric")
