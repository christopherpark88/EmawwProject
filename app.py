import xml.etree.ElementTree as ET
import json
import redis
import argparse
import os

# Access the REDIS_HOST environment variable
redis_host = os.getenv("REDIS_HOST")
redis_port = os.getenv("REDIS_PORT")
cache = redis.Redis(host=redis_host, port=redis_port, decode_responses=True)

def parseXML(xmlPath):
    # Parse the XML file and extract data
    # Return subdomains and cookie data
    print("----------PARSING XML----------")
    tree = ET.parse(xmlPath)
    root = tree.getroot()

    subdomainsData = []
    for subdomain in root.iter('subdomain'):
        subdomainsData.append(subdomain.text)

    cookiesData = []
    for cookie in root.iter('cookie'):
        cookiesData.append((cookie.attrib['name'], cookie.attrib['host'], cookie.text))
    
    print("----------FINISHED PARSING XML----------\n")
    return {'subdomains': subdomainsData, 'cookies': cookiesData}
    

def redisSave(subdomains, cookies):
    print("----------SAVING TO REDIS----------")
    # Convert subdomains object to JSON
    subdomainsJSON = json.dumps(subdomains)

    # Store subdomains as JSON in a Redis Key
    cache.set('subdomains', subdomainsJSON)

    for name, host, value in cookies:
        cookieKey = 'cookie:' + name + ':' + host 
        cache.set(cookieKey, value)

    print("----------FINISHED SAVING TO REDIS----------\n")
    return None

def printRedisKeys():
    print("----------PRINTING REDIS KEYS----------")
    keys = cache.keys('*')
    for key in keys:
        print("Redis Key: " + key)
    print("----------FINISHED PRINTING REDIS KEYS----------\n")

def main():
    parser = argparse.ArgumentParser(description="Export data from XML to Redis Keys")
    parser.add_argument("xml_path", help="Path to the XML file")
    parser.add_argument("-v", "--print", action="store_true", help="Print keys saved to Redis")
    args = parser.parse_args()

    parsedData = parseXML(args.xml_path)

    subdomains = parsedData['subdomains']
    cookies = parsedData['cookies']

    redisSave(subdomains, cookies)

    if args.print:
        printRedisKeys()
    
    print("----------COMPLETED EXECUTION----------")

if __name__ == "__main__":
    main()