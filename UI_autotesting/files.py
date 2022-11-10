# var = input("Напиши что нибудь:" )
# fw = open("doc/file.txt", "a")
# fw.write(var)
# fw.close()

# а - запись новых данных в файл и помещение новых данных в конец файла
# w - запись новых файлов но с удаление старых

# fw = open("doc/file_2.txt", "w")
# fw.write("privet!!!")
# fw.close()

fr = open("doc/file.txt", "r")
text = fr.read()
fr.close()

print(text)
