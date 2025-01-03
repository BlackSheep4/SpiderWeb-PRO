
#!/usr/bin/python3

def help_panel():

    print("\nUsage: ")
    print("\tpython main.py [command]\n")
    
    print("\nCommands:")
    
    # List of commands with descriptions
    commands = {
        "scan [URL]": "Start an information gathering recollection int he specified website\n                             Ejemplo: scan example.com",
        "update": "Actualiza el programa y sus dependencias a la última versión disponible.\n                             Ejemplo: update",
        "help": "Muestra este panel de ayuda con una lista de todos los comandos disponibles.\n                             Ejemplo: help",
        "info": "Muestra información sobre la versión, el autor y la última actualización del programa.\n                             Ejemplo: info",
        }
    
    # Display commands and descriptions
    for command, description in commands.items():
        print(f"  {command.ljust(25)} {description}")

    print("\nFor more details on each command, use: ")
    print("\tpython main.py help [command]")
    print("="*80 + "\n")