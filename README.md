Opinion Scrapper Test
===================

## DESCRIPTION ##

This program reads a list from opinios from http://www.cadc.uscourts.gov/internet/opinions.nsf and stores the results in a json file.

It has also a minimal web GUI to display the results.

## USAGE ##

Simply run getOpinions.py.

   $ python getOpinions.py 
   Retrieving opinions from URL...
   OK, 1 opinions retrieved.

The small web GUI was written in Flask.

   $python run.py
   * Running on http://127.0.0.1:5000/

   Then open the URL in your web browser.

## Installation

   pip install -r requirements.txt

Developed on Python 2.7.8 with this enviroment:

Flask is required for de web GUI
beautifulsoup4 is required for the scraping script.

Package version details are on requirements.txt file.


