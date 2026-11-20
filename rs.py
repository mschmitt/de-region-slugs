#!/usr/bin/env python3
import sys
from slugify import slugify, GERMAN
import json
import re

trailing_blanks = re.compile(' +$')
junk = re.compile('(, *Stadt$|, Landeshauptstadt|, kreisfreie Stadt|-Kreis|, documenta-Stadt$|, Wissenschaftsstadt$|, Brüder-Grimm-Stadt|, Freie und Hansestadt$|, Hansestadt$|, Klingenstadt$|, Stadt der FernUniversität$| im Breisgau|, Stadtkreis$| Kreis$|kreis( |\b|$)|^Regionalverband |^Region )')

for line in sys.stdin:
    type = line[0:2]
    if type == "40":
        ars  = line[10:18]
        ars  = trailing_blanks.sub('', ars)
        name = line[22:72]
        name = trailing_blanks.sub('', name)
        name = junk.sub('', name)
        print(f"{ars}0000000 {name} {slugify(name, replacements=GERMAN)}")
