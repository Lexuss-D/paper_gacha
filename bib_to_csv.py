from turtle import position
from urllib.error import URLError
import pandas as pd
from bs4 import BeautifulSoup
import requests
import re
from multiprocessing import Pool
from tqdm import tqdm
from pylatexenc.latex2text import LatexNodes2Text
from pybtex.database import parse_file


def get_citations_result(keyword, number):
    """Get citation number of the paper from Google Scholar

    Args:
        param1(str): Title of the paper
        param2(int): Number of returned results from google scholar
    Returns:
        citations(int): How many times the paper is cited 
    """

    html_doc = requests.get(
        "https://scholar.google.co.jp/scholar?hl=ja&as_sdt=0%2C5&num="
        + str(number)
        + "&q="
        + keyword
    ).text
    soup = BeautifulSoup(html_doc, "html.parser")

    tags = soup.find_all(text=re.compile("引用元"))  # citation

    citations = 0
    for tag in tags:
        citations = int(tag.replace("引用元", ""))

    return citations


def set_rarity_by_citations(citation):
    """Set the rarity of the paper by citations

    Args:
        param1(int): Citations of the paper
    Returns:
        Rarity(str): UR!
    """

    label = ["R", "SR", "SSR", "UR"]
    if citation >= 10000:
        return "UR"
    elif citation < 10000 & citation >= 5000:
        return "SSR"
    elif citation < 5000 & citation >= 1000:
        return "SR"
    else:
        return "R"


def get_data_from_bib(entries):
    """Get paper information from entries in bibdata

    Args:
        param1: bibdata.entries

    Returns:
        List: A list contains info of each paper
    """
    bibarray = []
    for bib_id in tqdm(entries):

        bf = entries[bib_id].fields
        bp = entries[bib_id].persons

        author_list = []

        if bp.get("editor"):
            for person in bp["editor"]:
                first = " ".join(person.first_names)
                middle = " ".join(person.middle_names)
                last = " ".join(person.last_names)
                author_list.append(" ".join([first, middle, last]))
        elif bp.get("author"):
            for person in bp["author"]:
                first = " ".join(person.first_names)
                middle = " ".join(person.middle_names)
                last = " ".join(person.last_names)
                author_list.append(" ".join([first, middle, last]))

        dauthor = ",".join(author_list)

        if bf["year"] is None:
            dyear = "NA"
        else:
            dyear = bf["year"]

        if bf.get("url"):
            durl = bf["url"]
        else:
            durl = "NA"

        if bf.get("booktitle"):
            text = LatexNodes2Text().latex_to_text(bf["booktitle"])
            dbooktitle = text.replace("{", "").replace("}", "")
        else:
            dbooktitle = "NA"

        dtitle = (
            LatexNodes2Text()
            .latex_to_text(bf["title"])
            .replace("{", "")
            .replace("}", "")
        )

        dcitations = get_citations_result(dtitle, 1)

        drate = set_rarity_by_citations(dcitations)

        d = {
            "bib_id": bib_id,  # some formula for obtaining values
            "Title": dtitle,
            "author": LatexNodes2Text().latex_to_text(dauthor),
            "Year": dyear,
            "url": durl,
            "Book Title": dbooktitle,
            "citations": dcitations,
            "rate": drate,
        }
        bibarray.append(d)
  
    return bibarray


if __name__ == "__main__":

    raw_file_path = "./anthology.bib"

    bibdata = parse_file(raw_file_path)
    bibkeys = bibdata.entries.keys()
    #print(len(bibdata.entries))

    # multiprocessing

    bibarray = get_data_from_bib(bibdata.entries)

    bibdataset = pd.DataFrame(bibarray)

    bibdataset.to_csv("./formatted_df_data.csv", sep=",", index=False, header=False)
