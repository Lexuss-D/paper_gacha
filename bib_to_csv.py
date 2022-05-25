import pandas as pd
from pylatexenc.latex2text import LatexNodes2Text
from pybtex.database import parse_file

raw_file_path = "/Users/lingzhidong/Documents/Github/paper_gacha/anthology.bib"

bibdata = parse_file(raw_file_path)
bibkeys = bibdata.entries.keys()
bibarray = []

for bib_id in bibdata.entries:

    bf = bibdata.entries[bib_id].fields
    bp = bibdata.entries[bib_id].persons

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
        text=LatexNodes2Text().latex_to_text(bf["booktitle"])
        dbooktitle = text.replace("{","").replace("}","")
    else:
        dbooktitle = "NA"

    dtitle=LatexNodes2Text().latex_to_text(bf["title"]).replace("{","").replace("}","")
    d = {
        "bib_id": bib_id,  # some formula for obtaining values
        "Title": dtitle,
        "author": LatexNodes2Text().latex_to_text(dauthor),
        "Year": dyear,
        "url": durl,
        "Book Title": dbooktitle,
        "rate": "R",
    }
    bibarray.append(d)

bibdataset = pd.DataFrame(bibarray)

bibdataset.to_csv("./formatted_df_data.csv", sep=",", index=False, header=False)
