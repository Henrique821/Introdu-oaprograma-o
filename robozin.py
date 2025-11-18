modo=(input("qual o modo de operação(plantio,colheita,irrigação)"))
umi=int(input("informe a umidade do solo com um número inteiro de 0 a 100: "))
temp=input("informe a temperatura do ambiente: ")
bat=int(input("informe a bateria do robo com um número inteiro de 1 a 100: "))
if bat<20:
    print("bateria muito baixa!Retorne imediatamente para a base")
if bat>= 20 and bat>50:
    ("atenção bateria em nível moderado")
if bat>=50:
    print("Bateria suficiente para operação")
if temp>40:
    print("Temperatura crítica! operação suspensa")
if temp<5:
    print("frio extremo! modo de economia ativado")
if umi<30:
    print("solo muito seco. Recomendo iniciar a irrigação")
if umi>80:
    print("solo encharcado! suspenda a irrigação imediatamente")
if modo=="plantio":
    print("iniciando modo plantio... ")
if modo=="colheita":
    print("iniciando modo colheita... ")
if modo=="irrigação":
    print("iniciando modo irrigação... ")
    