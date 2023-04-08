from database import fetch_transactions
import pandas as pd
from rich.panel import Panel
from rich.text import Text
from rich.console import Console

def print_ledger(conn):
    transactions = fetch_transactions(conn)
    if not transactions:
        print("No transactions found in the general ledger.")
        return

    header = ("ID", "Month", "Account", "Matching Account", "Name", "Reference", "Debit", "Credit")
    row_format = "{:<5} {:<10} {:<20} {:<20} {:<15} {:<25} {:<8} {:<8}"
    print(row_format.format(*header))

    for transaction in transactions:
        print(row_format.format(*transaction))

def print_dataframe(df, title):
    table = Table(title=title, show_header=False, show_lines=True)
    table.add_column("Category")
    table.add_column("Subcategory")

    for col in df.columns:
        table.add_column(str(col))

    for index, row in df.iterrows():
        table.add_row(str(index[0]), str(index[1]), *[str(value) for value in row])

    print(table)


def print_header(console: Console):
    header = Text("Kronys - Financial Statement Generator", style="bold blue")
    console.print(Panel(header, expand=False, border_style="blue"))


def print_status_message(console: Console, message, msg_type="info"):
    if msg_type == "complete":
        console.print(f"[green]✔[/green] {message}")
    elif msg_type == "processing":
        console.print(f"[yellow]⏳[/yellow] {message}")
    elif msg_type == "error":
        console.print(f"[red]❌[/red] {message}")
    else:
        console.print(f"[blue]ℹ[/blue] {message}")