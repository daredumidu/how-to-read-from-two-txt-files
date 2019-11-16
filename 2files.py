

f = open ("excel.txt", "r")
f1 = f.readlines()

g = open ("gsheet.txt", "r")
g1 = g.readlines()

#for excel_file in f1:
for excel_file, gsheet in zip(f1, g1):
    #excel_file, gsheet = excel_file, gsheet.rstrip()
    excel_file = excel_file.rstrip()
    gsheet = gsheet.rstrip()

    print (excel_file, gsheet)

    #print (excel_file)
    #print (gsheet)
