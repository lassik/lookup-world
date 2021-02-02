#! /usr/bin/env python3

import re

import util


URL = "https://en.wikipedia.org/wiki/ISO_4217?action=raw&section=8"
CACHE = "article.wiki"
COLUMNS = ["Code", "Number", "Currency", "Locations", "Digits"]


def cleanup_table_column(s):
    s = s.strip()
    s = re.sub(r"\[\[(.*?)(\|.*?)?\]\]", r"\1", s)
    s = re.sub(r"\[(.*?)\]", "", s)
    s = re.sub(r"\{\{.*?\}\}", "", s)
    s = re.sub(r"<.*?>", "", s)
    s = s.strip()
    return s


def scrape():
    region = None
    for line in open(util.get_cache_file(CACHE, URL)):
        if line.startswith("|"):
            fields = list(map(cleanup_table_column, line[1:].split("||")))
            if len(fields) == 5:
                yield fields


if __name__ == "__main__":
    util.write_csv(COLUMNS, scrape())
