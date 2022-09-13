import pyttsx3
def speak(audio):
    """
    This function convert text 
    data into speech.
    """
    try:
        engine = pyttsx3.init()
        # engine.setProperty()
        engine.say(audio)
        engine.runAndWait()
    except Exception as e:
        print(e)

    engine = pyttsx3.init()
    # engine.setProperty()
    engine.say(audio)
    engine.runAndWait()

def add_num(para):
    """
    This function add two numbers.
    """
    try:
        query = para.split()
        list = []
        for i in query:
            if i.isdigit():
                list.append(int(i))
        print(list[1]+list[0])
        speak(f"{list[1]} plus {list[0]} is{list[1]+list[0]}")
    except Exception as e:
        print(e)

    query = para.split()
    list = []
    for i in query:
        if i.isdigit():
            list.append(int(i))
    print(list[1]+list[0])
    speak(f"{list[1]} plus {list[0]} is{list[1]+list[0]}")

     
def subtract_num(para):
    """
    This function subtract two numbers
    """
    try:
        query = para.split()
        list = []
        for i in query:
            if i.isdigit():
                list.append(int(i))    
        print(list[0]-list[1])
        speak(f"{list[1]} minus {list[0]} is{list[1]-list[0]}")
    except Exception as e:
        print(e)
=======
    query = para.split()
    list = []
    for i in query:
        if i.isdigit():
            list.append(int(i))    
    print(list[0]-list[1])
    speak(f"{list[1]} minus {list[0]} is{list[1]-list[0]}")


def multiply_num(para):
    """
    This function multiply two numbers
    """
    try:
        query = para.split()
        list = []
        for i in query:
            if i.isdigit():
                list.append(int(i))
        print(list[0]*list[1])
        speak(f"{list[1]} multiplyed by {list[0]} is equal to {list[1]*list[0]}")
    except Exception as e:
        print(e)

=======
    query = para.split()
    list = []
    for i in query:
        if i.isdigit():
            list.append(int(i))
    print(list[0]*list[1])
    speak(f"{list[1]} multiplyed by {list[0]} is equal to {list[1]*list[0]}")
    
def devide_num(para):
    """
    This function devide two numbers.
    """
    try:
        query = para.split()
        list = []
        for i in query:
            if i.isdigit():
                list.append(int(i))
        if list[1]==0:
            print("can not devided by zero")
        else:
            print(list[0]/list[1])  
        speak(f"{list[0]} devided by{list[1]} is{list[0]/list[1]}")          
    except Exception as e:
        print(e)
=======
    query = para.split()
    list = []
    for i in query:
        if i.isdigit():
            list.append(int(i))
    if list[1]==0:
        print("can not devided by zero")
    else:
        print(list[0]/list[1])  
    speak(f"{list[0]} devided by{list[1]} is{list[0]/list[1]}")          

def reminder(para):
    """
    This function give reminder two numbers
    """
    try:
        query = para.split()
        list = []
        for i in query:
            if i.isdigit():
                list.append(int(i))   
        print(list[0]%list[1])    
        speak(f"reminder of {list[0]} and {list[1]} is equal{list[0]%list[1]}")
    except Exception as e:
        print(e)

=======
    query = para.split()
    list = []
    for i in query:
        if i.isdigit():
            list.append(int(i))   
    print(list[0]%list[1])    
    speak(f"reminder of {list[0]} and {list[1]} is equal{list[0]%list[1]}")
      
def squre (para):
    """
    This function calculate
    sqare of a number.
    """
    try:
        query = para.split()
        list = []
        for i in query:
            if i.isdigit():
                list.append(int(i))   
        print(list[0]*list[0])
        speak(f"squre of {list[0]} is {list[0]*list[0]}")
    except Exception as e:
        print(e)
=======
    query = para.split()
    list = []
    for i in query:
        if i.isdigit():
            list.append(int(i))   
    print(list[0]*list[0])
    speak(f"squre of {list[0]} is {list[0]*list[0]}")

def cube (para):
    """
    This function calculate
    cube of a number.
    """
    try:
        query = para.split()
        list = []
        for i in query:
            if i.isdigit():
                list.append(int(i))   
        print(list[0]*list[0]*list[0])
        speak(f"cube of {list[0]} is {list[0]*list[0]*list[0]}")
    except Exception as e:
        print(e)
=======
    query = para.split()
    list = []
    for i in query:
        if i.isdigit():
            list.append(int(i))   
    print(list[0]*list[0]*list[0])
    speak(f"cube of {list[0]} is {list[0]*list[0]*list[0]}")

def power(para):
    """
    This function calculate
    power of a number.
    """
    try:
        query = para.split()
        list = []
        for i in query:
            if i.isdigit():
                list.append(int(i))  
        print(list[0]**list[1])   
        speak(f"value of {list[0]} to the power {list[1]} is {list[0]**list[1]}")    
    except Exception as e:
        print(e) 
=======
    query = para.split()
    list = []
    for i in query:
        if i.isdigit():
            list.append(int(i))  
    print(list[0]**list[1])   
    speak(f"value of {list[0]} to the power {list[1]} is {list[0]**list[1]}")     

def sqrt(para):
    """
    This function calculate
    sqare root of a number.
    """
    try:
        query = para.split()
        list = []
        for i in query:
            if i.isdigit():
                list.append(int(i))  
        print(list[0]**0.5)    
        speak(f"square root of {list[0]} is {list[0]**0.5}")    
    except Exception as e:
        print(e)

=======
    query = para.split()
    list = []
    for i in query:
        if i.isdigit():
            list.append(int(i))  
    print(list[0]**0.5)    
    speak(f"square root of {list[0]} is {list[0]**0.5}")    


def cube_root(para):
    """
    This function calculate
    cube root of a number.
    """
    try:
        query = para.split()
        list = []
        for i in query:
            if i.isdigit():
                list.append(int(i))   
        print(list[0]**(1/3))
        speak(f"cube root of {list[0]} is {list[0]**1/3}")
    except Exception as e:
        print(e)

if __name__ == '__main__':
    while True:
        query = input("Enter a para with numbers:")
        if 'add' in query:
            add_num(query)

        elif 'subtract' in query:
            subtract_num(query)
        
        elif 'multiply' in query:
            multiply_num(query)

        elif 'devide' in query:
            devide_num(query)

        elif 'reminder' in query:
            reminder(query)
        
        elif 'squre' in query:
            squre(query)
        
        elif 'cube' in query:
            cube(query)
        
        elif 'square root' in query:
            sqrt()    
        
        elif 'cube root' in query:
            cube_root()        
        
        elif 'power' in query:
            power(query)
=======
    query = para.split()
    list = []
    for i in query:
        if i.isdigit():
            list.append(int(i))   
    print(list[0]**(1/3))
    speak(f"cube root of {list[0]} is {list[0]**1/3}")
if __name__ == '__main__':
    
    query = input("Enter a para with numbers:")
    if 'add' in query:
        add_num(query)

    elif 'subtract' in query:
        subtract_num(query)
    
    elif 'multiply' in query:
        multiply_num(query)

    elif 'devide' in query:
        devide_num(query)

    
    elif 'reminder' in query:
        reminder(query)
    
    elif 'squre' in query:
        squre(query)
    
    elif 'cube' in query:
        cube(query)
    
    elif 'square root' in query:
        sqrt()    
    
    elif 'cube root' in query:
        cube_root()        
    
    elif 'power' in query:
        power(query)
