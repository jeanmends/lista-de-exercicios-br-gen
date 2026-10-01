with open("preproinsulin-seq.txt", "r", encoding="utf-8") as arquivo:
    conteudo = arquivo.read()
    insulin_seq = conteudo

if "ORIGIN" in conteudo:
    conteudo = conteudo.split("ORIGIN")[1]


conteudo = conteudo.replace("//", "").replace(".", "").replace(";", "")

sequencia_limpa = "".join([char for char in conteudo if char.isalpha()])

preproInsulin = sequencia_limpa

# -*- coding: utf-8 -*-
# Versao do Python utilizada: Python 3.x
# Codificacao do arquivo: UTF-8

# ==============================================================================
# EXERCÍCIO 1: Atribuir variáveis aos elementos da sequência de insulina humana
# ==============================================================================

# Sequência completa da pré-proinsulina humana
preproInsulin = "malwmrllpl lallalwgpd paaafvnqhl cgshlvealy lvcgergffy tpktrreaed" \
                "lqvgqvelgg gpgagslqpl alegslqkrg iveqcctsic slyqlenycn"

# Partes da sequência de insulina
isInsulin = "malwmrllpl lallalwgpd paaa"
bInsulin = "fvnqhlcgsh lvealylvcg ergffytpkt r"
aInsulin = "giveqcctsicslyqlenycn"
cInsulin = "reaedlqvgqvelgggpgagslqplalegslqkr"

# Combinação da cadeia A com a cadeia B (Insulina madura)
insulin = bInsulin + aInsulin


# ==============================================================================
# EXERCÍCIO 3: Usar print() para exibir as sequências
# ==============================================================================

# Imprimindo a sequência da insulina humana no console
print("Apresentando a sequência da pré-proinsulina humana:")
print(preproInsulin)

# Exibição concatenada usando o operador +
print("Cadeia A da insulina: " + aInsulin)

# Exibição alternativa passando múltiplos argumentos separados por vírgula
print("Insulina combinada (Cadeia B + Cadeia A):", insulin)


# ==============================================================================
# EXERCÍCIO 4: Calcular o peso molecular aproximado da insulina
# ==============================================================================

# Dicionário com os pesos aproximados de cada aminoácido
aaWeights = {
    'A': 89.09, 'C': 121.16, 'D': 133.10, 'E': 147.13, 'F': 165.19,
    'G': 75.07, 'H': 155.16, 'I': 131.17, 'K': 146.19, 'L': 131.17,
    'M': 149.21, 'N': 132.12, 'P': 115.13, 'Q': 146.15, 'R': 174.20,
    'S': 105.09, 'T': 119.12, 'V': 117.15, 'W': 204.23, 'Y': 181.19
}

# Contagem das ocorrências de cada aminoácido na insulina (convertida para maiúsculas)
insulin_upper = insulin.upper()
aaCountInsulin = {x: float(insulin_upper.count(x)) for x in ['A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'Y']}

# Cálculo do peso molecular estimado
molecularWeightInsulin = sum({x: (aaCountInsulin[x] * aaWeights[x]) for x in ['A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'Y']}.values())

print("\nPeso molecular calculado da insulina (estimado):", molecularWeightInsulin)

# Variável contendo o peso molecular real aceito
molecularWeightInsulinActual = 5807.63

# Cálculo do percentual de erro: ((medido - aceito) / aceito) * 100
errorPercentage = ((molecularWeightInsulin - molecularWeightInsulinActual) / molecularWeightInsulinActual) * 100

# Exibição do percentual de erro convertido para string com str()
print("Percentual de erro no cálculo: " + str(errorPercentage) + "%")


