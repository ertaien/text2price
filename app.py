import re


def parser_amount(text):
    text = re.sub('[\s+]', '', re.sub(r'[^\w]', ' ', text.lower()))
    result = re.search("[0-9]+(тг|тенге|теңге|тнг|tg)", text)

    if result:
        return int(re.findall("[0-9]+", result.group())[0])

    return None