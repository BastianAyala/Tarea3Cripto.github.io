from des import DesKey
from base64 import b64encode

data = b'mensajes'
iv =b"12345678"
key = DesKey(b"llavedesllavedesllavedes")
key.is_triple()

cifrado = key.encrypt(data, initial=iv, padding=True)

cifrado = b64encode(cifrado).decode('utf-8')
print(cifrado)

html ="""
<p>Este sitio contiene un mensaje secreto</p>
<div class='tripleDES' id='"""+cifrado+"""'></div>
"""

archivo = open("index.html","w")
archivo.write(html)
archivo.close()
