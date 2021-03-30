# conversor de M para CM e MM .

metro = float(input('Digite uma medida em metros: '))
cm = metro*100
mm = metro*1000
print('{:.2f}m  >>  {:.2f}cm  >>  {:.2f}mm'.format(metro,cm,mm))