"""Define some command to import in top-level typer."""

from typing import Annotated

from typer import Argument, Option, Typer

cli: Typer = Typer()


@cli.command()
def works(
    args: Annotated[list[str], Argument()], opt: Annotated[str, Option("-o", "--opt")]
) -> None:
    print(f"{args = }")
    print(f"{opt = }")
