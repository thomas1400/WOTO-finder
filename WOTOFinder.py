import urllib.request
import time
from datetime import datetime
import webbrowser

if __name__ == "__main__":

    print("~~When's the WOTO?~~")
    print("A simple script to tell you when the WOTO opens.\n")

    print("NOTE: Making a selection in the console will pause the program. Press ESC to resume.\n")

    w = ''
    while True:
        w = input("Which WOTO would you like to check? (1 or 2) \n>")
        if w == '1' or w == '2':
            w = int(w)
            break
        print("Please enter either 1 or 2.\n")
        time.sleep(0.25)
    print()

    # Read the WOTO link from the dates page.
    html_links = urllib.request.urlopen(
        'https://docs.google.com/document/d/1KJFW38fXnbep-e1lHIc4H1Nq0zea-y4rqtv4xtfmM6g/edit'
        ).read()

    # Retrieve last 3 bit.ly links from the class links website. Determine the first WOTO link.
    # If the third one is a WOTO, use the second. If the third one is not a WOTO, use the first.
    loc3 = str(html_links).rfind('bit.ly') - 7
    end3 = str(html_links)[loc3:].find('\"') + loc3
    html_test3 = urllib.request.urlopen(
        str(html_links)[loc3: end3]
        ).read()
    nonwotolinkexists = 'WOTO' not in str(html_test3)

    loc2 = str(html_links)[0:loc3].rfind('bit.ly') - 7
    end2 = str(html_links)[loc2:].find('\"') + loc2

    loc1 = str(html_links)[0:loc2].rfind('bit.ly') - 7
    end1 = str(html_links)[loc1:].find('\"') + loc1

    if nonwotolinkexists and w == 1:
        woto_link = str(html_links)[loc1:end1]
    elif (nonwotolinkexists and w == 2) or (not nonwotolinkexists and w == 1):
        woto_link = str(html_links)[loc2:end2]
    else:
        woto_link = str(html_links)[loc3:end3]

    print(woto_link)

    # If automatic WOTO fetching doesn't work, use this questionable link construction based on observation.
    # months = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']
    #
    # woto_link = 'https://bit.ly/201fall19-' + months[datetime.now().month-1] + str(datetime.now().day) + "-1"
    # print(woto_link)

    # Check the WOTO every 10 seconds to see if it's accepting responses.
    closed = True
    while closed:
        html_woto = urllib.request.urlopen(
            woto_link
            ).read()
        if 'no longer accepting responses' in str(html_woto):
            print('--- Not open. ---')
            time.sleep(10)
        else:
            print('-#-#- WOTO open! -#-#-')
            print('Opening WOTO in default browser and closing program...')
            webbrowser.open(woto_link)
            closed = False
