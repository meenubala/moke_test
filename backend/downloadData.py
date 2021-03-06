import urllib.request
import bs4 as bs

def call_back(myurl):
    toremove = dict.fromkeys((ord(c) for c in u'\xa0\n\t'))
    # Fetch the html file
    response = urllib.request.urlopen(myurl)
    html_doc = response.read()

    # Parse the html file
    soup = bs.BeautifulSoup(html_doc, 'lxml')

    # Get question ans. data
    details_ques_ans = soup.find(class_="details_ques_ans")
    i = 1

    for line in details_ques_ans.find_all("span"):
        #print(line.get_text(), len(line.get_text()))
        if(len(line.get_text()) >= 1):
            for text in line.contents:
                try:
                    text = text.translate(toremove)
                    if len(text):
                        print(i, text)
                        i += 1
                except:
                    print(i, text)
                    i += 1
    answer = soup.find(class_="ans_panel")
    print(i, answer.get_text())

if __name__ == "__main__":
    for i in range(50):
        myurl = 'https://www.studyadda.com/sample-papers/neet-sample-test-paper-83_q1/1296/' + str(403162 + i)
        call_back(myurl)
