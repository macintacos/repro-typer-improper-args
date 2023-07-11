"""Begin repro."""

import typer

from repro import actually, new

cli = typer.Typer(
    no_args_is_help=True,
    context_settings={"help_option_names": ["-h", "--help"]},
)

cli.add_typer(new.cli, name="new")
cli.add_typer(actually.cli, name="actually")
