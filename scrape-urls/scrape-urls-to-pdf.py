import pdfkit
import os
import sys
import httplib2
import re
http = httplib2.Http()

GET_HTML = True

# For each section, get all readme files. Ignore "README.md".
paths = []
algos_dir = os.path.join(sys.path[0], "..", "algorithms")
for root, dirs, files in os.walk(algos_dir):
    section, chapter = root.split("/")[-2:]
    for name in files:
        if name.endswith(".md") and name not in ("README.md", "progress.md", "p-np-np-complete.md", ".DS_Store"):
            name = name[:-3]
            if section == "algorithms":
                paths.append((chapter, name))
            elif chapter == "algorithms":
                paths.append((name,))
            else:
                paths.append((section, chapter, name))

# paths = paths[:30]
# list(map(print, paths))
# for path in paths:
#     print(path)

base_url = "https://tech-prep-jeremy.gitbook.io/notes/algorithms/"

urls_filenames = [
    (
        base_url + "/".join(path),
        os.path.join(sys.path[0],
                     "htmls",
                     "-".join(path) + ".html"
                     ),
        path
    )
    for path in paths
]
# list(map(print, urls_filenames))
# Get all html files that we don't have, or force reset. Remember to clear the htmls folder if you want to reset.

# TODO: Clear htmls directory.

files = []
l = len(urls_filenames)
i = 1
print(f"Checking {l} urls (GET_HTML is {GET_HTML})...")
for url, filename, path in urls_filenames:
    if os.path.exists(filename):
        print(f"We already have {filename}")
    if not os.path.exists(filename) or GET_HTML:
        try:
            headers, body = http.request(url)
            # print(headers)
            print(f"Obtained {i}/{l} html file from url:{url}...")
            content = body.decode('utf-8')
            content = content.replace(
                path[-1].capitalize(),
                ('<u>' + path[-2] + '</u>: ' if len(path) > 1
                 else '') + path[-1].capitalize())
            # print("/".join(map(lambda s: s.capitalize(), path)))
            # print(content[:200])
            with open(filename, "w") as f:
                f.write(content)
            print(f"Wrote {i}/{l} html file to:{filename}...\n")
            i += 1
        except Exception as e:
            print(f"ERROR: Could not get url {url}")
            print(e)
    if os.path.exists(filename):
        files.append(filename)

files.sort()
# list(map(print, files))
# TODO: Add header.
CHUNK_SIZE = 10
file_chunks = [
    files[i:i+CHUNK_SIZE] if i + CHUNK_SIZE <= len(files) else files[i:]
    for i in range(0, len(files), CHUNK_SIZE)
]
for i, chunk in enumerate(file_chunks):
    res = pdfkit.from_file(
        chunk,
        os.path.join(sys.path[0], "pdfs", f"chunk-{i}-size-{CHUNK_SIZE}.pdf"),
        options={
            'print-media-type': '',
            'javascript-delay': 10000,
            'no-stop-slow-scripts': '',
            'disable-smart-shrinking': '',
            'encoding': 'utf-8',
            'header-left': 'Author: Jeremy Yew, 10/04/19.'
            # 'zoom': 1,
        }
    )
    if res:
        print(f"Generated chunk-{i} pdf.\n")
