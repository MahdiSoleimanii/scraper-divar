from bs4 import BeautifulSoup
import requests

divar_mashhad = requests.get('https://divar.ir/s/tehran').text
soup = BeautifulSoup(divar_mashhad, 'lxml')
ads = soup.find_all('div', class_="post-card-item")
ads_info = ''
for ad in ads:
    ad_title = ad.find('h2', class_="kt-post-card__title").text
    ad_price = ad.find('div', class_="kt-post-card__description")
    ad_location = ad.find('span', class_='kt-post-card__bottom-description kt-text-truncate').text
    ads_info += f'{ad_title}\n'
    if ad_price:
        ads_info += f'{ad_price.text}\n'
    else:
        ads_info += 'این آگهی کالا نیست\n'
    ads_info += f'{ad_location}\n'
    ads_info += '\n'
with open('ads.txt', 'w') as f:
    f.write(ads_info)