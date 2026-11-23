import json
from pathlib import Path

def GenerateReport(ReportDict: dict, ErrorList: list ,outDir: str = " "):
    targetDir = Path(outDir)
    targetDir.mkdir(parents=True, exist_ok=True)

    warnings = [name for name, info in ReportDict.items() if info.get("Status") == "WARNING"]
    print(f"\nAudited: {len(ReportDict)} packages | Warnings: {len(warnings)} | Missing/Invalid: {len(ErrorList)}")
    if ErrorList:
        print("Missing/Invalid Packages: ", ",".join(ErrorList))

    json_path = targetDir / "report.json"
    with json_path.open("w", encoding="utf-8") as f:
        json.dump({"packages": ReportDict, "errors": ErrorList}, f, indent=2)   

    lines = [
        "# PyPI Health Audit Report",
        "",
        f"- **Packages audited:** {len(ReportDict)}",
        f"- **Warnings:** {len(warnings)}",
        f"- **Missing / Errors:** {len(ErrorList)}",
        "",
        "## Packages",
        "| Package | Version | requires_python | Status |",
        "| --- | --- | --- | --- |",
    ]

    for pkg_name, info in ReportDict.items():
        lines.append(
            f"| {pkg_name} | {info.get('Version', 'N/A')} | {info.get('Requires_python', 'N/A')} | {info.get('Status', 'N/A')} |"
        )

    if ErrorList:
        lines.extend(["", "## Missing / Errors"])
        lines.extend(f"- {err}" for err in ErrorList)

    (targetDir / "report.md").write_text("\n".join(lines) + "\n", encoding="utf-8")

