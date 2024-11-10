# Extração de medicamentos
print("medicamentos")
medicamentos = df['processed_text'].str.extract(r'medicamento\s+(\w+)', expand=True)
print("value_counts", medicamentos.value_counts())
print("\n")

# Extração de exames
print("exames")
exames = df['processed_text'].str.extract(r'exame\s+(\w+)', expand=True)
print("value_counts",exames.value_counts())
print("\n")

print("doenças")
# Extração de doenças
doenças = df['processed_text'].str.extract(r'doença\s+(\w+)', expand=True)
print("value_counts",doenças.value_counts())
print("\n")