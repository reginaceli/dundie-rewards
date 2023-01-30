import argparse

from dundie.core import load


def main():
    """Entry point to application"""

    parser = argparse.ArgumentParser(
        description="Dunder Mifflin system rewards CLI",
        epilog="Enjoy and use with cautious.",
    )

    parser.add_argument(
        "subcommand",
        help="Subcommando to run",
        type=str,
        choices=("load", "show", "send"),
        default="help",
    )

    parser.add_argument(
        "filepath",
        help="File path to load",
        type=str,
        default=None,
    )

    args = parser.parse_args()

    # print(*globals()[args.subcommand](args.filepath))

    if args.subcommand == "load":
        result = load(args.filepath)
        header = ["name", "dept", "role", "email"]

        for person in result:
            print("-" * 50)

            for key, value in zip(header, person.split(",")):
                print(f"{key}-> {value.strip()}")
