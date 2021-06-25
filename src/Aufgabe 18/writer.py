filePath= 'D:\\Pycharm\\SRC'

msg = "class Kreis"
with open(filePath, 'w') as writer:
    writer.write(msg)

with open(filePath, 'a') as a_writer:
    a_writer.write('\nmsg')