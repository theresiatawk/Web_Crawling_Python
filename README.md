# Web Crawling Project:

## Project Overview: 

* The goal of the project was to develop a Python script that could find files, directories, and subdomains for a given website URL.
* The script could be used to find hidden links that might take users to vulnerable pages. 
* Two text files were provided to read potential subdomains and directories in order to achieve this.

## Running the Project:

The script should accept an argument that represents the URL of the targeted website and must be run from the terminal using the command: 
```
python test_script.py 'target url'
``` 
## Output:
Three Files: 
* subdomains_output.bat containing all the subdomains that exist for the target url after running the script.
* directories_output.bat containig all the directories that exist for the target url after running the script.
* files_output.bat containing all the files and links that exist when fetching the content (html) of the domain and the content (html) of all its existing subdirectories
 using regular expressions. 

## Steps Taken to Complete the Project:

**1.** Begin by downloading the requests library which is needed in python to send URL to the server by unning the following command on the server: 
```
pip install requests
``` 
**2.** Search for a way to read from files in python and to write on them or delete their content
```
open("filepath", "r")
``` 
```
open("filepath", "a")
```
```
open("filepath", "w")
``` 
**3.** Subdomains Testing: 
* Loop over the text file containing prospective subdomains to test them, and then we appended them to the URL of the target website. 
* The Python requests library was then used to send a GET request to each of these URLs. 
* Consider the subdomain to be valid and added it to the sundomains_output.bat if the response status code was 200.

**4.** Directories Testing:
* Scan the text file containing probable directories
* Append them to the URL of the target website to test them
* The Python requests library was then used to send a GET request to each of these URLs
* Presume that the directory was valid and added it to the directories_output.bat file if the return status code was 200

**5.** Fetching files: 
* Look for patterns that could be applied to extract links from the HTML file.
* Develop a Python function that retreive the links and files from the HTML regular expressions
* Add all the retreived file to the files_output.bat

**6.** Testing the script: 
* Test the script on several websites

## Challenges:
**1.** One Challenge was the fact that thoroughly testing the code takes a lot of time. The problem was solved by running the code on a smaller test dataset.

**2.** The'requests' library was new to me which made it challenging to utilize and comprehend it. By doing research and figuring out how to use the library efficiently, this problem was solved.









