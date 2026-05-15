med = float(input('Informe uma distância em metros: '))
km = med / 1000
hec = med / 100
dam = med / 10 
dm = med * 10
cm = med* 100
mm = med* 1000
print("A medida de {:.0f} corresponde a: \n {:.0f}km\n {:.0f}hec\n {:.0f}dam\n {:.0f}dm\n {:.0f}cm\n {:.0f}mm\n ".format(med,km, hec, dam, dm, cm, mm))