import json
import os
from justadork import DorkScanner

if __name__ == "__main__":
    if not os.path.exists("output"):
        os.makedirs("output")
    config = json.loads(open("config.json", "r").read())
    scanner = DorkScanner(config)
    urls = []
    for dork in open("dorks.txt", "r").readlines():
        dork = dork.strip()
        if len(dork) < 2:
            continue
        lls = scanner.search_urls(dork)
        if lls is None:
            print("your ip got blocked!")
            break
        else:
            for url in lls:
                urls.append(url)
    scanner.save(urls)
