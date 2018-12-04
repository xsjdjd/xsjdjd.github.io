# User's Manual

## What is the title of the project?
HLS Course Ratings

## What does it do?
HLS Course Ratings is a website that:
    1) Presents data gathered (by a script) about instructors' ratings. The ratings are based on student evaluations about the
        teacher's "overall effectiveness."
    2) Allows users to search for specific instructors based on their last names.

## How do I run the project?
In the terminal, cd to project/webpage. Then type in "flask run."

## Which files are included in the project?
Files included are:
    1) HTML files for the webpage, including a layout file (layout.html) and files extending the layout file.
    2) a Python file, application.py. The python file uses Flask to run the website.
    3) a database file, eval.db, which contains the information stored in the database.
    4) a Python file, extract_final.py, which was used to extract information from pdf files and store it in eval.db.

Files NOT included are:
    1) The underlying pdf files where the information was located. There are around 1,600 pdf files with a size of 300MB in total.
    I thought it probably wouldn't be needed, but they're stored in my CS50 IDE.

