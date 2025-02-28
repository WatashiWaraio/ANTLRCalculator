def main():

    visitor=Evalvisitor() #Instancia visitor

    while True:
        expr=input("ingrese una expresion: ")

        texto=InputStream(expr + "\n")
        lexer=LabeledExprLexer(texto)
        TokenStream=CommonTokenStream(lexer)
        parser=LabeledExprParser(TokenStream)
        arbol= parser.prog()

        result=visitor.visit(arbol) #evaluar con el visitor

        if result is not None:
            print("Resultado: ", result)

if name=="main":
    main()