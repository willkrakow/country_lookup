import socket
import ipinfo
import csv
import tldextract
import os
import sys

def main():
    # Initialize ipinfo handler
    access_token = os.getenv("IPINFO_ACCESS_TOKEN")
    handler = ipinfo.getHandler(access_token)

    # Import csv and add data to websites list
    inputfile = os.getenv("INPUT_CSV")
    outputfile = os.getenv("OUTPUT_CSV")

    websites = []
    country_websites = []

    country_code = sys.argv[0] or "US"
    # Read out lines from input file to websites array
    with open(inputfile, 'r') as data:
        for line in csv.DictReader(data):
            websites.append(line)

    # Loop over websites array, get host name and then ip details
    for website in websites:
        ext = tldextract.extract(website["url"])
        domain = '.'.join(ext[1:])
        ip = socket.gethostbyname(domain)
        details = handler.getDetails(ip)
        website["url"] = domain
        website["country"] = details.country
        website["ip"] = ip
        print(ip)
        if website["country"] == country_code:
            country_websites.append(website)

    #Write results to output csv file
    with open(outputfile, mode='w') as contact_file:
        output_writer = csv.writer(
            contact_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for website in country_websites:
            output_writer.writerow(
                [website['name'] or "", website['url'], website['email'] or ""])


if __name__ == "__main__":
    main()
