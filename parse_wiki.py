import re

from wikitextparser import WikiText, Tag

gecko_re = re.compile(
    r"^ \$(?P<header>.*?)(?: *\((?P<version>(?:Melee|SSBM)? *(?:PAL|NTSC)? *(?:v?\d\.\d\d)?)?\))?"
    r"(?: *\[(?P<authors>.*?)\])?[ \t:]*$"
    r"(?P<description>(?:\n \*(?:.*?)$)*)"
    r"(?P<hex>(?:$\n [\dA-Fa-f]{8} [\dA-Fa-fxyXY]{8}[ \t]*(?:#.*)?$)+)",
    flags=re.MULTILINE)


def parse_wiki(wiki: WikiText):
    for section in wiki.sections:
        def div_filter(tag: Tag):
            if tag.name != 'div':
                return False

            return True

        for div in filter(div_filter, section.get_tags()):
            for gecko in gecko_re.finditer(str(div.parsed_contents)):
                print(gecko['header'])
    return None
