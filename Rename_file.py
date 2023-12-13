import datetime
import os
import re
import time
from tkinter import filedialog

import pathvalidate


def get_file_type(file):
    base,file_extension = os.path.splitext(file)
    return file_extension

def get_split_sentence(sentence):
    # Change what punctuation or character you need the sentence to be split by

    Split_punctuation = r'[ ,._]'
    result = re.split(Split_punctuation, sentence)
    return result

def get_date():
    time.sleep(0.5)
    now = datetime.datetime.now()
    new_date = str(now)
    new_date = new_date.replace(":", "-").replace(" ", "__").replace(".", "-")
    return new_date

def rename_in_order(filename, folder_address, skip_file_with_no_numbers=True):
    for file in os.listdir(folder_address):
        # print(file)

        file_type = get_file_type(file)
        # print(file_type)

        old_file_path = os.path.join(folder_address, file)
        # print(old_file_path)
        if os.path.isdir(old_file_path):
            print(f"{file} is a directory...skipping")
            pass
        else:
            res = [i for i in get_split_sentence(file) if i.isdigit()]
            if res == [] and skip_file_with_no_numbers == True:
                print(f"Skipping {file} - No number found")
                pass

            elif res == [] and skip_file_with_no_numbers == False:

                new_date = get_date()

                new_filename = f"{filename} {new_date}{file_type}"
                new_file_path = os.path.join(folder_address, new_filename)

                # An existing path is impossible due to the new_date function so only the else statement will run
                if os.path.exists(new_file_path):
                    print(f"File '{new_filename}' already exists.")
                else:
                    os.rename(old_file_path, new_file_path)
                    print(f"{old_file_path} ----> {new_file_path}")

            else:

                end_number = str(res[-1])
                print(f"OG:::: {filename}")
                new_filename = f"{filename} {end_number}{file_type}"
                new_file_path = os.path.join(folder_address, new_filename)

                if os.path.exists(new_file_path):
                    print(f"File '{new_filename}' already exists. Adding date/time to file name")
                    new_date = get_date()
                    new_filename = f"{filename} ({end_number} - copy) {new_date}{file_type}"
                    new_file_path = os.path.join(folder_address, new_filename)
                    os.rename(old_file_path, new_file_path)
                else:
                    os.rename(old_file_path, new_file_path)
                    print(f"{old_file_path} ----> {new_file_path}")


def indiscriminate_rename(filename, folder_address):
    i = 1
    for file in os.listdir(folder_address):

        # Converting files to date time so all files are unique
        # This prevents duplication errors later when renaming the files

        file_type = get_file_type(file)
        old_file_path = os.path.join(folder_address, file)

        # Ignore file directory so it doesn't get renamed
        if os.path.isdir(old_file_path):
            print(f"{file} is a directory...skipping")
            pass
        else:

            new_date = get_date()
            new_filename = f"{new_date}{file_type}"
            print(new_filename)
            new_file_path = os.path.join(folder_address, new_filename)

            os.rename(old_file_path, new_file_path)



    for file in os.listdir(folder_address):

        # Renaming files to their proper names

        file_type = get_file_type(file)
        print(f"{file} has file type: {file_type}")
        old_file_path = os.path.join(folder_address, file)

        # Ignore file directory so it doesn't get renamed
        if os.path.isdir(old_file_path):
            print(f"{file} is a directory...skipping")
            pass
        else:
            new_filename = f"{filename} {i}{file_type}"
            print(new_filename)
            new_file_path = os.path.join(folder_address, new_filename)
            os.rename(old_file_path, new_file_path)
            i += 1

def menu():

    print("What should the name of the file be?")
    name_of_file = input()

    while (pathvalidate.is_valid_filename(name_of_file)) != True:
        print(f"{name_of_file} is NOT a valid filename, please choose another file name")
        name_of_file = input()

    print(f"{name_of_file} is a valid filename")


    print("Select the folder where the files are located in?")
    path = filedialog.askdirectory()
    print(f"{path} is the folder you selected\n\n")


    print("Press 1 if you want to skip files that don't have a number in them.\n"
          "Press 2 Add a date and time to files without numbers or duplicates.\n"
          "press 3 for an indiscriminate renaming of all files.\n"
          "Press 4 to quit.\n\n")


    option = input()
    if option == "1":
        rename_in_order(name_of_file, path)
    elif option == "2":
        rename_in_order(name_of_file, path, skip_file_with_no_numbers=False)
    elif option == "3":
        indiscriminate_rename(name_of_file, path)
    elif option == "4":
        quit()
    else:
        menu()





menu()


