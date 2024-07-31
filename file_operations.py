"""15. Write a Python module named file_operations.py with functions for reading, writing, and appending
data to a file."""

def file_writing(f_name, msg):
    f = open(f_name, 'w')
    f.write(msg)
    f.close()
    
def file_reading(f_name):
    f = open(f_name, 'r')
    print(f.read())
    
def file_appending(f_name, msg):
    f = open(f_name, 'a')
    f.write(msg)
    f.close()