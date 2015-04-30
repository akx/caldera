import codecs
from collections import defaultdict
import glob
import json
from lxml import etree
import os



def yield_xml_files(cldr_root, path_components):
    xml_files = glob.glob(os.path.join(*[cldr_root] + list(path_components) + ["*.xml"]))
    for xml_file in xml_files:
        lang_id = os.path.splitext(os.path.basename(xml_file))[0]
        yield (lang_id, etree.parse(xml_file))


data = defaultdict(dict)

for lang_id, tree in yield_xml_files("cldr", ("common", "main")):
    for date_format in tree.xpath("/ldml/dates/calendars/*/dateTimeFormats/availableFormats/dateFormatItem"):
       data[lang_id][date_format.get("id")] = date_format.text

with codecs.open("output/available_date_formats.json", "w", "UTF-8") as outf:
    json.dump(data, outf, separators=",:", ensure_ascii=False)
