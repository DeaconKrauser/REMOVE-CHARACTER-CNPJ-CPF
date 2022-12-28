def removeCaracterCNPJ():
  a = input("Digite: ")
  b = ".-/*"
  for i in range(0,len(b)):
    a =a.replace(b[i],"")
  print(a)
  removeCaracterCNPJ()
removeCaracterCNPJ()