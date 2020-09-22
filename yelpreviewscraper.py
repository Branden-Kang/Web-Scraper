import urllib3
import bs4
import sys

http = urllib3.PoolManager()


def get_reviews(url):
    reviews = ''
    has_next_page = False
    try:
        response = http.request('GET', url)
    except urllib3.exceptions.HTTPError, e:
        print('HTTPError = ' + str(e))
        return
    except Exception, e:
        print("Error = " + str(e))
        return

    soup = bs4.BeautifulSoup(response.data)
    next_page_button = soup.findAll('a',
                                    {"class": "page-option prev-next next"})
    review_content = soup.findAll('p', {"itemprop": "description"})

    product_name = soup.select('h1.biz-page-title')[0].text

    if(len(review_content)) == 0:
        print("An error has occured. No review content was found.")
        return

    if len(next_page_button) != 0:
        has_next_page = True

    for node in review_content:
        reviews += node.text

    page_num = 1
    while has_next_page:
        response = http.request('GET', (url + "?start=" + str(page_num*40)))
        soup = bs4.BeautifulSoup(response.data)
        next_page_button = soup.findAll('a',
                                        {"class":
                                         "page-option prev-next next"})
        review_content = soup.findAll('p', {"itemprop": "description"})

        for node in review_content:
            reviews += node.text + '\n\n'

        if len(next_page_button) == 0:
            has_next_page = False
        page_num = page_num + 1

    return product_name.strip(), reviews
