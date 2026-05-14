def analizador_encuestas():
    encuesta = {
        "pregunta1": "¿Cuál es tu color favorito?",
        "pregunta2": "¿Cuál es tu comida favorita?",
        "pregunta3": "¿Cuál es tu deporte favorito?"
    }
 
    respuestas = {
        "pregunta1": [],
        "pregunta2": [],
        "pregunta3": []
    }
 
    def realizar_encuesta():
        print("\n=== ENCUESTA ===")
        respuesta_persona = {}
 
        for codigo, pregunta in encuesta.items():
            respuesta = input(f"{pregunta} ")
            respuesta_persona[codigo] = respuesta
            respuestas[codigo].append(respuesta)
 
        print("¡Gracias por participar!")
 
    def generar_estadisticas():
        print("\n=== ESTADÍSTICAS ===")
 
        for codigo, pregunta in encuesta.items():
            print(f"\n{pregunta}")
            print("-" * len(pregunta))
 
            if not respuestas[codigo]:
                print("No hay respuestas")
                continue
 
            # Contar frecuencias
            contador = {}
            for respuesta in respuestas[codigo]:
                respuesta_lower = respuesta.lower()
                contador[respuesta_lower] = contador.get(respuesta_lower, 0) + 1
 
            total_respuestas = len(respuestas[codigo])
 
            # Mostrar estadísticas
            for respuesta, frecuencia in contador.items():
                porcentaje = (frecuencia / total_respuestas) * 100
                print(f"{respuesta.title()}: {frecuencia} ({porcentaje:.1f}%)")
 
            # Respuesta más común
            if contador:
                mas_comun = max(contador, key=contador.get)
                print(f"Más popular: {mas_comun.title()}")
 
    def reporte_final():
        print("\n=== REPORTE FINAL ===")
        total_participantes = len(respuestas["pregunta1"]) if respuestas["pregunta1"] else 0
        print(f"Total de participantes: {total_participantes}")
 
        if total_participantes > 0:
            generar_estadisticas()
        else:
            print("No hay datos para generar reporte")
 
    while True:
        print("\n=== ANALIZADOR DE ENCUESTAS ===")
        print("1. Realizar encuesta")
        print("2. Ver estadísticas")
        print("3. Reporte final")
        print("4. Salir")
 
        opcion = input("Opción: ")
 
        if opcion == "1":
            realizar_encuesta()
        elif opcion == "2":
            generar_estadisticas()
        elif opcion == "3":
            reporte_final()
        elif opcion == "4":
            break
 
analizador_encuestas()