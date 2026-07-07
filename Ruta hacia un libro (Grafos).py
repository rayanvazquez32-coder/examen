    def buscar_ruta(self, inicio, destino, visitados=[]):

        visitados = visitados + [inicio]

        if inicio == destino:
            return visitados

        for vecino in self.grafo[inicio]:

            if vecino not in visitados:

                ruta = self.buscar_ruta(
                    vecino,
                    destino,
                    visitados
                )

                if ruta:
                    return ruta

        return None