from bs4 import BeautifulSoup
import requests

def divarScraper(location, city):
    divar = requests.get(f'https://divar.ir/s/{city.lower()}').text
    soup = BeautifulSoup(divar, 'lxml')
    ads = soup.find_all('div', class_="post-card-item")
    ads_info = ''
    ad_counter = 0
    if location == '':
        ads_info += f'آگهی های اخیر شهر {city}\n\n'
    else:
        ads_info = f'آگهی های اخیر شهر {city} در منطقه {location}\n\n'
    for ad in ads:
        ad_title = ad.find('h2', class_="kt-post-card__title").text
        ad_price = ad.find('div', class_="kt-post-card__description")
        ad_location = ad.find('span', class_='kt-post-card__bottom-description').text
        zone_area = ad_location.split('در ')
        if (location in zone_area[-1] or location == zone_area[-1]) and location != '':
            ads_info += f'{ad_title}\n'
            if ad_price:
                ads_info += f'{ad_price.text}\n'
            else:
                ads_info += 'این آگهی کالا نیست\n'
            ads_info += '\n'
            ad_counter += 1
        elif location == '':
            ads_info += f'{ad_title}\n'
            if ad_price:
                ads_info += f'{ad_price.text}\n'
            else:
                ads_info += 'این آگهی کالا نیست\n'
            ads_info += f'{ad_location}\n'
            ads_info += '\n'
            ad_counter += 1
    ads_info += f'{ad_counter} آگهی در این فایل موجود است'
    with open('ads.txt', 'w') as f:
        f.write(ads_info)

divarScraper('', 'mashhad')