# Repro of Typer Issue

[Install `Poetry`](https://python-poetry.org/docs/). Clone the repo and run `poetry install && poetry shell`. Then notice:

- `repro new -o okay lol` successfully runs:

    ```bash
    $ repro new -o okay lol
    args = ['lol']
    opt = 'okay'
    ```

- ...but `repro new okay -o lol` does not:

    ```bash
    $ repro new okay -o lol
    Usage: repro new [OPTIONS] ARGS... COMMAND [ARGS]...
    Try 'repro new -h' for help.
    ╭─ Error ───────────────────────────────────────────╮
    │ Missing option '-o' / '--opt'.                    │
    ╰───────────────────────────────────────────────────╯
    ```

- Notice that the other command, _not_ added as a callback, seems to work okay (the command parameters are identical):

    ```bash
    $ repro actually works lol -o okay
    args = ['lol']
    opt = 'okay'

    $ repro actually works -o okay lol
    args = ['lol']
    opt = 'okay'
    ```
