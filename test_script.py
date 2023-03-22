import requests
import sys
import re


# Initializing empty arrays
subdomains_output = []
directories_output = []
files_output = []

# Clearing the content of all the files first
open("./subdomains_output.bat", "w").close()
open("./directories_output.bat", "w").close()
open("./files_output.bat", "w").close()


# Function that test for posible existing subdomain for a given domain
def testingSubdomains(target_url):
    try: 
        requests.get("http://"+target_url)
        input_file =  open("./input_files/subdomains_dictionary.bat", "r")
        subdomains_output_file = open("./subdomains_output.bat", "a")
        for line in input_file: 
            subdomain = line.strip()
            if subdomain[len(subdomain)-1] == "." :
                url = subdomain +""+ target_url
            else:
                url = subdomain +"."+ target_url
            print(url)
            try: 
                response = requests.get("http://" + url)
                if response.status_code == 200:
                    subdomains_output.append(url)
                    subdomains_output_file.write(url +"\n")
                    print(f"This subdomain exist {url} !!!!!!!!!!!!!!!")
                    print(subdomains_output)
            except requests.exceptions.ConnectionError:
                pass
        input_file.close()
        subdomains_output_file.close()
    except requests.exceptions.ConnectionError:
        print("No such domain")
    return subdomains_output

# Function that test for posible existing directories for a given domain
def testingDirectories(target_url):
    try:
        requests.get("http://"+target_url)
        input_file =  open("./input_files/dirs_dictionary.bat", "r")
        directories_output_file = open("./directories_output.bat", "a")
        for line in input_file: 
            directory = line.strip()
            url = target_url +"/"+ directory
            try:
                response = requests.get("http://" + url)
                if response.status_code == 200:
                    directories_output.append(url)
                    directories_output_file.write(url +"\n")
                    # Fetching the files for each existing subdirectory of the domain
                    print(fetchingFiles(url))
                    print(f"This directory {url} exist !!!!!!!!!!!!!!!")
            except requests.exceptions.ConnectionError:
                pass
        input_file.close()
        directories_output_file.close()
    except requests.exceptions.ConnectionError:
        print("No such directory")
    return directories_output
    
# Function that fetch all the link files of a url using regex
def fetchingFiles(target_url):
    files_output_file = open("./files_output.bat", "a")
    try:
        response = requests.get("http://"+target_url)
        files_output =  re.findall('href="(.*?)"', response.content.decode('utf-8'))
        for link in files_output:
            files_output_file.write(link +"\n")
        files_output_file.close()
        return files_output
    except requests.exceptions.ConnectionError:
        return "No such file"

# Checking for arguments
if len(sys.argv) < 2:
    print("Please provide a url without the 'www.'")
else: 
    target_url = sys.argv[1]
    print("URL: "+target_url)
    # testingSubdomains(target_url)
    # testingDirectories(target_url)
    # fetchingFiles(target_url)

# Bonus part

url = "https://requestswebsite.notanothercoder.repl.co/confirm-login"

def send_request(username, password): 
    form_data = {
        "username": username,
        "password": password
    }
    response = requests.post(url, data=form_data)
    print(response.text)

send_request("1","1")