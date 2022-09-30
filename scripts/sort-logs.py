import re
import sys
import os
from pathlib import Path
from operator import itemgetter


dateRegex = re.compile(r"\d{2}:\d{2}:\d{2},\d{3}-\[", re.I)

if len(sys.argv) != 2:
    sys.exit(1)

filename = sys.argv[1]

if not filename:
    sys.exit(1)

pFile = Path(filename)

lines = []

with open(pFile, encoding="utf-8") as f:
    for line in f:

        timeArr = re.findall(dateRegex, line)

        if len(timeArr) == 0:
            continue

        time = timeArr[0]

        time = time.split(",")[0]
        time = time.replace(":", "")

        lineDict = {"time": int(time), "line": line}

        lines.append(lineDict)

sortedLines = sorted(lines, key=itemgetter("time"))

with open(f"{os.path.basename(pFile)}-sorted.log", "w", encoding="utf-8") as f:
    for lineDict in sortedLines:
        f.write(lineDict["line"])
