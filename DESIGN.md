# DESIGN

## The original idea
HLS has a website where course evaluations are published in pdf files. I wanted to extract some of that information and publish
them in a website. That way, students can more easily search/view the information, without having to download and open each pdf
to view the information file.

## Downloading the files

The website publishes the pdf files sort of like this:

  --Professor Name
  --Class Name: 2001 2002 2003 ... 2018

Wherethe years are hyperlinks to the pdf file

I decided that the best way to extract the information would be to first download the files, then use a script to extract
information inside.

After some trial and error, I decided the best way to download the files would be using wget. Unfortunately I don't have the
command stored. But it involved using wget command that:
    1) accesses the page,
    2) allows me to type in my username and password in the terminal (since the files are password protected),
    3) download all pdf files and store in the same folder.

## Extracting the information
Unfortunately, the files have different naming conventions, depending on the year. Moreover, the pdf files were also formatted
in a different way in the early 2000s and in the late 2000s. (As in, the information are located in different parts of the file).
I decided the best way to deal with the problem is to limit my data extraction to the past 5 years, where the pdf files follow the
same format.

Thus, I decided that my program would extract certain information from the pdf files that are:
  -from 2013 onwards;
  -with a class size above 6;

### Steps of extracting information
1) I extracted text from one of the pdf files using PyPDF2. Then I removed white space and split the words into a list.
2) There were some types of information that I wanted (e.g. name of prof, class name, ratings). I used file.index("xxx")
to determine the position of that information in the list. I wrote a function to perform this and the previous step.
3) Because pdf files from 2013 onwards follow the same format, I can apply the functions to all pdf files since 2013.

### Error checking and enter into database
I did some debugging, but because thorough debugging can take too much time, I decided to limit my dataset to those that I can
successfully extract information from. I wrote errorchecking codes and skipped files where errors happend.

In the end, around 600 out of 1700 files were successfully extracted from. Much of the remaining files were from before 2013 (and
thus may have had different formatting). I don't know what proportion of post-2013 files were successfully read, although I suspect
it's a high proportion.

### Select which pdf files to extract from
I used regex to make sure files that I knew are before 2013 are excluded (e.g. if title contained "2009".) I relied on errorchecking
to get rid of the other data.

## Displaying on the website
I then displayed the information on a website. The basics parts are straightforward. However, I had a lot of trouble trying to use
SQL to customize the data that I wanted to input/display.

For example, I tried to create an ID for each professor, and link each class with a professor in SQL. I.e. if the first and last
names of the class instructor matches a professor's, the class would be associated with the prof's ID. But I couldn't figure out
how to do it.

Because of this, I limited the number of features in the project. It currently displays all ratings of classes, sorted by professor
name, then class name, then year.

### Search function
The website also has a search function based on keywords in the data. I originally had a search page implemented with Python, until
I came accross Datatables (https://datatables.net). I realized that Datatables is a much better implementation and incorporated it
into my website.