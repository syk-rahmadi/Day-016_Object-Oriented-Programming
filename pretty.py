from prettytable import PrettyTable
table = PrettyTable()
tables = PrettyTable()
tableso = PrettyTable()

pokemon = ["pikachu", "squirtle", "charmander"]
pokemon_type = ["electric", "water", "fire"]


#Add row by now (add_row)
table.field_names = ["Pokemon Name", "Type"]
table.add_row(["Pikachu","electric"])
table.add_row(["Squirtle", "water"])
table.add_row(["Charmander", "Fire"])
print(table)

#Add row all rows at once (add_rows)
tables.field_names = ["Pokemon Name", "Type"]
tables.add_rows(
    [
        ["Pikachu","electric"],
        ["Squirtle", "water"],
        ["Charmander", "Fire"]
    ]

)
print(tables)


#Add column by column
tableso.add_column("Pokemon Name", ["Eevee", "Squirtle", "Charmander"])
tableso.add_column("Pokemon Type",["Fire","Water", "Fire"])
print(tableso)

#We cannot assign a value to a function call