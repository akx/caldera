# -*- coding: utf-8 -*-

from __future__ import print_function
from collections import defaultdict
import sys

from utils import yield_xml_files

GREGORIAN_DATE_FORMAT_ITEMS_XPATH = \
    "/ldml/dates/calendars/calendar[@type='gregorian']/" \
    "dateTimeFormats/availableFormats/dateFormatItem"


def get_date_formats():
    data = defaultdict(dict)
    for lang_id, tree in yield_xml_files("cldr", ("common", "main")):
        for date_format in tree.xpath(GREGORIAN_DATE_FORMAT_ITEMS_XPATH):
            data[lang_id][date_format.get("id")] = date_format.text
        n = len(data[lang_id])
        print("%s: %d entries" % (lang_id, n), file=sys.stderr)
        if not n:
            data.pop(lang_id)

    print("%d locales parsed." % len(data), file=sys.stderr)
    return data
