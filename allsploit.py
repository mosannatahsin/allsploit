#!/usr/bin/env python3
import os
import subprocess
import requests
from rich import print
from rich.panel import Panel
from rich.console import Console
from rich.prompt import Prompt

console = Console()

def banner():
    console.print(Panel.fit(
        "[bold green]ALLSPLOIT[/bold green]
"
        "[bold white]Ultimate Exploit Finder[/bold white]",
        border_style="bright_magenta",
        padding=(1, 4)
    ))

def search_searchsploit(query):
    try:
        output = subprocess.check_output(["searchsploit", query], stderr=subprocess.STDOUT)
        return output.decode()
    except subprocess.CalledProcessError as e:
        return f"[red]Searchsploit error:[/red] {e.output.decode()}"

def search_exploitdb(query):
    try:
        url = f"https://www.exploit-db.com/search?q={query}"
        return f"[cyan]Exploit-DB URL:[/cyan] {url}"
    except Exception as e:
        return f"[red]Exploit-DB search error:[/red] {str(e)}"

def search_github(query):
    try:
        url = f"https://github.com/search?q={query}+exploit"
        return f"[cyan]GitHub URL:[/cyan] {url}"
    except Exception as e:
        return f"[red]GitHub search error:[/red] {str(e)}"

def main():
    os.system("clear")
    banner()
    console.print("[yellow]Author:[/yellow] Mosanna Tahsin (https://github.com/mosannatahsin) & ChatGPT by OpenAI
")

    while True:
        query = Prompt.ask("[green]Enter exploit name (or 'exit' to quit)[/green]")
        if query.lower() == "exit":
            console.print("[bold red]Exiting allsploit. Stay safe![/bold red]")
            break

        console.print(f"
[bold magenta]Searching for:[/bold magenta] {query}")
        print("
[bold blue]Searchsploit Results:[/bold blue]")
        print(search_searchsploit(query))
        print("
[bold blue]Exploit-DB Link:[/bold blue]")
        print(search_exploitdb(query))
        print("
[bold blue]GitHub Link:[/bold blue]")
        print(search_github(query))

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"[red]Unexpected error occurred:[/red] {e}")
        print("[yellow]Please contact the developer at https://github.com/mosannatahsin[/yellow]")
