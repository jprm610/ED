class Mensaje :
    def __init__(self, remitente, destinatario, time, asunto, texto, bandeja) -> None:
        self.remitente = remitente
        self.destinatario = destinatario
        self.time = time
        self.asunto = asunto
        self.texto = texto
        self.bandeja = bandeja
        
    def toString(self, short=True) :
        if short :
            return f"{self.time} / {self.remitente} -> {self.destinatario} / {self.asunto}"

        return f"""
            {self.remitente} -> {self.destinatario} - {self.time}
            {self.asunto}
            ---------------------------------------------------
            {self.texto}
            """
