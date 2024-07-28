import typer
from alembic import command
from alembic.config import Config
from pathlib import Path
import projects.migrator as lib

ALEMBIC_DIR = Path(lib.__file__).parent
ALEMBIC_CFG = Config(ALEMBIC_DIR / "alembic.ini")
app = typer.Typer()

def upgrade(revision="head"):
    command.upgrade(ALEMBIC_CFG, revision)


def downgrade(revision):
    command.downgrade(ALEMBIC_CFG, revision)

@app.command()
def current(verbose=False):
    command.current(ALEMBIC_CFG, verbose=verbose)


@app.command()
def goodbye(name: str, formal: bool = False):
    if formal:
        print(f"Goodbye Ms. {name}. Have a good day.")
    else:
        print(f"Bye {name}!")


if __name__ == "__main__":
    app()