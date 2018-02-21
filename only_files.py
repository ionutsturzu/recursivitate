def doar_fisier(nume_fisier):
    for i in os.listdir(nume_fisier):
        if os.path.isdir(nume_fisier + "/"+i):
            doar_fisier(nume_fisier + "/" + i)
        else:
            print(nume_fisier,i)
doar_fisier(sys.argv[1])
