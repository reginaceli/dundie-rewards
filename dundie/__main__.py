import argparse
import os


filepath = os.path.join(__file__)
print('=>', filepath)


def load(filepath):
    """Reads data from filepath to the database"""
    try:
        with open(filepath) as file_:
            for line in file_:
                print(line)
    except FileNotFoundError as e:
        print(f"File not found: {e}")


# def read_required_txt(paths):


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
        choices=("load", "show", "send")
    )

    parser.add_argument(
        "filepath",
        help="File path to load",
        type=str,
    )

    args = parser.parse_args()

    try:
        globals()[args.subcommand](args.filepath)
    except KeyError:
        print("Subcommand is invalid")


if __name__ == "__main__":
    main()
