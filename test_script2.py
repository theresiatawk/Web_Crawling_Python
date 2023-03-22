import requests
import sys

if len(sys.argv) < 2:
    print("Please provide the url")
else: 
    target_url = sys.argv[1]
    print("URL: "+target_url) 

subdomains_output = []
directories_output = []

def testingSubdomains(target_url):
    try: 
        requests.get("https://"+target_url)
        with open("./input_files/subdomains_dictionary_copy.bat") as file:
            for line in file: 
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
                        print(f"This subdomain exist {url} !!!!!!!!!!!!!!!")
                        print(subdomains_output)
                except requests.exceptions.ConnectionError:
                    pass
        with open("./subdomains_output.bat", "a") as subdomains_file:
            for element in subdomains_output:
                subdomains_file.write(element +"\n")
    except requests.exceptions.ConnectionError:
        print("No such domain")
    return subdomains_output

url = "google.com"

print(testingSubdomains(url))
print(requests.get("https://" + url))