# -*- coding: utf-8 -*-

from __future__ import print_function
import glob
import os

from lxml import etree


def yield_xml_files(cldr_root, path_components):
    glob_pat = os.path.join(*[cldr_root] + list(path_components) + ["*.xml"])
    xml_files = glob.glob(glob_pat)
    for xml_file in xml_files:
        lang_id = os.path.splitext(os.path.basename(xml_file))[0]
        yield (lang_id, etree.parse(xml_file))
