# Função para verificar se uma string contém apenas números
def contem_apenas_numeros(string):
    return string.replace('.', '', 1).replace(',', '', 1).isdigit()  # Considerando vírgula como separador decimal


# Função para solicitar entrada do usuário e validar se contém apenas números
def input_numero(mensagem):
    while True:
        entrada = input(mensagem)
        if contem_apenas_numeros(entrada):
            return entrada
        else:
            print("Entrada inválida. Digite apenas números.")


# Função para validar a entrada do peso do usuário
def input_peso():
    while True:
        peso = input_numero("Qual seu peso atualmente? (Kg): ")
        try:
            peso_float = float(peso.replace(',', '.'))  # Substitui vírgula por ponto para converter para float
            if 0 < peso_float <= 999:  # Definindo limites para o peso
                return peso_float
            else:
                print("Peso inválido. Digite um valor válido.")
        except ValueError:
            print("Peso inválido. Digite um valor numérico válido.")


# Função para solicitar o objetivo do usuário e validar a entrada
def input_objetivo():
    while True:
        print("\nQual seu objetivo?")
        print("1. Ganhar massa muscular")
        print("2. Perder peso")
        opcao = input("Escolha o número correspondente ao seu objetivo: ")
        if opcao in ['1', '2']:  # Adicionado retorno dos valores dos objetivos selecionados
            return opcao
        else:
            print("Escolha inválida. Por favor, selecione uma opção válida.")


# Função para validar a entrada da altura do usuário
def input_altura():
    while True:
        altura = input_numero("Qual a sua altura? (Em metros e com ponto ou vírgula, Exemplo: 1.60 ou 1,60): ")
        altura = altura.replace(',', '.')  # Substitui vírgula por ponto para garantir que seja um float
        try:
            altura_float = float(altura)
            if 0 < altura_float < 3:  # Considerando altura máxima de 3 metros
                return altura_float
            else:
                print("Altura inválida. Digite um valor entre 0 e 3 metros.")
        except ValueError:
            print("Altura inválida. Digite um valor numérico válido.")


# Função para solicitar e validar a idade do usuário
def input_idade():
    while True:
        idade = input_numero("Qual a sua idade? : ")
        try:
            idade_int = int(idade)
            if 0 < idade_int <= 120:  # Considerando idade máxima de 120 anos
                return idade_int
            else:
                print("Idade inválida. Digite um valor entre 1 e 120 anos.")
        except ValueError:
            print("Idade inválida. Digite um valor numérico válido.")


# Função para solicitar e validar se o usuário pratica atividade física regularmente
def input_atividade_fisica():
    while True:
        print("\nVocê pratica atividade física regularmente?")
        print("1. Sim")
        print("2. Não")
        escolha = input("Escolha o número correspondente à sua resposta: ")
        if escolha in ['1', '2']:
            return escolha
        else:
            print("Escolha inválida. Por favor, selecione uma opção válida.")


# Função para solicitar e validar a duração do sono do usuário
def input_duracao_sono():
    while True:
        print("\nQuantas horas você dorme por noite?")
        print("1. Entre 3 e 5 horas")
        print("2. Entre 6 e 8 horas")
        print("3. Mais de 9 horas")
        escolha = input("Escolha o número correspondente à sua resposta: ")
        if escolha in ['1', '2', '3']:
            return escolha
        else:
            print("Escolha inválida. Por favor, selecione uma opção válida.")


# Função para exibir as opções de intolerância/alergia alimentar
def mostrar_opcoes_intolerancia():
    print("\nVocê possui alguma intolerância ou alergia alimentar?")
    print("1. Lactose")
    print("2. Glúten")
    print("3. Peixes e Frutos do mar")
    print("4. Não tenho intolerâncias")
    print("5. Outro")


