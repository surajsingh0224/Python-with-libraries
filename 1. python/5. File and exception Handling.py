from pathlib import Path

def readFileandFolder():
    path = Path('')
    items = list(path.rglob('*'))
    for i, items in enumerate(items):
        print(f"{i+1} : {items}")
        
    
    
    
def createfile():
    try:
        readFileandFolder()
        name = input("Enter file name with extension: ")
        p = Path(name)
        if not p.exists():
            with open(p, 'w') as fs:
                data = input("Enter data to write in file: ")
                fs.write(data)
            print(f"File '{name}' created successfully.")
        else:
            print(f"File '{name}' already exists.")
    
    except Exception as e:
        print(f"An error occurred: {e}")

print("Press 1 for creating a file")
print("Press 2 for reading a file")
print("Press 3 for Update a file")
print("Press 4 for Delete a file")

check = int(input("Enter your choice: "))
if check == 1:
    createfile()
    