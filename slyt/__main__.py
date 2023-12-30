import click
from slyt.lexer import lexer


@click.command()
@click.option('--file', help="file to execute", required=True)
def main(file: str):
    """It's a utility to execute SLYT scripts"""
    with open(file) as f:
        for line in lexer(f.readlines()):
            click.echo(line)

if __name__ == "__main__":
    main()
