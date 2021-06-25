filePath_source= 'C:\\Users\\Skayd\\PycharmProjects\\Schule\\SRC\\Aufgabe 18'
filePath_destination = 'C:\\Users\\Skayd\\PycharmProjects\\Schule\\SRC\\Aufgabe 18'

with open(filePath_source, 'r') as source_reader, open(filePath_destination, 'w') as destination_writer:
   source_content = source_reader.readlines()
   destination_writer.writelines(reversed(source_content))