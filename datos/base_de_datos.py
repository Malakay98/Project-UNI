import sqlite3


class BaseDeDatos:
    url_base_de_datos = 'Universidad.db'

    def _crear_conexion(self):
        try:
            # Se crea la conexion a la base de datos
            self.conexion = sqlite3.connect(BaseDeDatos.url_base_de_datos)
            # Si ocurre algun error, se nos informara
        except Exception as e:
            print(e)

    def _cerrar_conexion(self):
        self.conexion.close()
        self.conexion = None

    def ejecutar_sql(self, sql, retornar_id_creado=False):
        self._crear_conexion()
        cur = self.conexion.cursor()
        cur.execute(sql)

        filas = cur.fetchall()

        if retornar_id_creado:
            filas = cur.lastrowid

        # Gurdamos los cambios con el metodo commit()
        self.conexion.commit()
        # Cerramos la conexion con la funcion previamente creada
        self._cerrar_conexion()
        return filas