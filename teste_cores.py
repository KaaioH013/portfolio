# Importamos as funções que queremos da biblioteca rich
from rich import print
from rich.traceback import install

# Esta linha é a mais importante: ela "instala" o formatador de erros do Rich.
# A partir de agora, qualquer erro no seu programa será bonito e colorido.
install()

print("[bold green]O Rich consegue imprimir textos coloridos e formatados![/bold green]")
print("[yellow]Avisos podem ficar assim, por exemplo.[/yellow]")
print("[bold red]E erros poderiam ter este destaque.[/bold red]")

# Agora, a mágica de verdade: vamos forçar um erro de propósito.
print("\n[cyan]Agora vamos forçar um erro para ver o traceback do Rich...[/cyan]")

# Esta linha vai causar um erro de divisão por zero
1 / 0