import hashlib
matkhau = "1223455"
a = hashlib.md5(matkhau.encode())# bat buoc phai encode truoc khi chuyen sang ma hash
print(a.digest())
print(a.hexdigest())
b = hashlib.sha256(matkhau.encode())
print(b.hexdigest())