import click
from data_preparation.data_preparation import process_pairs_of_docs

@click.command()
@click.option('--doc_url', help='URL of the spreadsheet', required=True)
def process_docs_command(doc_url):
    process_pairs_of_docs(doc_url)
    click.echo('Docemnts pairs processed successfully.')

if __name__ == "__main__":
    process_docs_command("https://docs.google.com/spreadsheets/d/1ZsTxRosThq-1vGT8tRaLm0m-E826f_7BlQJ08QaK9kI/edit#gid=0")