import argparse
from pathlib import Path

import analyzer
import fetcher
import parser
import reporter

def main() -> None:
    arg_parser = argparse.ArgumentParser(description="Audit Python package health via PyPI.")
    arg_parser.add_argument(
        "requirements", 
        nargs="?",
        default="requirements.txt",
        help="Path to requirements file (default: requirements.txt)",
    )
    arg_parser.add_argument(
        "--out",
        default=".",
        help="Output directory for generated reports (default: .)",
    )
    args = arg_parser.parse_args()

    requirePath = Path(args.requirements)
    if not requirePath.is_file():
        print(f"Error: requirements.txt file not found: {requirePath}")
        raise SystemExit(1)

    pkg_list = parser.parse()
    pkg_dict, error_list = fetcher.fetch(pkg_list)
    analyzed = analyzer.analyze(pkg_dict, error_list)
    reporter.GenerateReport(analyzed, error_list, outDir=args.out)

if __name__ == "__main__":
    main()