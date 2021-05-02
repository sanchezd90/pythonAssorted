import PyPDF2

nombres=['ELORTEGUI, Julieta', 'AVELLA GRILLIA, Maria Susana', 'BARRETO, Soledad', 'BUSTOS, Ricardo', 'CALAFIORE, Alejandro', 'CALB, Diego', 'CAVALIERI, Hernan', 'CAVALIERI, Hernan', 'CORNET, Alejandra', 'COUTO, Silvina', 'D ANGELI, Victoria', 'DEFIORE, Daniela', 'FERRARI, Maria', 'FERRERO, Carolina', 'GAGLIARDI, Ma. Gabriela', 'GALLO, Laura', 'GARCIA BRAVO, Monica', 'GENTILE, Gustavo ', 'GIALLONGO, Gabriela', 'GONZALES, Mariel', 'GONZaLEZ, Ana Karina', 'JAIMEZ, Marcela', 'LALAYAN, Anabella', 'LAVAISSE, Lucia', 'LECUNA, Betiana', 'Llamasares, Sandra', 'MACHADO, Nadia', 'MAGGIOTTI, Gabriela', 'MANGIACONE, Nora', 'MARTINEZ, Graciela Cristina', 'MELO ANALIA MABEL', 'MIRANDA, Marcela', 'PEREZ AnAnOS, Mercedes', 'ROJAS Josefina', 'ROSSI, Clarisa', 'RUIZ DIAZ,  Ricardo', 'SALOMON, Carolina', 'SAMACOITS, Mariana', 'SaNCHEZ, Manuel', 'SICA, Fernando', 'SINFREU, Matias', 'SODERINI, Ana', 'SOMOZA, Javier', 'SZTRUM, Abelardo', 'TILBE, Claudia', 'TRIEMSTRA, Belen']

origin=open("certificado docentes.pdf","rb")
reader=PyPDF2.PdfFileReader(origin)

for x in range(len(nombres)):
    pageObj=reader.getPage(x)
    writer=PyPDF2.PdfFileWriter()
    writer.addPage(pageObj)
    nombre=nombres[x]+".pdf"
    output=open(nombre,"wb")
    writer.write(output)
    output.close()

origin.close()