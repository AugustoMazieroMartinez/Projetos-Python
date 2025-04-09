import Reader as rdr

reader = rdr.Reader("Projetos/file_reader/file.txt")
print(reader.read())
print(reader.count_words())
print(reader.count_repeating_letters())