# Função para validar a entrada das intolerâncias/alergias alimentares do usuário
# Função para validar a entrada das intolerâncias/alergias alimentares do usuário
def input_intolerancias_alergias():
    while True:
        mostrar_opcoes_intolerancia()
        escolha = input("Escolha o número correspondente à sua resposta: ")
        if escolha in ['1', '2', '3', '4', '5']:
            if escolha == '4':
                return []  # Retorna uma lista vazia se o usuário não tiver intolerâncias
            elif escolha == '5':
                intolerancias = input("Por favor, liste suas intolerâncias ou alergias alimentares separadas por vírgula: ")
                return [intolerancia.strip() for intolerancia in intolerancias.split(',')]  # Separa e remove espaços em branco
            else:
                return [escolha]
        else:
            print("Escolha inválida. Por favor, selecione uma opção válida.")



# Função principal
def main():
    print("(Desenvolvido por Mateus Augusto Souza Aniceto  RU:4088933)")
    print("\nBem-vindo(a) ao Programa de Orientação Nutricional!")
    print("Vamos começar!\n")

    # Coletando informações do usuário
    nome = input("Qual o seu nome? : ")
    idade = input_idade()
    altura = input_altura()
    peso = input_peso()
    sexo = input("Qual o seu sexo? (M/F): ").upper()

    objetivo = input_objetivo()
    atividade_fisica = input_atividade_fisica()
    duracao_sono = input_duracao_sono()
    intolerancias_alergias = input_intolerancias_alergias()

    # Cálculo do IMC
    imc = peso / (altura ** 2)
    print(
        f"\nOlá, {nome}! Com base nas informações fornecidas, seu IMC é de {imc:.2f}, o que indica que você está na categoria de '{categoria_imc(imc)}'.")

    # Cálculo da TMB
    tmb = calcular_tmb(peso, altura, idade, sexo)
    print(f"Sua Taxa Metabólica Basal (TMB) é de {tmb:.2f} calorias por dia.")

    # Cálculo do nível de atividade física
    nivel_atividade = calcular_nivel_atividade(atividade_fisica)
    print(f"Com base no seu nível de atividade física, seu fator de atividade é de {nivel_atividade}.")

    # Cálculo da necessidade calórica diária
    necessidade_calorica = calcular_necessidade_calorica(tmb, nivel_atividade)
    print(f"A sua necessidade calórica diária é de {necessidade_calorica:.2f} calorias.")

    # Cálculo da distribuição de macronutrientes na dieta
    proteinas, gorduras, carboidratos = calcular_macronutrientes(objetivo, necessidade_calorica)
    print(f"\nPara o seu objetivo de {'ganhar massa muscular' if objetivo == '1' else 'perder peso'}, "
          f"você precisa consumir aproximadamente:\n"
          f"- Proteínas: {proteinas:.2f}g\n"
          f"- Gorduras: {gorduras:.2f}g\n"
          f"- Carboidratos: {carboidratos:.2f}g")

    # Gerando e exibindo o plano alimentar personalizado
    plano_alimentar = gerar_plano_alimentar(objetivo, intolerancias_alergias)
    mostrar_plano_alimentar(plano_alimentar)

    # Gerando e exibindo o plano de exercícios personalizado
    local = input("\nOnde pretende realizar os exercícios? (1. Academia / 2. Casa/Rua): ")
    plano_exercicios = gerar_plano_exercicios(objetivo, local)
    mostrar_plano_exercicios(plano_exercicios)


# Função para calcular o índice de massa corporal (IMC)
def categoria_imc(imc):
    if imc < 18.5:
        return 'Abaixo do peso'
    elif 18.5 <= imc < 25:
        return 'Peso normal'
    elif 25 <= imc < 30:
        return 'Sobrepeso'
    else:
        return 'Obesidade'


# Função para calcular a taxa metabólica basal (TMB) usando a Equação de Harris-Benedict revisada
def calcular_tmb(peso, altura, idade, sexo):
    if sexo == 'M':
        return 88.362 + (13.397 * peso) + (4.799 * altura * 100) - (5.677 * idade)
    elif sexo == 'F':
        return 447.593 + (9.247 * peso) + (3.098 * altura * 100) - (4.330 * idade)
    else:
        return None  # Retornar None se o sexo não for válido


# Função para calcular o fator de atividade com base na atividade física
def calcular_nivel_atividade(atividade_fisica):
    if atividade_fisica == '1':  # Atividade física regular
        return 1.55
    elif atividade_fisica == '2':  # Sedentário
        return 1.2
    else:
        return None  # Retornar None se a atividade física não for válida


