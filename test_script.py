import requests
import sys
import re
from urllib.parse import urljoin

if len(sys.argv) < 2:
    print("Please provide the url")
else: 
    target_url = sys.argv[1]
    print("URL: "+target_url) 

subdomains_output = []
directories_output = []

def testingSubdomains(target_url):
    open("./subdomains_output.bat", "w").close()
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

def testingDirectories(target_url):
    open("./directories_output.bat", "w").close()
    try:
        requests.get("http://"+target_url)
        input_file =  open("./input_files/dirs_dictionary.bat", "r")
        directories_output_file = open("./directories_output.bat", "a")
        for line in input_file: 
            directory = line.strip()
            url = target_url +"/"+ directory
            print(url)
            try:
                response = requests.get("http://" + url)
                if response.status_code == 200:
                    directories_output.append(url)
                    directories_output_file.write(url +"\n")
                    print(f"This directory {url} exist !!!!!!!!!!!!!!!")
                    print(directories_output)
            except requests.exceptions.ConnectionError:
                pass
        input_file.close()
        directories_output_file.close()
    except requests.exceptions.ConnectionError:
        print("No such domain")
    return directories_output
    

def fetshingFiles(target_url):
    open("./files_output.bat", "w").close()
    files_output_file = open("./files_output.bat", "a")
    try:
        response = requests.get("http://"+target_url)
        links =  re.findall('href="(.*?)"', response.content.decode('utf-8'))
        for link in links:
            files_output_file.write(link +"\n")
        files_output_file.close()
        return links
    except requests.exceptions.ConnectionError:
        return "No such domain"
  
url1 = "google.com"
url2 = "testphp.vulnweb.com"
# print(testingSubdomains(url1))
# print(fetshingFiles(url2))
print(testingDirectories(url1))