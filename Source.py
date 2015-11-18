import urllib.request


def main():
    print("Enter the name of the article: ")
    a = input()
    nextLink = inputarticle(a)
    if(nextLink == None):
        return
    while not(nextLink == "Philosophy"):
        print(nextLink)
        nextLink = inputarticle(nextLink)
    print ("Philosophy!")
    return True

def inputarticle(a):
    nextLink = ""
    b = "http://en.wikipedia.org/wiki/" + a
    try:
        file = urllib.request.urlopen(b)
    except:
        print("Bad article name. Could not find.")
        return None
    page = file.read().decode("utf-8")
    nextLinkStart = page.find("<p>")
    nextLinkStart = page.find("a href=\"/wiki/", nextLinkStart)
    nextLinkStart += 14
    while((page[nextLinkStart:nextLinkStart+8] == "Category") |
              (page[nextLinkStart:nextLinkStart+9] == "Wikipedia") |
              (page[nextLinkStart:nextLinkStart+4] == "Help")|
              (page[nextLinkStart:nextLinkStart+4] == "File")):
        nextLinkStart = page.find("a href=\"/wiki/", nextLinkStart)
        nextLinkStart += 14
    while(page[nextLinkStart] is not "\""):
        nextLink += page[nextLinkStart]
        nextLinkStart += 1
    return nextLink

stop = False
while stop == False:
    error = main()
    if error == None:
        main()
    else:
        print("Would you like to try again? y/n")
        answer = input()
        if('n' in answer):
            stop = True
            print("Thanks for playing!")