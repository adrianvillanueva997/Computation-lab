import requests
from bs4 import BeautifulSoup


def make_request(url):
    """

    :type url: str
    """
    headers = {'User-Agent': 'Mozilla/5.0'}
    request = requests.get(url=url, headers=headers)
    print(request)
    html = request.content
    return html


def get_div_matches(html, div_class_name):
    soup = BeautifulSoup(html, 'html.parser')
    matches = soup.findAll("div", class_=div_class_name)
    return matches


def get_card_links(matches):
    match_list = []
    for match in matches:
        a = match.find('a')
        url = a.attrs['href']
        match_list.append(url)
        # print(url)
    return match_list


def get_card_info(cards):
    for card in cards:
        html = make_request(card)
        matches = get_div_matches(html, div_class_name='col-md-3 col-sm-12 col-xs-12')
        for match in matches:
            a = match.text


if __name__ == '__main__':
    class_to_find = 'col-md-2 col-sm-3 col-xs-6 '
    card_info = []
    for i in range(1, 12):
        url = f'https://www.playartifact.info/cards/all/?page={i}'
        print('[INFO] Connecting to: ', url)
        html = make_request(url)
        matches = get_div_matches(html, class_to_find)
        card_list = get_card_links(matches)
        get_card_info(card_list)
