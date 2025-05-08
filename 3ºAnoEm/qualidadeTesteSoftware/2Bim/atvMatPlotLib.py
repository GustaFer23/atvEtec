# 6. Peça ao usuário para informar quantas horas ele passou em um dia: dormindo, estudando e em lazer. Crie
# um gráfico de pizza com esses dados.
horas = []
momentos = ['Dormindo', 'Estudando', 'Ocioso']

print("Pensando no seu último dia, você: dormiu(1), estudou(2) e esteve em lazer(3) por quantas horas?")
for i in range(3):
    hora = input(f"Horas no {i+1}° hábito: ")
    horas.append(hora)

plt.pie(horas, labels=momentos, autopct="%.2f%%")
plt.title("Sua rotina em %")
plt.show()

# 7. Crie um gráfico de linha que mostre a velocidade de um carro ao longo do tempo. Use os dados: tempo [0, 5,
# 10, 15, 20] segundos e velocidade [0, 20, 40, 35, 50] km/h.
"""
tempoS = [0, 5, 10, 15, 20]
velocidadeKmh = [0, 20, 40, 35, 50]


plt.plot(tempoS, velocidadeKmh)
plt.title("Amostra da velocidade do carro", fontsize=20)
plt.xlabel("Tempo em segundos")
plt.ylabel("Velocidade (Km/h)")
plt.show()

# 8. Peça ao usuário para digitar quantas bananas, maçãs e laranjas ele comeu na semana. Mostre os dados em
# um gráfico de barras.
qntdd = []
frutas = ['Bananas', 'Maçãs', 'Laranjas']

print("Nesta semana, você comeu quantas: bananas(1), maçãs(2) e laranjas(3)?")
for i in range(3):
    qtd = int(input(f"Quantidade comida da {i+1}ª fruta: "))
    qntdd.append(qtd)

plt.bar(frutas, qntdd)
plt.title("Quantidade de frutas ingeridas (separadamente)", fontsize=15)
plt.show()

# 9. Peça ao usuário para digitar quantas horas ele usa por dia as seguintes redes sociais: Instagram, YouTube,
# TikTok, WhatsApp e Outros. Crie um gráfico de pizza com essas informações.
horas = []
redes = ['Instagram', 'YouTube', 'Whats', 'Tktk']

print("Por quantas horas você utiliza, num dia: instagram(1), youtube(2), whatsapp(3) e tik tok?")
for i in range(4):
    hora = input(f"Horas diárias no {i+1}° app: ")
    horas.append(hora)

plt.pie(horas, labels=redes, autopct="%.2f%%")
plt.title("Uso dessas redes em %")
plt.show()

# 10. Peça ao usuário para digitar o seu nível de energia (de 0 a 10) pela manhã, à tarde e à noite. Crie um gráfico
# de linha com esses dados
nivelEnergia = []
periodoDia = ['Manhã', 'Tarde', 'Noite']

print("Quanta energia você tem, num índice de 0 a 10,"
      " nas seguintes partes do dia: manhã(1), tarde(2), noite(3)?")
for i in range(3):
    nvlNrg = input(f"Energia na {i+1}ª parte:")
    nivelEnergia.append(nvlNrg)
