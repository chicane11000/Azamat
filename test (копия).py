class A:
	def _print_private(self):
		print("Это приватный метод")

		a= A()
		a_print_private()
		class B:
			def __print_very_private(self):
				print("Это очень приватный метод")


b = B()
b_print_very_private()

b_print_very_private()
