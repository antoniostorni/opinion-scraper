import urllib2
from bs4 import BeautifulSoup
import json
import sys

#URL = "http://www.cadc.uscourts.gov/internet/opinions.nsf"
URL = "http://www.cadc.uscourts.gov/internet/opinions.nsf/OpinionsByMonday?OpenView&StartKey=201411&Count=8&scode=3"
RESULT_FILE = "result.json"


def main():

    print "Retrieving opinions from URL..."
    
    try:
        data = urllib2.urlopen(URL).read()
    except:
        print "Error retrieving opinions"
        raise

    soup = BeautifulSoup(data)
        
    #  We have 1 opinion every 2 row-entry classes, so we use step 2
    rows = soup.find_all("div", class_="row-entry")[::2]

    if not rows:
        print "No opinions available."
    else:
    
        response = []

        #  We have 1 opinion every 2 row-entry classes, so we use step 2

        #  for div in range(0,rows_count,2):
        for entry in rows:
            opinion = {}
            opinion['opinion_number']  = entry.find("a").contents[0]
            opinion['title'] = entry.find("span", class_="column-two").contents[0]
            opinion['date'] = entry.nextSibling.find("span", class_="column-two").contents[0]
        
            response.append(opinion)

        result = open(RESULT_FILE, 'w')
        result.write(unicode(json.dumps(response, ensure_ascii=False)))

        print "OK, " + str(len(rows)) + " opinions retrieved."


if __name__ == "__main__":
    main()
    sys.exit()

