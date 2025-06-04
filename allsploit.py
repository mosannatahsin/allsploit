#!/usr/bin/env python3
import os
import sys
import requests
from rich import print
from rich.panel import Panel
from rich.prompt import Prompt
from rich.console import Console
from rich.table import Table

console = Console()

AUTHOR = "Mosanna Tahsin & ChatGPT"
TOOL_NAME = "ALLSPLOIT"

BANNER = f"""[bold green]
      █████╗ ██╗     ██╗     ███████╗███████╗██████╗ ██╗     ██╗████████╗
     ██╔══██╗██║     ██║     ██╔════╝██╔════╝██╔══██╗██║     ██║╚══██╔══╝
     ███████║██║     ██║     █████╗  █████╗  ██████╔╝██║     ██║   ██║   
     ██╔══██║██║     ██║     ██╔══╝  ██╔══╝  ██╔═══╝ ██║     ██║   ██║   
     ██║  ██║███████╗███████╗███████╗███████╗██║     ███████╗██║   ██║   
     ╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝╚══════╝╚═╝     ╚══════╝╚═╝   ╚═╝   [/bold green]

[b cyan]Author:[/b cyan] [white]{AUTHOR}[/white]
[b cyan]Tool:[/b cyan] [white]{TOOL_NAME}[/white]
"""


def search_exploits(term):
    results = []

    try:
        console.print("[yellow]Searching in ExploitDB (online)...[/yellow]")
        exploitdb_url = f"https://www.exploit-db.com/search?order_by=date_published&description={term}"
        results.append(("ExploitDB", exploitdb_url))
    except Exception as e:
        console.print(f"[red]ExploitDB search failed:[/red] {e}")

    try:
        console.print("[yellow]Searching in GitHub...[/yellow]")
        github_url = f"https://github.com/search?q={term}+exploit"
        results.append(("GitHub", github_url))
    except Exception as e:
        console.print(f"[red]GitHub search failed:[/red] {e}")

    try:
        console.print("[yellow]Searching in Metasploit modules (local)...[/yellow]")
        metasploit_cmd = f"msfconsole -q -x 'search {term}; exit'"
        os.system(metasploit_cmd)
    except Exception as e:
        console.print(f"[red]Metasploit search failed:[/red] {e}")

    return results


def show_results(results):
    table = Table(title="Exploit Search Results", header_style="bold magenta")
    table.add_column("Platform", style="cyan")
    table.add_column("Link / Source")

    for name, link in results:
        table.add_row(name, link)

    console.print(table)


def main():
    os.system("clear")
    print(Panel.fit(BANNER, border_style="green"))

    while True:
        try:
            option = Prompt.ask("[bold green]Enter exploit name to search (or type 'exit')[/bold green]")
            if option.lower() == 'exit':
                console.print("[bold yellow]Exiting... Stay safe![/bold yellow]")
                break

            results = search_exploits(option)
            if results:
                show_results(results)
            else:
                console.print("[red]No results found. Please refine your search term.[/red]")

        except KeyboardInterrupt:
            console.print("
[bold yellow]Interrupted. Exiting...[/bold yellow]")
            break
        except Exception as err:
            console.print(f"[red]An unexpected error occurred: {err}[/red]")
            console.print("[bold cyan]Please contact the author: Mosanna Tahsin (https://github.com/mosannatahsin)[/bold cyan]")
            break


if __name__ == "__main__":
    main()
