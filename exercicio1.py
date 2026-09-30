insulin_seq = ""

with open("preproinsulin-seq.txt", "r", encoding="utf-8") as arquivo:
    conteudo = arquivo.read()
    insulin_seq = conteudo

if "ORIGIN" in conteudo:
    conteudo = conteudo.split("ORIGIN")[1]

# 2. Remove as marcações de fim de arquivo
conteudo = conteudo.replace("//", "").replace(".", "").replace(";", "")

# 3. Filtra mantendo apenas as letras
sequencia_limpa = "".join([char for char in conteudo if char.isalpha()])

print(f"Tamanho retornado: {len(sequencia_limpa)}")
print(f"Sequência: {sequencia_limpa}")