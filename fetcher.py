import requests
import parser

error_list = []

def fetch():
    pkg_list = parser.parse()
    pkg_dict = {}

    for Package in pkg_list:
            try:
                r = requests.get(f"https://pypi.org/pypi/{Package}/json", timeout=10)
                r.raise_for_status()
                data = r.json()

                pkg_dict.update({
                     
                    data["info"]["name"]: {
                        "version": data["info"]["version"],
                        "requires_python": data["info"]["requires_python"]
                    },
                })

                

            except Exception as e:
                print(f"Error: {e}",f"PKG: --> {Package}")
                error_list.append(Package)
                

    return error_list, pkg_dict

if __name__ == "__main__":
    fetch()
    print(error_list)