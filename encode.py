from des import DesKey
from base64 import b64encode
from Crypto.Cipher import DES3
from Crypto.Util.Padding import pad

data = b'mensajes'
iv =b"12345678"

key = DesKey(b"llavedesllavedesllavedes")
key.is_triple();
cifrado = key.encrypt(b'mensajes', initial=iv, padding=True)

iv = b64encode(iv).decode('utf-8')
cifrado = b64encode(cifrado).decode('utf-8')
print(cifrado)

html ="""
<p>Este sitio contiene un mensaje secreto</p>
<div class='tripleDES' id='"""+cifrado+"""'></div>
"""

archivo = open("encode.html","w")
archivo.write(html)
archivo.close()