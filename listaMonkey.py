from rich.console import Console
from rich.table import Table
listaProducto = []
listaCheck = []

table = Table(title="Lista de compras")
table.add_column("Nro de producto",style="green",no_wrap=True)
table.add_column("Producto",style="yellow")
table.add_column("Status", justify="center", style="green")

def pedido(listaProducto, listaCheck):
   cont = 0
   pedido = int(input("Ingrese la cantidad de productos a comprar: "))
   while(pedido != cont):
       producto = input("Ingrese el nombre del producto: ")
       listaProducto.append(producto)
       check = input("Indique si existe o no el producto: ")
       listaCheck.append(check)
       check = "✅" if check == "si" else "❌"
       for i in range(cont):
           table.add_row(str(cont), listaProducto[i], listaCheck[i])
       cont+= 1

def editar(listaProducto, listaCheck):
    editarPedido = input("¿Quiere editar el pedido? ")
    if(editarPedido == "si"):
        pregunta = input("¿Qué producto desea editar? ")
        for i, producto in enumerate(listaProducto):
            if(producto == pregunta):
                del listaProducto[i]
                del listaCheck[i]
                print(f"Producto '{producto}' eliminado del pedido.")
            else:
                print(f"El producto '{pregunta}' no se encuentre en el pedido")

pedido(listaProducto, listaCheck)
editar(listaProducto, listaCheck)
console = Console()
console.print(table)
