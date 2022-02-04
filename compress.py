import zipfile 

#file = ["Actividad3_Consultoria.docx"]
#file = ["words1.txt", "words2.txt", "words3.txt"]
file = ["descarga.jpg"]
archive = "foto.zip"
password =b"12345"

#comprimir los archivos 
with zipfile.ZipFile(archive, "w") as zf:
    for  file in file:
        zf.write(file)
        
    zf.setpassword(password)
    
with zipfile.ZipFile(archive, "r") as zf:
    crc_test = zf .testzip()
    if crc_test is not None:
        print ("Algo sucedió o header incorrectos: {crc_text}")
        
    info = zf.infolist()
    print (info)
    
    file = info [0]
    with zf.open(file) as f:
        print(f.read(). decode())