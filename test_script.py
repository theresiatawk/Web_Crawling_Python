import requests
import sys

if len(sys.argv) < 2:
    print("Please provide the url")
else: 
    target_url = sys.argv[1]
    print("URL: "+target_url) 

def testingSubdomains(target_url):
    subdomains_output = []
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
                subdomains_output.append(new_url)

    with open("./subdomains_output.bat", "a") as subdomains_file:
        for element in subdomains_output:
            subdomains_file.write(element +"\n")
    
    return subdomains_output

url = "testphp.vulnweb.com"

print(testingSubdomains(url))
print(requests.get("https://" + url))