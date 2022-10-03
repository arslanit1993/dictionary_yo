import json
from file import*



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
                print(arg_1)
            elif a == "F":
                return append_write(arg_1)
            else:
                arg_1[i]["rating"] = arg_1[i]["rating"] - 1
    
    print(arg_1)
    return interactor(arg_1)
                
    

#WRITE INTO THE FILE 
def append_write(arg_1):

	with open('file.py','w') as data:
		data.write("a = ")


	with open('file.py','a') as data:
		data.write(str(a))


interactor(a)