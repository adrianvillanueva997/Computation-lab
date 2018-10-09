import requests
from bs4 import BeautifulSoup
import random


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
        print(url)
    return match_list


def get_card_info(cards):
    for card in cards:
        html = make_request(card)
        matches = get_div_matches(html, div_class_name='col-md-3 col-sm-12 col-xs-12')
        for match in matches:
            a = match.text


if __name__ == '__main__':
    class_to_find = 'col-md-2 col-sm-3 col-xs-6 '
    card_links = []
    limit = 2
    i = 1
    while i < limit:
        url = 'https://www.playartifact.info/cards/all/?page=' + str(i)
        print('[INFO] Connecting to: ', url)
        html = make_request(url)
        matches = get_div_matches(html, class_to_find)
        card_list = get_card_links(matches)
        print(len(card_list))
        if len(card_list) != 0:
            limit = limit + 1
            i = i + 1
            for card in card_list:
                card_links.append(card)
        else:
            i = limit
    with open('export.txt', 'w', encoding='utf-8') as file:
        for card in card_links:
            file.write(card)
            file.write('\n')
