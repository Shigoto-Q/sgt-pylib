"""Console script for shigoto_library."""

import click


@click.command()
def main():
    """Main entrypoint."""
    click.echo("shigoto-library")
    click.echo("=" * len("shigoto-library"))
    click.echo("Skeleton project created by Cookiecutter PyPackage")


if __name__ == "__main__":
    main()  # pragma: no cover
