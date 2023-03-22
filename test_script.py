import requests
import sys
import re

if len(sys.argv) < 2:
    print("Please provide the url")
else: 
    target_url = sys.argv[1]
    print("URL: "+target_url) 

subdomains_output = []
directories_output = []

def testingSubdomains(target_url):
    try: 
        requests.get("http://"+target_url)
        input_file =  open("./input_files/subdomains_dictionary.bat", "r")
        subdomains_output_file = open("./subdomains_output.bat", "a")
        for line in input_file: 
            subdomain = line.strip()
            url = ""
            if subdomain[len(url)-1] == "." :
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
    except requests.exceptions.ConnectionError:
        print("No such domain")
    return subdomains_output

def fetshingHTML(target_url):
    try:
        response = requests.get("http://"+target_url)
    except requests.exceptions.ConnectionError:
        print("No such domain")

url1 = "google.com"
url2 = "testphp.vulnweb.com"
print(testingSubdomains(url1))
# fetshingHTML(url2)
# print(requests.get("https://" + url))