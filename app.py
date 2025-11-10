class Imovel:
    def __init__(self, tipo, quartos, vagas, tem_criancas):
        self.tipo = tipo
        self.quartos = quartos
        self.vagas = vagas
        self.tem_criancas = tem_criancas


class Orcamento:
    CONTRATO_VALOR = 2000

    def __init__(self, imovel, parcelas_contrato):
        self.imovel = imovel
        self.parcelas_contrato = parcelas_contrato

    def calcular(self):
        tipo = self.imovel.tipo
        quartos = self.imovel.quartos
        vagas = self.imovel.vagas
        tem_criancas = self.imovel.tem_criancas

        # Valores base
        if tipo == "apartamento":
            aluguel_base = 700
            if quartos == 2:
                aluguel_base += 200
        elif tipo == "casa":
            aluguel_base = 900
            if quartos == 2:
                aluguel_base += 250
        else:
            aluguel_base = 1200

        # Vagas
        if tipo == "estudio":
            acresc_vagas = 0
            if vagas >= 2:
                acresc_vagas += 250
                acresc_vagas += max(vagas - 2, 0) * 60
            elif vagas == 1:
                acresc_vagas += 60
        else:
            acresc_vagas = vagas * 300

        # Desconto
        desconto = 0
        if tipo == "apartamento" and not tem_criancas:
            desconto = aluguel_base * 0.05

        aluguel_final = aluguel_base + acresc_vagas - desconto

        parcela_contrato = (
            self.CONTRATO_VALOR / self.parcelas_contrato
            if self.parcelas_contrato > 0
            else 0
        )

        return aluguel_final, parcela_contrato
