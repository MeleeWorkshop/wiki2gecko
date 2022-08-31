from wikitextparser import WikiText


def parse_wiki(wiki: WikiText):
    for section in wiki.sections:
        print(f'{section.level} -> {section.title}')
    return None
