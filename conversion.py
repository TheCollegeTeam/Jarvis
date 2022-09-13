def get_number(query):

    try:
        lst = query.split()
        for words in lst :
            if words.isnumeric():
                word = int(words)
        return word  
    except Exception as e:
        print(e)      

def Celsius_to_fahrenhite(query):
    try:
        c = get_number(query)
        f = ((c*9)/5)+32
        print(f"The value of {c} degree celcisus in fahrenhite in {round(f,2)}")
    except Exception as e:
        print(e)


def fahrenhite_to_Celsius():
    try:
        f = get_number(query)
        c = (((f - 32) * 5) / 9)
        print(f"The value of {f} degree fahrenhite in celcisus is {round(c, 2)}")
    except Exception as e:
        print(e)
        
=======
    lst = query.split()
    for words in lst :
        if words.isnumeric():
            word = int(words)
    return word        

def Celsius_to_fahrenhite(query):
    c = get_number(query)
    f = ((c*9)/5)+32
    print(f"The value of {c} degree celcisus in fahrenhite in {round(f,2)}")


def fahrenhite_to_Celsius():
    f = get_number(query)
    c = (((f - 32) * 5) / 9)
    print(f"The value of {f} degree fahrenhite in celcisus is {round(c, 2)}")

if __name__ == '__main__':
    query = input("Enter temprature :")
    if 'fahrenhite to celsius' in query:
        fahrenhite_to_Celsius()
        
    elif 'celsius to fahrenhite' in query:
        Celsius_to_fahrenhite() 
        