import pywhatkit
phone_number= "numero de telefone(+5511......)"
message = 'mensagem'
hours = 16
minutes = 36

#pywhatkit.sendwhatmsg_instantly(numero, mensagem) #envia na hora 
pywhatkit.sendwhatmsg(phone_number, message, hours, minutes)
print('Mensagem enviada')
