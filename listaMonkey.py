from rich.console import Console
from rich.table import Table

table = Table(title="Lista de monos")

table.add_column("Nro",style="green",no_wrap=True)
table.add_column("Tipo de mono",style="yellow")
table.add_column("Status", justify="center", style="green")

table.add_row("1", "Alocado", "✅")
table.add_row("2", "Gracioso", "✅")
table.add_row("3", "Pendenciero", "❌")
console = Console()
console.print(table)