# Função para calcular a necessidade calórica diária
def calcular_necessidade_calorica(tmb, nivel_atividade):
    if tmb is not None and nivel_atividade is not None:
        return tmb * nivel_atividade
    else:
        return None  # Retornar None se os valores de TMB ou nível de atividade não forem válidos


# Função para calcular a distribuição de macronutrientes na dieta
def calcular_macronutrientes(objetivo, necessidade_calorica):
    if objetivo == '1':  # Ganho de massa muscular
        proteinas = necessidade_calorica * 0.3 / 4  # 30% das calorias totais vêm de proteínas (1g de proteína = 4 cal)
        gorduras = necessidade_calorica * 0.25 / 9  # 25% das calorias totais vêm de gorduras (1g de gordura = 9 cal)
        carboidratos = necessidade_calorica * 0.45 / 4  # 45% das calorias totais vêm de carboidratos (1g de carboidrato = 4 cal)
    else:  # Perda de peso
        proteinas = necessidade_calorica * 0.35 / 4  # 35% das calorias totais vêm de proteínas
        gorduras = necessidade_calorica * 0.25 / 9  # 25% das calorias totais vêm de gorduras
        carboidratos = necessidade_calorica * 0.4 / 4  # 40% das calorias totais vêm de carboidratos
    return proteinas, gorduras, carboidratos


# Função para exibir o plano alimentar de forma mais organizada
def mostrar_plano_alimentar(plano_alimentar):
    print("\nCaso haja um alimento irregular na lista, considere tróca-lo.")
    print("OBS: Isso é uma recomendação, sempre aconselhamos a palavra de um nutricionista para casos mais específicos.")
    print("Plano Alimentar: (São 3 opções para cada hora do dia, à sua escolha)")
    for refeicao, opcoes in plano_alimentar.items():
        print(f"\n{refeicao}:")
        for i, opcao in enumerate(opcoes, start=1):
            print(f"{i}. {opcao}")  # Adicionado número da opção
            # Adicionar descrições das refeições aqui, se necessário


# Função para gerar um plano alimentar personalizado
def gerar_plano_alimentar(objetivo, intolerancias_alergias):
    plano_alimentar = {}

    # Plano alimentar para ganho de peso (Ganho de massa muscular)
    if objetivo == '1':
        plano_alimentar['Café da manhã'] = ['Ovos mexidos com torradas', 'Iogurte com granola',
                                            'Vitamina de banana com aveia']
        plano_alimentar['Lanche da manhã'] = ['Batata-doce assada', 'Frutas secas', 'Shake de proteína']
        plano_alimentar['Almoço'] = ['Frango grelhado com arroz integral e legumes cozidos',
                                     'Salada de quinoa com vegetais e feijão', 'Peixe assado com batata e brócolis']
        plano_alimentar['Lanche da tarde'] = ['Sanduíche de pasta de amendoim', 'Torrada com abacate',
                                              'Queijo cottage com frutas']
        plano_alimentar['Café da tarde'] = ['Iogurte grego com mel e nozes', 'Smoothie de manga e espinafre',
                                            'Tigela de cereal com leite']
        plano_alimentar['Janta'] = ['Carne vermelha assada com purê de batata', 'Salmão grelhado com quinoa',
                                    'Macarrão integral com molho de tomate e frango']
        plano_alimentar['Ceia'] = ['Omelete de claras com queijo cottage', 'Iogurte com aveia e frutas',
                                   'Leite com biscoitos integrais']

    # Plano alimentar para perda de peso
    else:
        plano_alimentar['Café da manhã'] = ['Aveia com frutas', 'Pão integral com queijo branco', 'Iogurte natural']
        plano_alimentar['Lanche da manhã'] = ['Frutas frescas', 'Castanhas', 'Barra de cereal']
        plano_alimentar['Almoço'] = ['Salada verde com frango grelhado', 'Peixe assado com legumes cozidos',
                                     'Sopa de legumes com frango desfiado']
        plano_alimentar['Lanche da tarde'] = ['Cenoura e pepino em palitos com homus', 'Torradas integrais',
                                              'Pão de queijo fit']
        plano_alimentar['Café da tarde'] = ['Iogurte desnatado com granola', 'Shake de proteína', 'Frutas da estação']
        plano_alimentar['Janta'] = ['Salmão grelhado com brócolis', 'Omelete de vegetais', 'Salada de atum com feijão']
        plano_alimentar['Ceia'] = ['Chá verde', 'Leite desnatado', 'Gelatina diet']

    # Remover opções que o usuário tem intolerância/alergia
    for intolerancia in intolerancias_alergias:
        for refeicao, opcoes in plano_alimentar.items():
            plano_alimentar[refeicao] = [opcao for opcao in opcoes if intolerancia.lower() not in opcao.lower()]

    return plano_alimentar


