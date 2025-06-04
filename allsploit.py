#!/usr/bin/env python3

from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.prompt import Prompt
from rich import print
import requests

console = Console()

def banner():
    banner_text = """
 █████╗  ██╗      ██╗     ███████╗███████╗██████╗  ██╗      ██╗████████╗
██╔══██╗ ██║      ██║     ██╔════╝██╔════╝██╔══██╗ ██║      ██║╚══██╔══╝
███████║ ██║      ██║     █████╗  █████╗  ██████╔╝ ██║      ██║   ██║   
██╔══██║ ██║      ██║     ██╔══╝  ██╔══╝  ██╔═══╝  ██║      ██║   ██║   
██║  ██║ ███████╗ ███████╗███████╗███████╗██║      ███████╗ ██║   ██║   
╚═╝  ╚═╝ ╚══════╝ ╚══════╝╚══════╝╚══════╝╚═╝      ╚══════╝ ╚═╝   ╚═╝   
    """
    # Using Rich's markup for colors and effects
    from rich.markup import escape

    # Split lines and color them alternately for cool effect
    lines = banner_text.strip('\n').split('\n')
    styled_lines = []
    colors = ["bold red", "bold yellow", "bold green", "bold cyan", "bold magenta"]

    for i, line in enumerate(lines):
        color = colors[i % len(colors)]
        styled_lines.append(f"[{color}]{escape(line)}[/{color}]")

    # Join back with newlines
    styled_banner = "\n".join(styled_lines)

    console.print(Panel(styled_banner, title="[bold bright_white]ALLSPLOIT[/bold bright_white]", subtitle="by [bold yellow]Mosanna Tahsin & ChatGPT[/bold yellow]", border_style="bright_magenta", padding=(1,2)), justify="center")
    
def menu():
    table = Table(show_header=True, header_style="bold blue")
    table.add_column("Option", justify="center")
    table.add_column("Action", justify="left")
    table.add_row("1", "Search for Exploits")
    table.add_row("2", "Help")
    table.add_row("3", "Exit")
    console.print(table)

def search_exploits(term):
    console.print(f"[bold cyan]Searching exploits for:[/bold cyan] [yellow]{term}[/yellow]\n")
    sources = [
        {"name": "ExploitDB", "url": f"https://www.exploit-db.com/search?query={term}"},
        {"name": "GitHub", "url": f"https://github.com/search?q={term}+exploit"},
        {"name": "Metasploit Docs", "url": f"https://docs.rapid7.com/metasploit/search/?q={term}"},
    ]

    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("Source")
    table.add_column("URL")

    for src in sources:
        try:
            response = requests.head(src["url"], timeout=5)
            if response.status_code < 400:
                table.add_row(src["name"], src["url"])
            else:
                table.add_row(src["name"], "[red]Connection failed[/red]")
        except Exception as e:
            table.add_row(src["name"], f"[red]Error: {str(e)}[/red]")

    console.print(table)

def help_menu():
    console.print(Panel.fit(
        """[bold cyan]Help - ALLSPLOIT[/bold cyan]

1. Enter a keyword or vulnerability name when prompted.
2. ALLSPLOIT will search multiple online sources for related exploits.
3. If any source fails, error message will be displayed.
4. Type 3 or 'exit' to quit the tool.

[green]Example:[/green] apache struts, windows smb, ftp overflow""",
        title="Help",
        border_style="green"
    ))

def main():
    banner()
    while True:
        menu()
        choice = Prompt.ask("\n[bold yellow]Enter your choice[/bold yellow]", choices=["1", "2", "3", "exit"])
        
        if choice == "1":
            keyword = Prompt.ask("[bold green]Enter exploit search term[/bold green]")
            if keyword.strip() != "":
                search_exploits(keyword.strip())
            else:
                console.print("[red]Search term cannot be empty![/red]")
        elif choice == "2":
            help_menu()
        elif choice in ["3", "exit"]:
            console.print("\n[bold magenta]Thanks for using ALLSPLOIT![/bold magenta]")
            break

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        console.print(f"[bold red]An unexpected error occurred:[/bold red] {e}")
        console.print("[yellow]Please contact the author: https://github.com/mosannatahsin[/yellow]")
