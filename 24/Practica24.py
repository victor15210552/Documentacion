class Consulta(object):

	def __init__(self, saldo, titular, credito, productos=['producto1','producto2','producto3']):
		self.saldo = saldo
		self.titular = titular
		self.credito = credito
		self.productos = productos

	def get_saldo(self):
		return self.saldo

	def get_info(self):
		return self.titular

	def get_credito(self):
		return self.credito

	def get_producto(self):
		return self.productos		

	def __str__(self):
		return "%s tiene un saldo de %s\n un credito de %s\n y productos %s" % (self.titular, self.saldo, self.credito, self.productos)

#consul = Consulta(1000, 'Cliente', 0)
#print (consul)

class Deposito(object):

	def __init__(self, saldo=0):
		self.saldo = saldo

	def efectivo(self, monto):
		self.saldo += monto
		print ("Se han depositado %s en efectivo" % (monto))
		print ("Su saldo es de %s" % (self.saldo))

	def cheque(self, monto, no_cheque=100234):
		self.saldo += monto
		print ("Se han depositado %s desde un cheque con el numero %s " % (monto, no_cheque))
		print ("Su saldo es de %s" % (self.saldo))

	def transferencia(self, monto, no_transferencia=230191):
		self.saldo += monto
		print ("Se han depositado %s desde una transferencia con el numero %s " % (monto, no_transferencia))
		print ("Su saldo es de %s" % (self.saldo))

#dep = Deposito()
#dep.efectivo(2000)
#dep.cheque(500)
#dep.transferencia(1000)


class Retiro(object):

	def __init__(self, saldo = 5000):
		self.saldo = saldo

	def cajero(self, monto):
		self.saldo -= monto
		print ("Se han retirado %s desde un cajero automatico" % (monto))
		print ("Su saldo es de %s" % (self.saldo))

	def ventanilla(self, monto, no_ventanilla=1):
		self.saldo -= monto
		print ("Se han retirado %s desde la ventanilla numero %s" % (monto, no_ventanilla))
		print ("Su saldo es de %s" % (self.saldo))

#ret = Retiro()
#ret.cajero(1000)
#ret.ventanilla(500)

class Reporte(object):

	def __init__(self, productos=['Cuentas','Cheques','Seguros'], movimientos=['depositos','retiros','transferencias'], informacion="Lorem ipsum dolor"):
		self.productos = productos
		self.movimientos = movimientos
		self. informacion = informacion

	def get_prod(self):
		return self.productos

	def get_mov(self):
		return self.movimientos

	def get_info(self):
		return self.informacion

	def __str__(self):
		return "Productos: %s\nMovimientos: %s\nInformacion: %s" % (self.productos, self.movimientos, self.informacion)

#rep1 = Reporte()
#print (rep1)

class Asignacion(object):

	def __init__(self, cliente, producto=['1-Cuenta','2-Cheque','3-Seguro'], productos_cliente = []):
		self.cliente = cliente
		self.producto = producto
		self.productos_cliente = productos_cliente

	def asignar(self):
		print ("Productos: %s" % (self.producto))
		opcion = int(input("Que producto quiere asignar?"))

		if (opcion == 1):
			self.productos_cliente.append('Cuenta')
			print ("Cuenta asignada a %s" % (self.cliente))
			print ("Productos de cliente: %s" % (self.productos_cliente))
		elif (opcion == 2):
			self.productos_cliente.append('Cheque')
			print ("Cheque asignado a %s" % (self.cliente))
			print ("Productos de cliente: %s" % (self.productos_cliente))
		else:
			self.productos_cliente.append('Seguro')
			print ("Seguro asignada a %s" % (self.cliente))
			print ("Productos de cliente: %s" % (self.productos_cliente))

asign = Asignacion('cliente')
asign.asignar()
