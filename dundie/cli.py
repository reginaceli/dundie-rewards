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
        default="help"
    )

    parser.add_argument(
        "filepath",
        help="File path to load",
        type=str,
        default=None
    )

    args = parser.parse_args()

    try:
        globals()[args.subcommand](args.filepath)
    except KeyError:
        print("Subcommand is invalid")