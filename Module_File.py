def write_to_a_file(filename,texts):
    with open(filename,'w') as file:
            file.write(texts)
 
def read_a_file(filename):
    try:
        with open(filename,'r') as file:
            print(file.read())
    except FileNotFoundError:
        print("Error : File does not exist")
 
def append_to_a_file(filename,texts):
    with open(filename,'a') as file:
         file.write(texts)