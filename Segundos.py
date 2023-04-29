segundos=input("Por favor, entre com o número de segundos que deseja converter:")
total_seg=int(segundos)

a=total_seg//86400
seg_restantes=total_seg%86400
b=seg_restantes//3600
seg_restantes2=seg_restantes%3600
c=seg_restantes2//60
d=seg_restantes2%60

print(a,"dias,",b,"horas,",c,"minutos e",d,"segundos.")