from bs4 import BeautifulSoup
from urllib.request import urlopen
import re

URL = "http://socrates.vsau.org/wiki/index.php/%D0%A1%D0%BF%D0%B8%D1%81%D0%BE%D0%BA_%D0%B0%D0%B4%D1%80%D0%B5%D1%81_%D0%B5%D0%BB%D0%B5%D0%BA%D1%82%D1%80%D0%BE%D0%BD%D0%BD%D0%B8%D1%85_%D0%BF%D0%BE%D1%88%D1%82%D0%BE%D0%B2%D0%B8%D1%85_%D1%81%D0%BA%D1%80%D0%B8%D0%BD%D1%8C_%D1%81%D1%82%D1%80%D1%83%D0%BA%D1%82%D1%83%D1%80%D0%BD%D0%B8%D1%85_%D0%BF%D1%96%D0%B4%D1%80%D0%BE%D0%B7%D0%B4%D1%96%D0%BB%D1%96%D0%B2_%D1%83%D0%BD%D1%96%D0%B2%D0%B5%D1%80%D1%81%D0%B8%D1%82%D0%B5%D1%82%D1%83"

name_email_regex = r'(?<=\n)(.+)(\n)?(?=</b>)'


def find_email(url, regex):
    page = urlopen(url)
    soup = BeautifulSoup(page, 'html.parser')
    names_emails = re.findall(regex, str(soup))
    result_list = []
    clean_result_list = []
    for el in range(len(names_emails)):  # Convert from tuple to list for cleaning
        # Only strings with names ending in tag </b> are included in the tuple. Last 8 emails without names.
        # TODO fix it!
        name_email = names_emails[el][0]
        result_list.append(name_email)

    for el in range(len(result_list)):  # Cleaning of strings
        line = result_list[el].split("<b>")
        line_clear = []
        for elem in range(len(line)):
            el_clear = str(line[elem]).replace("<p>", "").replace("</p>", "").replace("\t", "").replace("<br/>", "").replace("  ", " ").replace("  ", " ").replace("  ", " ")
            line_clear.append(el_clear)
        res_tuple = tuple(line_clear)
        clean_result_list.append(res_tuple)
    return clean_result_list


def save_to_file(file_name, data):
    file = open(file_name, "w")
    file.write(str(data))
    file.close()


if __name__ == '__main__':
    result = find_email(URL, name_email_regex)
    save_to_file('emails.txt', result)
