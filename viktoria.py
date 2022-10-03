import json
from file import*


#GET THE DICTIONARY 
my_new_rec = json.load((open("My_Record.json")))
print(my_new_rec)



#WRITE TO THE DICTIONARY 
def writer(arg_1):
    j = json.dumps(my_new_rec)
    with open("My_Record.json", "w") as f:
        f.write(j)
        f.close()


#WORD ADDER 





#INTERACT WITH THE USER    			
def interactor(arg_1):
    the_ratings = []
    the_lowest = 0
    for i in range(len(arg_1)):
        the_ratings.append(arg_1[i]["rating"])    
    
    the_lowest = min(the_ratings)
    

    #ASK_INCREMENT_THE_LOWEST_RATING 
    for i in range(len(arg_1)):
        if arg_1[i]["rating"] == the_lowest:
            a = input(f"{arg_1[i]['word']}, \n")
            if a == arg_1[i]["translation"]:
                arg_1[i]["rating"] = arg_1[i]["rating"] + 1
                print("yaaay!",arg_1[i]["word"], " = ", a)
    #NEW WORD AND FINISH
            elif a == "F":
                return writer(arg_1)
            elif a == "N":
                add_new_word(arg_1)
                                        
                    
            else:
                arg_1[i]["rating"] = arg_1[i]["rating"] - 1
    
  
    return interactor(arg_1)
                



# #Create json 
# def json_append_write(the_dict):



    

# #WRITE INTO THE FILE 
# def append_write(arg_1):

# 	with open('file.py','w') as list:
# 		list.write("a = ")


# 	with open('file.py','a') as list:
# 		list.write(str(a))


def add_new_word(a):
    d = {}
    d["word"] = input("Enter the Word in ENGLISH: ")
    
    #Check if we have it in the list
    for i in range(len(a)):
        if a[i]["word"] == d["word"]:
            return f"Sorry The word {d['word']} is already in the list"
    d["translation"] = input(f"Enter the Translation of the word {d['word']}")
    d["rating"] = 0
    get_input = input((d['word'].lower(), " with the translation ", d["translation"].lower(), " has been added to the list, press y to confirm or n to decline"))
    if get_input.lower() == "y":
        a.append(d)
        print(a)


interactor(my_new_rec)