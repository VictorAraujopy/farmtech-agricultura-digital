import math
from dataclasses import dataclass, asdict


@dataclass
class TalhaoBase:
    nome: str  # Identificador/nome do talhão
    ruas: int  # Quantidade de ruas (linhas de plantio) no talhão
    metros_por_rua: float  # Comprimento de cada rua, em metros
    dose_ml_por_m: float  # Dose (em mL) aplicada por metro linear

    def calcular_litros(self) -> float:
        """Cálculo da quantidade total de insumo (em L) para o talhão

        :return: float - com a quantidade total de insumo (em L)

        Lógica: número_de_ruas * metros_por_rua * (dose_mL_por_m / 1000 para converter mL -> L).
        Exemplo: 10 ruas * 100 m/rua * 500 mL/m = 500.000 mL -> 500 L
        """
        return self.ruas * self.metros_por_rua * (self.dose_ml_por_m / 1000)

    def calcular_area(self):
        """Método "genérico" (na classe-mãe) — cada cultura calcula área de um jeito"""
        raise NotImplementedError(f"Implementar função {type(self).__name__} na subclasse")

    def to_row(self, cultura: str) -> list:
        return [
            cultura,
            self.nome,
            self.calcular_area(),
            self.ruas,
            self.metros_por_rua,
            self.dose_ml_por_m,
            self.calcular_litros(),
        ]


@dataclass
class TalhaoSoja(TalhaoBase):
    """Classe responsável pelas regras da cultura Soja

    Cultura "soja": área em formato de círculo (usamos o raio)
    """
    raio: float  # Raio do talhão circular, em metros

    def calcular_area(self):
        return math.pi * (self.raio ** 2)


@dataclass
class TalhaoCafe(TalhaoBase):
    """Classe responsável pelas regras da cultura Café

    Cultura "café": área em formato de retângulo (comprimento x largura)
    """
    comprimento: float  # Comprimento do talhão, em metros
    largura: float  # Largura do talhão, em metros
    # Observação: mantemos tudo em metros para padronizar e evitar conversões depois.

    def calcular_area(self):
        """Área do retângulo = comprimento * largura"""
        return self.comprimento * self.largura

