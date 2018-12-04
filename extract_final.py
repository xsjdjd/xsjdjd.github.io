# Reads a folder of pdf files, extract certain information, write in db
import PyPDF2
import os
import re
from cs50 import SQL

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///eval.db")

def extract_text(name):
    # Extracts text to list
    try:
        with open(os.path.join('./evaluations', name), "rb") as object:
            reader = PyPDF2.PdfFileReader(object)
            page = reader.getPage(0).extractText()
            page = page.replace('-','').replace('\n','').split()
        return page

    except:
        return 1

def extract_info(page):
    # Extracts first name, last name, class size, average rating of class, class name and year

    # Check if text extracted from pdf file and converted to list successfully
    if not isinstance(page, list):
        return 2

    # Check formatting, make sure I can extract prof name
    if "Prof." not in page and "Dean" not in page:
        return 3

    # Get position of Professor's name
    if "Prof." in page:
        pos = page.index("Prof.")
    else:
        pos = page.index("Dean")

    # Check if I can extract class size, which is right behind professor name
    size = page[pos + 3]
    if not size.isnumeric():
        return 4

    # Eliminate data if class size is too small
    size_thresh = 6
    size = int(size)
    if size < size_thresh:
        return 5

    # Error checking for class name and year
    if "Code:" not in page:
        return 6
    if "Semester:" not in page:
        return 7

    # Find rating, assuming it's the only string that contains a "." e.g. "5.00"
    temp_list = page[page.index("teacher") + 1 : page.index("1Not")]
    for num in temp_list:
        if "." in num:
            break
    num = float(num)

    # Find class name
    name = " ".join(page[page.index("Code:")+ 2 : page.index("1L")])

    # Find class year, semester
    year = int(page[page.index("Semester:")+ 2])
    sem = page[page.index("Semester:")+ 1]

    return page[pos + 1], page[pos + 2], size, num, name, year, sem


# Check if info extracted should be excluded from database
def info_failed(file):
    text = extract_text(file)
    info = extract_info(text)

    # if info is an int, that means error was returned
    if isinstance(info, int):
        return True
    return False


def insert(file_name):
    text = extract_text(file_name)

    # First name, last name, class size, average rating, class name, year, semester
    info = extract_info(text)

    # if info is an int, that means error was returned
    if not isinstance(info, int):
        db.execute(f"INSERT INTO eval (first_name, last_name, class_size, avg_rating, class_name, year, sem)\
                            VALUES(:first_name, :last_name, :class_size, :avg_rating, :class_name, :year, :sem)",
                            first_name = info[0],
                            last_name = info[1],
                            class_size = info[2],
                            avg_rating = info[3],
                            class_name = info[4],
                            year = info[5],
                            sem = info[6]
                            )
        return 0

    # Can't insert successfully
    return 8


def main(path):
    filelist = os.listdir(path)
    i = 0
    for file in filelist:
        # Use regex to eliminate files that don't need to be read
        if re.match("(.*)_0\d*(.*)", file) or re.match("(.*)Spring201[12]*(.*)", file) or re.match("(.*)Fall201[12]*(.*)", file):
            continue

        # Ignore data if extraction is problematic
        elif info_failed(file):
            continue

        else:
            insert(file)

if __name__ == "__main__":
    main("/home/ubuntu/workspace/project/evaluations")