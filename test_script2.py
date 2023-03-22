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
    with open("./input_files/subdomains_dictionary_copy.bat") as file:
        count = 0
        for line in file: 
            count += 1 
            subdomain = line.strip()
            if count == 100:
                break
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
            except requests.exceptions.Timeout:
                print(f"Connection to {subdomain}.{url} timed out.")
            except requests.exceptions.RequestException as e:
                print(f"An error occurred while connecting to {subdomain}.{url}: {e}")
            if response != "":
                # print("Subdomain found: " + ", ".join([res.decode() for res in response]))                
                subdomains_output.append(url)
                print(subdomains_output)

    with open("./subdomains_output.bat", "a") as subdomains_file:
        for element in subdomains_output:
            subdomains_file.write(element +"\n")
    
    return subdomains_output

url = "testphp.vulnweb.com"

print(testingSubdomains(url))
print(requests.get("https://" + url))