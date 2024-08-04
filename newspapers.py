class newspaper:
    def __init__(self, title, urls):
        self.title = title
        self.urls = urls

    def __str__(self):
        return f"{self.title}: " + ", ".join(self.urls)

wanted_titles = ['El Mundo', 'El País', 'Marca', 'La Provincia (Las Palmas)']

wanted_titles = ['El Mundo', 'El País', 'Marca', 'La Provincia (Las Palmas)']

def is_wanted_title(title):
    return title in wanted_titles

def extract_news_groups(soup):
    news_groups = []
    if soup:
        bb_wrappers = soup.find_all(class_='bbWrapper')
        for wrapper in bb_wrappers:
            text = wrapper.get_text().strip().split('\n')
            title = None
            urls = []
            for line in text:
                if line.startswith('----') and line.endswith('----'):
                    if title and urls and is_wanted_title(title):
                        news_groups.append(newspaper(title, urls))
                    title = line.strip('- ').strip()
                    urls = []
                elif line.startswith('http'):
                    urls.append(line.strip())
            if title and urls and is_wanted_title(title):
                news_groups.append(newspaper(title, urls))
    return news_groups

def find_wanted_newspapers(soup):
    return extract_news_groups(soup)