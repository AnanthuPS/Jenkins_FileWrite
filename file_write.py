#Writing name to a file

name = "Ananthu"
fd = open("name.txt","w")
fd.write(name)
fd.close()
