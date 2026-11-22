import requests
import parser

pkg_list = parser.parse()

def fetch(pkg):

    r = requests.get(f"https://pypi.org/pypi/{pkg}/json", timeout=10)
    r.raise_for_status()
    data = r.json()


    print(data["info"]["name"], data["info"]["version"], f"Python: {data["info"]["requires_python"]}")

if __name__ == "__main__":
    for Package in pkg_list:
        try:
            fetch(Package)
        except requests.exceptions.HTTPError as e:
            print(f"Package not found In Pypi. PKG: --> {Package}")