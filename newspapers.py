class newspaper:
    def __init__(self, title, urls):
        self.title = title
        self.urls = urls

    def __str__(self):
        return f"{self.title}: " + ", ".join(self.urls)

    def filter_urls(self, wanted_servers):
        self.urls = [url for url in self.urls if any(server in url for server in wanted_servers)]


wanted_titles = ['El Mundo', 'El País', 'Marca', 'La Provincia (Las Palmas)']
wanted_servers = ['dailyuploads.net']

def is_wanted_newspaper(title):
    return title in wanted_titles

def find_wanted_newspapers(soup):
    news_groups = []
    if soup:
        bb_wrappers = soup.find_all(class_='bbWrapper')
        for wrapper in bb_wrappers:
            text = wrapper.get_text().strip().split('\n')
            title = None
            urls = []
            for line in text:
                if line.startswith('----') and line.endswith('----'):
                    if title and urls and is_wanted_newspaper(title):
                        news_group = newspaper(title, urls)
                        news_group.filter_urls(wanted_servers)
                        news_groups.append(news_group)
                    title = line.strip('- ').strip()
                    urls = []
                elif line.startswith('http'):
                    urls.append(line.strip())
            if title and urls and is_wanted_newspaper(title):
                news_group = newspaper(title, urls)
                news_group.filter_urls(wanted_servers)
                news_groups.append(news_group)
    return news_groups