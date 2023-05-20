def encriptar_mensaje(mensaje):
    contador = 0
    parte_a_bytes = bytearray()
    parte_b_bytes = bytearray()
    mensaje_encriptado = bytearray()
    while contador < len(mensaje):
        parte_a_bytes += mensaje[contador : contador + 1]
        parte_b_bytes += mensaje[contador + 1 : contador + 2]
        parte_a_bytes += mensaje[contador + 2 : contador + 4]
        parte_b_bytes += mensaje[contador + 4 : contador + 6]
        contador += 6

    if len(parte_a_bytes) % 2 == 0:
        mitad = int(len(parte_a_bytes) / 2)
        byte_central1 = parte_a_bytes[len(parte_a_bytes) - mitad - 1]
        byte_central2 = parte_a_bytes[len(parte_a_bytes) - mitad]
        suma_parte_a = byte_central1 + byte_central2
    else:
        if len(parte_a_bytes) == 1:
            suma_parte_a = parte_a_bytes[0]
        else:
            mitad = len(parte_a_bytes) // 2
            byte_central1 = parte_a_bytes[mitad - 1]
            byte_central2 = parte_a_bytes[mitad]
            byte_central3 = parte_a_bytes[mitad + 1]
            promedio = (byte_central1 + byte_central3) / 2
            suma_parte_a = byte_central2 + promedio

    if len(parte_b_bytes) % 2 == 0:
        if len(parte_b_bytes) == 0:
            suma_parte_b = 0
        else:
            mitad = int(len(parte_b_bytes) / 2)
            byte_central1 = parte_b_bytes[len(parte_b_bytes) - mitad - 1]
            byte_central2 = parte_b_bytes[len(parte_b_bytes) - mitad]
            suma_parte_b = byte_central1 + byte_central2
    else:
        if len(parte_b_bytes) == 1:
            suma_parte_b = parte_b_bytes[0]
        else:
            mitad = len(parte_b_bytes) // 2
            byte_central1 = parte_b_bytes[mitad - 1]
            byte_central2 = parte_b_bytes[mitad]
            byte_central3 = parte_b_bytes[mitad + 1]
            promedio = (byte_central1 + byte_central3) / 2
            suma_parte_b = byte_central2 + promedio

    if suma_parte_a <= suma_parte_b:
        mensaje_encriptado.extend(b"\x01")
        mensaje_encriptado.extend(parte_a_bytes)
        mensaje_encriptado.extend(parte_b_bytes)
    else:
        mensaje_encriptado.extend(b"\x00")
        mensaje_encriptado.extend(parte_b_bytes)
        mensaje_encriptado.extend(parte_a_bytes)

    return mensaje_encriptado


def desencriptar_mensaje(mensaje_encriptado):
    if mensaje_encriptado[0] == 1:
        orden = 1
    elif mensaje_encriptado[0] == 0:
        orden = 2

    mensaje = mensaje_encriptado.decode("utf-8")[1:]

    if len(mensaje) == 1:
        return mensaje
    mensaje_desencriptado = ""
    i = 0
    indices_utilizados = []
    # SI ES IMPAR LA MITAD CALZA PERFECT
    mitad = len(mensaje) // 2
    if orden == 1:
        if len(mensaje) >= 6:
            if len(mensaje) % 6 == 0:
                mitad -= 1
            elif (len(mensaje) - 2) % 6 == 0:
                mitad -= 1
        while len(mensaje_desencriptado) < len(mensaje):
            mensaje_desencriptado += mensaje[i]
            indices_utilizados.append(i)
            if len(mensaje_desencriptado) == len(mensaje) - 1:
                break

            mensaje_desencriptado += mensaje[i + mitad + 1]
            indices_utilizados.append(i + mitad + 1)
            if len(mensaje_desencriptado) == len(mensaje) - 1:
                break

            mensaje_desencriptado += mensaje[i + 1]
            indices_utilizados.append(i + 1)
            if len(mensaje_desencriptado) == len(mensaje) - 1:
                break

            mensaje_desencriptado += mensaje[i + 2]
            indices_utilizados.append(i + 2)
            if len(mensaje_desencriptado) == len(mensaje) - 1:
                break

            mensaje_desencriptado += mensaje[i + mitad + 2]
            indices_utilizados.append(i + mitad + 2)
            if len(mensaje_desencriptado) == len(mensaje) - 1:
                break

            mensaje_desencriptado += mensaje[i + mitad + 3]
            indices_utilizados.append(i + mitad + 3)
            if len(mensaje_desencriptado) == len(mensaje) - 1:
                break
            i += 3
        for i in range(len(indices_utilizados) + 1):
            if i not in indices_utilizados:
                mensaje_desencriptado += mensaje[i]

    elif orden == 2:
        if len(mensaje) >= 10:
            if (len(mensaje) + 2) % 6 == 0:
                mitad -= 1
        while len(mensaje_desencriptado) < len(mensaje):
            mensaje_desencriptado += mensaje[i + mitad]
            indices_utilizados.append(i + mitad)
            if len(mensaje_desencriptado) == len(mensaje) - 1:
                break

            mensaje_desencriptado += mensaje[i]
            indices_utilizados.append(i)
            if len(mensaje_desencriptado) == len(mensaje) - 1:
                break

            mensaje_desencriptado += mensaje[i + mitad + 1]
            indices_utilizados.append(i + mitad + 1)
            if len(mensaje_desencriptado) == len(mensaje) - 1:
                break

            mensaje_desencriptado += mensaje[i + mitad + 2]
            indices_utilizados.append(i + mitad + 2)
            if len(mensaje_desencriptado) == len(mensaje) - 1:
                break

            mensaje_desencriptado += mensaje[i + 1]
            indices_utilizados.append(i + 1)
            if len(mensaje_desencriptado) == len(mensaje) - 1:
                break

            mensaje_desencriptado += mensaje[i + 2]
            indices_utilizados.append(i + 2)
            if len(mensaje_desencriptado) == len(mensaje) - 1:
                break
            i += 3
        for i in range(len(indices_utilizados) + 1):
            if i not in indices_utilizados:
                mensaje_desencriptado += mensaje[i]

    return mensaje_desencriptado


def traspasar_chunks(mensaje_encriptado):
    largo_mensaje_encriptado = len(mensaje_encriptado)
    cantidad_bloques = largo_mensaje_encriptado // 20
    if largo_mensaje_encriptado % 20 != 0:
        cantidad_bloques += 1
    cantidad_bloques_bytes = cantidad_bloques.to_bytes(4, byteorder="little")
    TAMANO_CHUNK = 20
    contador_bloques = 0
    mensaje_final = bytearray(cantidad_bloques_bytes)

    for i in range(0, largo_mensaje_encriptado, TAMANO_CHUNK):
        # Aqui obtenemos nuestro chunk
        numero_bloque = contador_bloques.to_bytes(4, byteorder="big")
        chunk = bytearray(numero_bloque)
        mensaje_chunk = mensaje_encriptado[i : i + TAMANO_CHUNK]

        if len(mensaje_chunk) == 20:
            chunk.extend(b"\x01")
            largo_chunk = 20
            largo_chunk_bytes = largo_chunk.to_bytes(1, byteorder="big")
            chunk.extend(largo_chunk_bytes)
        else:
            chunk.extend(b"\x00")
            largo_chunk = len(mensaje_chunk)
            largo_chunk_bytes = largo_chunk.to_bytes(1, byteorder="big")
            chunk.extend(largo_chunk_bytes)
        chunk.extend(mensaje_chunk)
        contador_bloques += 1

        mensaje_final.extend(chunk)

    return mensaje_final
