from __future__ import print_function
import codecs
import json

from date_formats import get_date_formats

data = get_date_formats()
with codecs.open("output/available_date_formats.json", "w", "UTF-8") as outf:
    json.dump(data, outf, separators=",:", ensure_ascii=False)
