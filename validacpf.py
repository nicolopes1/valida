print '\n============================ Validacao de CPF =================================\n'
n1 = input('Digite o primeiro numero do seu cpf: ')
n2 = input('Digite o segundo numero do seu cpf: ')
n3 = input('Digite o terceiro numero do seu cpf: ')
n4 = input('Digite o quarto numero do seu cpf: ')
n5 = input('Digite o quinto numero do seu cpf: ')
n6 = input('Digite o sexto numero do seu cpf: ')
n7 = input('Digite o setimo numero do seu cpf: ')
n8 = input('Digite o oitavo numero do seu cpf: ')
n9 = input('Digite o nono numero do seu cpf: ')

validarprimeirodigito1 = n1 * 10;
validarprimeirodigito2 = n2 * 9;
validarprimeirodigito3 = n3 * 8;
validarprimeirodigito4 = n4 * 7;
validarprimeirodigito5 = n5 * 6;
validarprimeirodigito6 = n6 * 5;
validarprimeirodigito7 = n7 * 4;
validarprimeirodigito8 = n8 * 3;
validarprimeirodigito9 = n9 * 2;

ResultadoPrimeiroDigito = validarprimeirodigito1 + validarprimeirodigito2 + validarprimeirodigito3 + validarprimeirodigito4 + validarprimeirodigito5 + validarprimeirodigito6 + validarprimeirodigito7 + validarprimeirodigito8 + validarprimeirodigito9

'''print ResultadoPrimeiroDigito'''

passo2 = ((ResultadoPrimeiroDigito * 10) % 11)

'''print passo2'''

primeiroNumeroCpf = input('Digite o primeiro numero do CPF apos o  " - " : ')

def validar1():
	if (passo2 == primeiroNumeroCpf):
		print '\n >> Seu CPF passou na validacao do primeiro digito ! \n'
		return True;

	else:
		print '\n >> Seu CPF nao passou na valicadao do primeiro digito ! \n'
		return False;


''' validacao do segundo digito '''

ValidarSegundoDigito1 = n1 * 11;
ValidarSegundoDigito2 = n2 * 10;
ValidarSegundoDigito3 = n3 * 9;
ValidarSegundoDigito4 = n4 * 8;
ValidarSegundoDigito5 = n5 * 7;
ValidarSegundoDigito6 = n6 * 6;
ValidarSegundoDigito7 = n7 * 5;
ValidarSegundoDigito8 = n8 * 4;
ValidarSegundoDigito9 = n9 * 3;
ValidarSegundoDigito10 = primeiroNumeroCpf * 2;

ResultadoSegundoDigito = ValidarSegundoDigito1 + ValidarSegundoDigito2 + ValidarSegundoDigito3 + ValidarSegundoDigito4 + ValidarSegundoDigito5 + ValidarSegundoDigito6 + ValidarSegundoDigito7 + ValidarSegundoDigito8 + ValidarSegundoDigito9 + ValidarSegundoDigito10

'''print 'O resultado do segundo digito eh ' + str(ResultadoSegundoDigito)'''

passo3 = ((ResultadoSegundoDigito * 10) % 11)
if (passo3 == 10):
	passo3 = 0;
'''print passo3'''

segundoNumeroCpf = input('Digite o segundo numero do CPF apos o " - " : ')

def validar2():
	if (passo3 == segundoNumeroCpf):
		print '\n >> Seu CPF passou na validacao do segundo digito ! \n'
		return True;

	else:
		print '\n >> Seu CPF nao passou na  validacao do segundo digito ! \n'
		return False;

if (validar1() == True):
	if(validar2() == True):
		print '\n ------------------ Seu CPF e valido !! ------------------ \n'

	else:
		print '\nSeu CPF e invalido !! \n'
else:
	'\nErro !\n'