#https://github.com/Ahamed-Fahim29/HIT137-Assignment-02_Group-125-SYD
global_variable = 100 
my_dict= {'ke11': 'value1', 'ke12': 'value2', 'ke13': 'value3'}

def process_numbers():
    # No need to call the global variable
    local_variable = 5 # No need to declare, it is local variable
    numbers=[1, 2, 3, 4, 5]#need an equal sign, to assign the list in a variale

    while local_variable > 0:
        if local_variable % 2 == 0:
            numbers.remove(local_variable)
        local_variable -= 1

    return numbers

my_set = {1, 2, 3, 4, 5, 5, 4, 3, 2, 1} 
result = process_numbers ()#removed the parameters

def modify_dict(): 
    local_variable = 10 
    my_dict['ke14'] = local_variable

modify_dict()#remove the parameter

def update_global():
    global global_variable
    global_variable += 10

for i in range(5):
    print(i)
    #"c += 1", unnecessary line

if my_set is not None and my_dict['ke14'] == 10: # change hone->None, m1_dict->my_dict
    print("Condition met!")# change wondition->condition

if 5 not in my_dict:
    print("5 not found in the dictionary!")

print(global_variable)
print(my_dict)
print(my_set)#change m1_set ->my_set