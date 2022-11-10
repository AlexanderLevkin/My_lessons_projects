fw = open("dir/file_1.txt", "w")
fw.write("Hi there\n")
fw.close()

var_1 = input("Write something: ")
fa = open("dir/file_1.txt", "a")
fa.write(f"{var_1}\n")
fa.close()

fr_1 = open("dir/file_1.txt", "r+")
text = fr_1.read()
print(text)
text = fr_1.write("New line\n")
fr_1.close()

fr_2 = open("dir/file_1.txt", "r")
text_2 = fr_2.read()
print(text_2)





