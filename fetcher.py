import requests
import parser

pkg_list = parser.parse()
pkg_dict = {}
data_list = []

def fetch(pkg):

    for Package in pkg:
            try:
                r = requests.get(f"https://pypi.org/pypi/{Package}/json", timeout=10)
                r.raise_for_status()
                data = r.json()

                pkg_dict.update({
                     
                    data["info"]["name"]: {
                        data["info"]["version"],
                        data["info"]["requires_python"]
                    },
                })

                

            except requests.exceptions.HTTPError as e:
                print(f"Package not found In Pypi. PKG: --> {Package}")

    data_list.append(pkg_dict)

if __name__ == "__main__":
    fetch(pkg_list)
    print(data_list)