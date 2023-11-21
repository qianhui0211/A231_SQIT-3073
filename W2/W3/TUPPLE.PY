ID_database = [] 
create_ID_input = str(input('Create ID:')) 

create_ID_input_type=str(create_ID_input)
ID_database.append(create_ID_input_type)


Input_ID = input('Input ID:') 

Input_ID_type=str(Input_ID)
if Input_ID_type in ID_database:
 print("Available")
else:
 print("Not Available")


