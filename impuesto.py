def impuesto_aplicado(monto,imp):

    pcimp=monto+monto*(imp/100)
    return pcimp


monto=float(input("Introduce la cantidad:"))
impuesto=float(input("Introduce el impuesto:"))
print("El pago con impuesto es ",impuesto_aplicado(monto,impuesto))
