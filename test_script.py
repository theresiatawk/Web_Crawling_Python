import requests
import sys

if len(sys.argv) < 2:
    print("Please provide the url")
else: 
    first_arg = sys.argv[1]
    print("First arguemnt"+first_arg) 
def testingSubDomains(target_url):
    subdomains = [] 
    count = 0
    with open("./input_files/subdomains_dictionary.bat") as file:
        for line in file:
            
            url = line.strip()
            if url[len(url)-1] == "." :
                continue 
            print(url)
            new_url = url +"."+ target_url
            print(new_url)
            response = ""
            try: 
                response = requests.get("http://" + new_url)
                print(response)
            except requests.exceptions.ConnectionError:
                pass 
            if response != "":
                print(response)
            if response != "": 
                subdomains.append(new_url)
    return subdomains

url = "testphp.vulnweb.com"

print(testingSubDomains(url))
print(requests.get("https://" + url))