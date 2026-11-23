def analyze(Packagedict: dict, ErrorList: list) -> dict:
    report = {}

    for pkg_name, meta in Packagedict.items():
        requres_python = meta.get("requires_python")
        status = "WARNING" if requres_python == None else "OK" 
        flags = [] 
        if not requres_python:
            flags.append("Missing requires_python")

        report[pkg_name] = {
            "Version": meta.get("version"),
            "Requires_python": meta.get("requires_python"),
            "Status": status,
            "Flags": flags
        }

    for idx, errors in enumerate(ErrorList):
        report[errors] = {
            "Status": "MISSING/INVALID",
            "Index": idx,
            "Version": None,
            "Requires_python": None,
            "flags": ["not_found_or_invalid_package"]
        }

    print(report)

    return report
