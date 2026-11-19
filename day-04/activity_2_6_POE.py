try:
    with open("names.txt","w") as f:
        f.write("Granny\n" )
        f.write("Tebogo\n" )
        f.write("Peter\n" )
        f.write( "John\n")
        f.write("Slave\n" )
    
    f = open("names.txt","r")
    text = f.read()
    f.close()
    print(text.strip().upper())
    with open("names.txt", "a") as f:
        f.write("Thandi\n")
    with open("names.txt") as f:
        lines = f.readlines()
    print(len(lines))

    with open("nothing.txt") as f:
        print(f.read())
except FileNotFoundError:
    print ("File not found.Check the name and the folder")
