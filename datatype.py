x = "y"

def main(): 
    print(" ")   
    print("Hey there, Hope you are doing great.")
    print(" ")
    print(" ")
    List_pdp = ["Number" , "Strings" , "List" , "Tuple" , "Dictionary" , "Set"]
    print(List_pdp)
    print(" ")
    a = input("Enter the name of the data type you want to know about -->  ")
    print(" ")
    if a == "Number":
        print(" ")
        print('''Number Datatype:-
            NUmber datatype stores numeric value which are integer, float, and complex.''')
    elif a == "Strings":
        print(" ")
        print('''String Datatype:- 
            A string  is the sequence of characters. 
            we can use single quotes or double quotes to represent strings
            Multiline string can be denoted with triple quotes.
            eg:- a = 'hey'  
                b = "Name"
                c =' '' Hey, How are you doing.
                hope you are doing well.
                Good bye ' ''  "''')
        print(" ")
    
    elif a == "List":
        print(" ")
        print('''List Datatype :-  
            List is one of the powerful datatypes of python an it is very flexible.
            In list items are separated with commas i.e ",", and it is denoted with "[]".
            List is mutual and mutable.
            Which means we can change value or elements in List. 
            
            eg:- 
                a = [23,65,"Name"]
                print(a) ''')
        print(" ")
    
    elif a == "Tuple":
        print(" ")
        print('''Tuple Datatype:- 
            It is an ordered sequence of items, small as List.
            The only difference between tuple and list is immutability.3
            Tuples are immutable while list is mutable.
            Tuples are used to write protected data(* passwords, or any another kind of confidential 
            information for eg.) because of immuatability. It is defined with 
            parentheses "()", curly braces "{ }" . In tuples items are separeted by commas ",".
            we can write another tuple in an existing tuple. ''')
        print(" ")
    
    elif a == "Dictionary":
        print(" ")
        print('''Dictionary Datatype:-
            Dictionary is a collection of value with key pair it is generally
            used when we have huge amount of data.
                Dictionary are optimised for retriving data. We must know the key for retriving value.
            In python dictionary are defined with curly braces"{ }", with each item bring pair in the
            form of key values. Values van be of any types.
            
        For example -->
            a = {'Key 1 ': 'Value','key 2':'value'} ''')
        print(" ")

    elif a == "Set":
        print(" ")
        print("""Set datatype:- 
            Set is a collection of unique item. 
            It is defined by value separated by comma ',' , and is 
            written within the braces.
            
            Eg --> 
                a = {1,2,4,6,22,4,6,1} """)
        print(" ")

    else:
        print("Please select any one option from above.")
        main()  

while x == "y":
    main()
    x = input("Do you want to search for another item (y/n)--> ")     
