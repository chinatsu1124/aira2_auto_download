class Anime:
    name: str
    year: str
    keyword: str

    def __init__(self, name, year='', keyword=''):
        self.name = name
        self.year = year
        self.keyword = keyword

    def get_dir_name(self):
        return f'{self.name} ({self.year})'
