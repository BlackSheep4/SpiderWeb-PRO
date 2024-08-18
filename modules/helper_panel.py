
#!/usr/bin/python3

def help_panel():
    print("\n" + "="*80)
    print("AIO Tool For Information Gathering And Automatic Vulnerability Scanner")
    print("Version: 2.0")
    print("Author: BlackSheep4")
    print("Github: https://github.com/BlackSheep4")
    print("="*80 + "\n")
    print("Usage: ")
    print("  python main.py [command]\n")
    
    print("Commands:")
    
    # List of commands with descriptions
    commands = {
        "scan [URL]": "Realiza un escaneo de vulnerabilidades en la URL especificada.\n                             Ejemplo: scan example.com",
        "update": "Actualiza el programa y sus dependencias a la última versión disponible.\n                             Ejemplo: update",
        "fix": "Repara dependencias o configuraciones dañadas.\n                             Ejemplo: fix",
        "help": "Muestra este panel de ayuda con una lista de todos los comandos disponibles.\n                             Ejemplo: help",
        "exit": "Cierra el programa de forma segura.\n                             Ejemplo: exit",
        "info": "Muestra información sobre la versión, el autor y la última actualización del programa.\n                             Ejemplo: info",
        "modules": "Lista todos los módulos y funcionalidades disponibles en el programa.\n                             Ejemplo: modules",
        "reset": "Restablece la configuración predeterminada del programa.\n                             Ejemplo: reset",
        "status": "Muestra el estado actual del sistema y sus dependencias.\n                             Ejemplo: status",
        "logs": "Muestra los registros de acciones y escaneos recientes.\n                             Ejemplo: logs",
        "config": "Muestra o modifica la configuración del programa.\n                             Ejemplo: config",
        "proxy set [URL]": "Configura un proxy para ejecutar los escaneos a través de una conexión específica.\n                             Ejemplo: proxy set http://proxy:port",
        "check": "Verifica la configuración del sistema y la disponibilidad de las dependencias.\n                             Ejemplo: check",
        "clear": "Limpia la consola de salida para mejorar la legibilidad.\n                             Ejemplo: clear",
        "report [URL] --format [F]": "Genera un informe de los resultados del escaneo en el formato especificado (JSON, HTML, PDF).\n                             Ejemplo: report example.com --format pdf",
        "verbose": "Habilita el modo detallado, mostrando más información durante la ejecución.\n                             Ejemplo: verbose",
        "debug": "Habilita el modo de depuración para registrar en detalle cada paso del programa.\n                             Ejemplo: debug",
        "history": "Muestra los últimos comandos ejecutados.\n                             Ejemplo: history",
        "save-config [file]": "Guarda la configuración actual en un archivo para futuras sesiones.\n                             Ejemplo: save-config config.yaml",
        "load-config [file]": "Carga configuraciones desde un archivo previamente guardado.\n                             Ejemplo: load-config config.yaml",
    }
    
    # Display commands and descriptions
    for command, description in commands.items():
        print(f"  {command.ljust(25)} {description}")

    print("\nFor more details on each command, use: ")
    print("  python main.py help [command]")
    print("="*80 + "\n")