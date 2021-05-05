"""Main module for a general python application."""
import argparse


def main(args: argparse.Namespace) -> None:
    """Run some code.

    Params:
    -------
    `args`: An `argparse` namespace containing parsed command line arguments.

    Returns:
    --------
    None.
    """
    print(f"Hello, {args.name}!")


def parse() -> argparse.Namespace:
    """Parse `sys.argv` and return an `argparse.Namespace` object.

    Params:
    -------
    None.

    Returns:
    --------
    An `argparse.Namespace` object containing the values of each parsed argument.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--name", type=str, default="world", help="The name to say hello to."
    )
    return parser.parse_args()


if __name__ == "__main__":
    main(parse())
