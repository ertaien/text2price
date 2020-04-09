import re


def parser_amount(text):
    text = re.sub('[\s+]', '', re.sub(r'[^\w]', ' ', text.lower()))
    result = re.search("[0-9]+(тг|тенге|теңге|тнг|tg|млн|тыс|миллион|мың|мын)", text)

    if result:
        result_int = re.findall("[0-9]+", result.group())[0]

        if re.search("[0-9]+(млн|миллион)", text):
            result_int += "000000"
        elif re.search("[0-9]+(тыс|мың|мын)", text):
            result_int += "000"

        return int(result_int)

    return None
