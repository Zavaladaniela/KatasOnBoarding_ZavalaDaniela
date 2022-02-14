def main():
    try:
        configuration = open('config.txt','r')
    except FileNotFoundError:
        print("Couldn't find the config.txt file!")
    except IsADirectoryError:
        print ('Se encontro pero se puede abrir porque es una carpeta')
    except PermissionError:
        print ('No tengo permisos para leer el archivo config.txt')


if __name__ == '__main__':
    main()