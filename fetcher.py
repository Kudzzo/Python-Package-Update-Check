import requests
import parser

error_list = []
pkg_dict = {}

def fetch(Packagelist: list):

    for Package in Packagelist:
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
