class Anime:
    name: str
    year: str
    keyword: str
    season: str

    def __init__(self, name, year, keyword, season):
        self.name = name
        self.year = year
        self.keyword = keyword
        self.season = season

    def get_dir_name(self):
        return f'{self.name} ({self.year})'
