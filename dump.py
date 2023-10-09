#!/usr/bin/env python3
# SPDX-License-Identifier: MIT

import argparse
import json

from katwarn_api import dump_all


def main():
    parser = argparse.ArgumentParser(description="Dump all data from the API to JSON")
    parser.add_argument(
        "-o",
        "--output",
        metavar="PATH",
        type=str,
        default="dump.json",
        help="Output file",
    )
    args = parser.parse_args()

    with open(args.output, "w", encoding="utf-8") as f:
        json.dump(dump_all(), f, indent=2, ensure_ascii=False, sort_keys=True)


if __name__ == "__main__":
    main()
