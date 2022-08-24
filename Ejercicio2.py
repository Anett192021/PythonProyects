def ivaProd():
    producto = float(input("Ingrese el precio del producto: "));
    result = (producto + 1.15);

    print("El precio con IVA del producto es: " + result.ToString())

    ivaProd()