cities = {
    'تبریز': 'tabriz',
    'ارومیه': 'urmia',
    'اردبیل': 'ardabil',
    'اصفهان': 'isfahan',
    'کرج': 'karaj',
    'ایلام': 'ilam',
    'بوشهر': 'bushehr',
    'تهران': 'tehran',
    'شهرکرد': 'shahrekord',
    'بیرجند': 'birjand',
    'مشهد': 'mashhad',
    'بجنورد': 'bojnurd',
    'خوزستان': 'ahvaz',
    'زنجان': 'zanjan',
    'سمنان': 'semnan',
    'زاهدان': 'zahedan',
    'شیراز': 'siraz',
    'قزوین': 'qazvin',
    'قم': 'qom',
    'سنندج': 'sanandaj',
    'کرمان': 'kerman',
    'کرمانشاه': 'kermanshah',
    'یاسوج': 'yasuj',
    'گرگان': 'gorgan',
    'رشت': 'rasht',
    'خرم آباد': 'khorramabad',
    'ساری': 'sari',
    'اراک': 'arak',
    'بندر عباس': 'bandar-abas',
    'همدان': 'hamedan',
    'یزد': 'yazd'
}
def cityDictionary(city):
    if city in cities:
        return cities[city]
    return None