# Função para exibir o plano de exercícios
def mostrar_plano_exercicios(plano_exercicios):
    print("\nPlano de Exercícios:")
    for dia, exercicios in plano_exercicios.items():
        print(f"\nDia {dia}:")
        for exercicio in exercicios:
            print(f"- {exercicio}")
    print("\nLembre-se de sempre consultar um profissional de educação física antes de iniciar uma rotina de exercícios!")


# Função para gerar um plano de exercícios personalizado
def gerar_plano_exercicios(objetivo, local):
    plano_exercicios = {}

    # Plano de exercícios para ganho de massa muscular (musculação)
    if objetivo == '1':
        if local == '1':  # Academia
            plano_exercicios['Segunda-feira'] = ['Supino reto', 'Desenvolvimento com halteres', 'Remada curvada',
                                                 'Leg press', 'Cadeira extensora', 'Panturrilha no leg press']
            plano_exercicios['Quarta-feira'] = ['Levantamento terra', 'Pull ups', 'Elevação lateral',
                                                'Agachamento livre',
                                                'Cadeira flexora', 'Gêmeos em pé']
            plano_exercicios['Sexta-feira'] = ['Rosca direta', 'Tríceps testa', 'Elevação frontal', 'Mesa flexora',
                                               'Abdução de quadril', 'Panturrilha sentado']
        else:  # Casa/Rua
            plano_exercicios['Segunda-feira'] = ['Flexão de braço', 'Agachamento', 'Prancha', 'Afundo',
                                                 'Bicicleta no chão']
            plano_exercicios['Quarta-feira'] = ['Barra fixa', 'Salto com corda', 'Abdominal', 'Flexão de perna',
                                                'Polichinelo']
            plano_exercicios['Sexta-feira'] = ['Flexão diamante', 'Corrida leve', 'Burpee', 'Prancha lateral',
                                               'Agachamento sumô']

    # Plano de exercícios para perda de peso (cardio + treinamento funcional)
    else:
        if local == '1':  # Academia
            plano_exercicios['Segunda-feira'] = ['Esteira (30 minutos)', 'Transport', 'Remo', 'Prancha',
                                                 'Abdominal na bola suíça']
            plano_exercicios['Quarta-feira'] = ['Bicicleta ergométrica (30 minutos)', 'Step', 'Corda naval',
                                                'Prancha lateral',
                                                'Flexão de braço na bola suíça']
            plano_exercicios['Sexta-feira'] = ['Escada (10 minutos)', 'Elíptico', 'Kettlebell swing',
                                               'Agachamento com salto',
                                               'Flexão de braço com bola suíça']
        else:  # Casa/Rua
            plano_exercicios['Segunda-feira'] = ['Corrida leve (30 minutos)', 'Agachamento com salto',
                                                 'Flexão de braço',
                                                 'Prancha', 'Abdominal']
            plano_exercicios['Quarta-feira'] = ['Caminhada rápida (30 minutos)', 'Polichinelo', 'Prancha lateral',
                                                'Abdominal',
                                                'Flexão de braço']
            plano_exercicios['Sexta-feira'] = ['Corrida intervalada (20 minutos)', 'Agachamento sumô',
                                               'Flexão diamante',
                                               'Prancha lateral', 'Abdominal na bola suíça']

    return plano_exercicios


# Início do programa
if __name__ == "__main__":
    main()