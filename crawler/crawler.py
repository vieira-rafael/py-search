import requests
import json
import time

def query_params():
    language = "language:python"
    size = "size:<100"
    stars = "stars:>=1"
    pushed = "pushed:2015-01-01..2015-12-31"
    return " ".join([language, size, stars, pushed])

def timeout():
    return 60

def make_request(count, next_page=None):
    url = next_page or "https://api.github.com/search/repositories"
    payload = {"q": query_params(), "page": next_page}
    # In case we want to know where a match occurs, if it were a term search.
    # headers = {"Accept": "application/vnd.github.v3.text-match+json"}

    res = requests.get(url, params=payload)

    filename = "data/repos/page{}".format(count)
    with open(filename, "w") as f:
        json.dump(res.json(), f)

    next_page = res.links["next"]["url"]
    if next_page != res.links["last"]["url"]:
        return next_page
    return None

def main():
    count = 1
    next_page = make_request(count)
    while next_page is not None:
        next_page = make_request(count, next_page)
        count += 1
        if count % 10 == 0:
            time.sleep(60)

if __name__ == "__main__":
    main()
