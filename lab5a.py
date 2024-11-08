#!/usr/bin/env python3
# Author ID: yahmad4

def read_file_string(file_name):
    """
    Takes file_name as a string for a file name, 
    returns its entire contents as a single string.
    """
    try:
        with open(file_name, 'r') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: The file {file_name} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

def read_file_list(file_name):
    """
    Takes file_name as a string for a file name,
    returns its entire contents as a list of lines 
    without new-line characters.
    """
    try:
        with open(file_name, 'r') as file:
            return [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        print(f"Error: The file {file_name} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    file_name = 'data.txt'
    print(read_file_string(file_name))
    print(read_file_list(file_name))
