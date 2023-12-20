from dataclasses import dataclass, field

@dataclass
class PubmedSearcherConfig:
    query: str = field(default=None)
    num_of_articles: int = field(default=50)
    folder_to_save: str = field(default='./articles')
    email: str = field(default=None)
    