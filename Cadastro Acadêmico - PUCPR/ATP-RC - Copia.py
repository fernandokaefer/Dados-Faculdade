#Fernando Kaefer - Análise e desenvolvimento de sistemas - Raciocínio Computacional.


import json

# Função para salvar dados em formato JSON
def salvar_dados_json(dados, nome_arquivo):
    with open(nome_arquivo, 'w') as f:
        json.dump(dados, f)
        print("Dados salvos com sucesso em", nome_arquivo)

# Função para carregar dados em formato JSON
def carregar_dados_json(nome_arquivo):
    try:
        with open(nome_arquivo, 'r') as f:
            dados = json.load(f)
        return dados
    except FileNotFoundError:
        print("Arquivo", nome_arquivo, "não encontrado.")
        return None

# Lista que carrega dados do JSON quando o programa inicia
estudantes = carregar_dados_json('estudantes.json') or []
professores = carregar_dados_json('professores.json') or []
disciplinas = carregar_dados_json('disciplinas.json') or []
turmas = carregar_dados_json('turmas.json') or []
matriculas = carregar_dados_json('matriculas.json') or []


# Comando Def para dar mais organização e uma estética mais bonita ao código.
def titulo(txt):
    tam = len(txt) + 6
    print("-" * tam)
    print(f'  {txt}')
    print("-" * tam)


# Comando Def para facilitar a inclusão de um estudante.
def incluir_estudante():
    codigo_estudante = int(input("Digite o código do estudante: "))
    nome_estudante = str(input("Digite o nome do estudante: "))
    cpf_estudante = str(input("Digite o CPF do estudante: "))

    # Adiciona o estudante depois de colher todos os dados pedidos.
    estudante = {"Código": codigo_estudante, "Nome": nome_estudante, "CPF": cpf_estudante}
    print("Aluno adicionado com sucesso!")
    return estudante



# Comando Def para facilitar a inclusão de um professor.
def incluir_professor():
    codigo_professor = int(input("Digite o código do professor: "))
    nome_professor = str(input("Digite o nome do professor: "))
    cpf_professor = str(input("Digite o CPF do professor: "))

    # Adiciona o professor depois de colher todos os dados pedidos.
    professor = {"Código": codigo_professor, "Nome": nome_professor, "CPF": cpf_professor}
    print("Professor adicionado com sucesso!")
    return professor


# Comando Def para facilitar a inclusão de uma disciplina.
def incluir_disciplina():
    codigo_disciplina = int(input("Digite qual o código da disciplina que deseja incluir: "))
    nome_disciplina = str(input("Digite o nome da disciplina que deseja incluir: "))

    # Adiciona a disciplina depois de colher todos os dados pedidos.
    disciplina = {"Código": codigo_disciplina, "Nome": nome_disciplina}
    print("Disciplina adicionada com sucesso!")
    return disciplina


# Comando Def para facilitar a inclusão de uma turma.
def incluir_turma():
    codigo_turma = int(input("Digite qual o código da turma: "))
    codigo_professor = int(input("Digite o código do professor: "))

    # Verifica se o código do professor está cadastrado.
    professor_existe = False
    for professor in professores:
        if professor['Código'] == codigo_professor:
            professor_existe = True
            break
    if not professor_existe:
        print("Código de professor inválido. Por favor, cadastre o professor antes de criar a turma.")
        return None

    codigo_disciplina = int(input("Digite qual o código da disciplina: "))

    # Verifica se o código da disciplina está cadastrado
    disciplina_existe = False
    for disciplina in disciplinas:
        if disciplina['Código'] == codigo_disciplina:
            disciplina_existe = True
            break
    if not disciplina_existe:
        print("Código de disciplina inválido. Por favor, cadastre a disciplina antes de criar a turma.")
        return None

    # Adiciona a turma depois de colher todos os dados pedidos.
    turma = {"Código": codigo_turma, "Professor": codigo_professor, "Disciplina": codigo_disciplina}
    print("Turma adicionada com sucesso!")
    return turma


# Comando Def para facilitar a inclusão de uma matrícula.
def incluir_matriculas():
    codigo_matricula = int(input("Digite qual o código da matrícula que deseja adicionar:"))
    codigo_turma = int(input("Digite qual o código da turma: "))

    # Verifica se o código da turma está cadastrado.
    turma_existe = False
    for turma in turmas:
        if turma['Código'] == codigo_turma:
            turma_existe = True
            break
    if not turma_existe:
        print("Código de turma inválido. Por favor, cadastre a turma antes de criar a turma.")
        return None

    codigo_estudante = int(input("Digite o código do estudante: "))

    # Verifica se o código do estudante está cadastrado.
    estudante_existe = False
    for estudante in estudantes:
        if estudante['Código'] == codigo_estudante:
            estudante_existe = True
            break
    if not estudante_existe:
        print("Código de estudante inválido. Por favor, cadastre o estudante antes de criar a turma.")
        return None

    # Adiciona a matrícula depois de colher todos os dados pedidos.
    matricula = {"Código": codigo_matricula, "Turma": codigo_turma, "Estudante": codigo_estudante}
    print("Matrícula adicionada com sucesso!")
    return matricula



# Opção aqui serve para dar o início na variável para usar no While.
opcao = -1


# While para o sistema permanecer rodando,
while opcao !=0:
    titulo("  MENU PRINCIPAL")
    opcao = int(input(" 1. Estudantes\n 2. Professores\n 3. Disciplinas\n 4. Turmas\n 5. Matrículas\n 0. Sair\n"))
    print("Você digitou ", opcao )


    # If para entrar nas operações de estudantes.
    if opcao == 1:

        # Opcao de estudantes para dar o início na variável para usar no While.
        opcao_estudantes = -1

        # While para manter no menu de operações até que o usuário decida sair.
        while opcao_estudantes != 9:
            titulo("  [ESTUDANTES] Menu de operações ")
            opcao_estudantes = int(input(" 1. Incluir\n 2. Listar\n 3. Atualizar\n 4. Excluir\n 9. Voltar ao menu\n"))
            print("Você digitou ", opcao_estudantes)

            # If para incluir o nome de um estudante.
            if opcao_estudantes == 1:
                novo_estudante = incluir_estudante()
                estudantes.append(novo_estudante)

            # Elif para listar os que já foram incluídos.
            elif opcao_estudantes == 2:

                titulo("Listando Estudantes")

                # If para mostrar que nenhum foi cadastrado se não houver cadastros.
                if not estudantes:
                    print("\nNenhum estudante cadastrado.\n")

                # For para listar quando existir algum cadastrado.
                for estudante in estudantes:
                    print("- ", estudante)

                input("\nPressione ENTER para continuar. ")

            # Elif para atualizar algum nome dentro dos que foram incluídos.
            elif opcao_estudantes == 3:
                titulo("   Menu de atualização de cadastro.")
                codigo_procurado_estudante = int(input("Digite o código do estudante que deseja alterar: "))

                # For para percorrer os elementos da lista e Enumerate para obter o índice "i" e o valor "pessoa".
                for i, pessoa in enumerate(estudantes):
                    if pessoa["Código"] == codigo_procurado_estudante:
                        print("Código encontrado!")
                        atualizacao_de_informacao = int(input("Qual informação deseja alterar?\n 1. Código de estudante.\n 2. Nome do estudante.\n 3. CPF do estudante.\n "))

                        # If para atualizar o código.
                        if atualizacao_de_informacao == 1:
                            print("Código antes da edição:", pessoa["Código"])
                            novo_codigo_de_estudante = int(input("Qual o novo código do estudante?"))
                            estudantes[i]["Código"] = novo_codigo_de_estudante
                            print("Código após a edição:", pessoa["Código"])

                        # Elif para atualizar o nome.
                        elif atualizacao_de_informacao == 2:
                            print("Nome antes da edição:", pessoa["Nome"])
                            estudantes[i]["Nome"] = str(input("Qual o novo nome? "))
                            print("Nome após a edição:", pessoa["Nome"])

                        # Elif para atualizar o CPF.
                        elif atualizacao_de_informacao == 3:
                            print("CPF antes da edição:", pessoa["CPF"])
                            estudantes[i]["CPF"] = input("Qual o novo CPF? ")
                            print("CPF após a edição:", pessoa["CPF"])

                        # Else para informar que digitou uma opção inválida.
                        else:
                            print("Digite uma opção válida.")

                    # Elif para informar que o código informado não foi encontrado.
                    elif pessoa["Código"] != codigo_procurado_estudante:
                        print("Código não encontrado.")


                    titulo("Lista atualizada:")
                    print(estudantes)


            # Elif para excluir algum nome dentro dos que foram incluídos.
            elif opcao_estudantes == 4:
                # If para mostrar que nenhum foi cadastrado se não houver cadastros.
                if not estudantes:
                    print("Nenhum estudante cadastrado.")
                # Else para continuar o processo de excluir.
                else:
                    print(estudantes)
                    excluir_estudante = int(input("Digite o código do aluno que deseja excluir. "))

                    # Verifica se o estudante existe.
                    estudante_existe = False
                    for estudante in estudantes:
                        if estudante['Código'] == excluir_estudante:
                            del estudantes[estudantes.index(estudante)]
                            estudante_existe = True
                            break

                    if estudante_existe:
                        print("Lista atualizada:", estudantes)


                    else:
                        print("Não há nenhum estudante com o código", excluir_estudante, "na lista.")

            # Elif para informar que voltará ao menu principal.
            elif opcao_estudantes == 9:
                print("Voltando ao Menu...")

            # Else para informar ao usuário que digitou uma opção inválida.
            else:
                print("Opção inválida, tente novamente")


    # Elif para entrar nas operações de Professores.
    elif opcao == 2:

        # Opcao de professores para dar o início na variável para usar no While.
        opcao_professores = -1

        # While para manter no menu de operações até que o usuário decida sair.
        while opcao_professores != 9:
            titulo("  [PROFESSORES] Menu de operações ")
            opcao_professores = int(input("1. Incluir\n2. Listar\n3. Atualizar\n4. Excluir\n9. Voltar ao menu\n"))
            print("Você digitou ", opcao_professores)

            # If para incluir o nome de um estudante.
            if opcao_professores == 1:
                novo_professor = incluir_professor()
                professores.append(novo_professor)

            # Elif para listar os que já foram incluídos.
            elif opcao_professores == 2:
                titulo("Listando Professores")

                # If para mostrar que nenhum foi cadastrado se não houver cadastros.
                if not professores:
                    print("\nNenhum professor cadastrado.\n")

                # For para listar quando existir alguma cadastrada.
                for professor in professores:
                    print("- ", professor)

                input("\nPressione ENTER para continuar. ")


            # Elif para atualizar algum nome dentro dos que foram incluídos.
            elif opcao_professores == 3:
                titulo("   Menu de atualização de cadastro.")
                codigo_procurado_professor = int(input("Digite o código do professor que deseja alterar: "))

                # For para percorrer os elementos da lista e Enumerate para obter o índice "i" e o valor "pessoa".
                for i, pessoa in enumerate(professores):
                    if pessoa["Código"] == codigo_procurado_professor:
                        print("Código encontrado!")
                        atualizacao_de_informacao = int(input("Qual informação deseja alterar?\n 1. Código do professor.\n 2. Nome do professor.\n 3. CPF do professor.\n "))

                        # If para atualizar o código.
                        if atualizacao_de_informacao == 1:
                            print("Código antes da edição:", pessoa["Código"])
                            novo_codigo_de_professor = int(input("Qual o novo código do professor?"))
                            professores[i]["Código"] = novo_codigo_de_professor
                            print("Código após a edição:", pessoa["Código"])

                        # If para atualizar o nome.
                        elif atualizacao_de_informacao == 2:
                            print("Nome antes da edição:", pessoa["Nome"])
                            professores[i]["Nome"] = str(input("Qual o novo nome? "))
                            print("Nome após a edição:", pessoa["Nome"])

                        # If para atualizar o CPF.
                        elif atualizacao_de_informacao == 3:
                            print("CPF antes da edição:", pessoa["CPF"])
                            professores[i]["CPF"] = input("Qual o novo CPF? ")
                            print("CPF após a edição:", pessoa["CPF"])
                            break

                        # Else para informar que digitou uma opção inválida.
                        else:
                            print("Digite uma opção válida.")

                    # Elif para informar que o código informado não foi encontrado.
                    elif pessoa["Código"] != codigo_procurado_professor:
                        print("Código não encontrado.")

                    titulo("Lista atualizada:")
                    print(professores)


            # Elif para excluir algum nome dentro dos que foram incluídos.
            elif opcao_professores == 4:
                if not professores:
                    print("Nenhum professor cadastrado.")
                else:
                    print(professores)
                    excluir_professor = int(input("Digite o código do professor que deseja excluir. "))
                    existe = False
                    for professor in professores:
                        if professor['Código'] == excluir_professor:
                            del professores[professores.index(professor)]
                            existe = True
                            break

                    if existe:
                        print("Lista atualizada:", professores)


                    else:
                        print("Não há nenhum professor com o código", excluir_professor, "na lista.")

            # Elif para informar que voltará ao menu principal.
            elif opcao_professores == 9:
                print("Voltando ao Menu...")

            # Else para informar ao usuário que digitou uma opção inválida.
            else:
                print("Opção inválida, tente novamente")


    # Elif para entrar nas operações de Disciplinas.
    elif opcao == 3:

        # Opcao de disciplinas para dar o início na variável para usar no While.
        opcao_disciplinas = -1

        # While para manter no menu de operações até que o usuário decida sair.
        while opcao_disciplinas != 9:
            titulo("  [DISCIPLINAS] Menu de operações ")
            opcao_disciplinas = int(input("1. Incluir\n2. Listar\n3. Atualizar\n4. Excluir\n9. Voltar ao menu\n"))
            print("Você digitou ", opcao_disciplinas)

            # If para incluir o nome de uma disciplina.
            if opcao_disciplinas == 1:
                nome_disciplinas = incluir_disciplina()
                disciplinas.append(nome_disciplinas)

            # Elif para listar os que já foram incluídos.
            elif opcao_disciplinas == 2:
                titulo("Listando Disciplinas")

                # If para mostrar que nenhuma foi cadastrada se não houver cadastros.
                if not disciplinas:
                    print("\nNenhuma disciplina cadastrada.\n")

                # For para listar quando existir algum cadastrado.
                for disciplina in disciplinas:
                    print("- ", disciplina)

                input("\nPressione ENTER para continuar. ")

            # Elif para atualizar algum nome dentro dos que foram incluídos.
            elif opcao_disciplinas == 3:
                titulo("   Menu de atualização de cadastro.")
                codigo_procurado_disciplina = int(input("Digite o código da disciplina que deseja alterar: "))

                # For para percorrer os elementos da lista e Enumerate para obter o índice "i" e o valor "disciplina".
                for i, disciplina in enumerate(disciplinas):
                    if disciplina["Código"] == codigo_procurado_disciplina:
                        print("Código encontrado!")
                        atualizacao_de_informacao = int(input("Qual informação deseja alterar?\n 1. Código da disciplina.\n 2. Nome da disciplina.\n"))

                        # If para atualizar o código.
                        if atualizacao_de_informacao == 1:
                            print("Código antes da edição:", disciplina["Código"])
                            novo_codigo_de_disciplina = int(input("Qual o novo código da disciplina?"))
                            disciplinas[i]["Código"] = novo_codigo_de_disciplina
                            print("Código após a edição:", disciplina["Código"])

                        # If para atualizar o nome.
                        elif atualizacao_de_informacao == 2:
                            print("Nome antes da edição:", disciplina["Nome"])
                            disciplinas[i]["Nome"] = str(input("Qual o novo nome? "))
                            print("Nome após a edição:", disciplina["Nome"])

                        # Else para informar que digitou uma opção inválida.
                        else:
                            print("Digite uma opção válida.")

                    # Elif para informar que o código informado não foi encontrado.
                    elif disciplina["Código"] != codigo_procurado_disciplina:
                        print("Código não encontrado.")

                    titulo("Lista atualizada:")
                    print(disciplinas)

            # Elif para excluir algum nome dentro dos que foram incluídos.
            elif opcao_disciplinas == 4:
                if not disciplinas:
                    print("Nenhuma disciplina cadastrada.")
                else:
                    print(disciplinas)
                    excluir_disciplina = int(input("Digite o código da disciplina que deseja excluir. "))
                    existe = False
                    for disciplina in disciplinas:
                        if disciplina['Código'] == excluir_disciplina:
                            del disciplinas[disciplinas.index(disciplina)]
                            existe = True
                            break

                    if existe:
                        print("Lista atualizada:", disciplinas)


                    else:
                        print("Não há nenhuma pessoa com o código", excluir_disciplina, "na lista.")

            # Elif para informar que voltará ao menu principal.
            elif opcao_disciplinas == 9:
                print("Voltando ao Menu...")

            # Else para informar ao usuário que digitou uma opção inválida.
            else:
                print("Opção inválida, tente novamente")


    # Elif para entrar nas operações de Turmas.
    elif opcao == 4:

        # Opcao de turmas para dar o início na variável para usar no While.
        opcao_turmas = -1

        # While para manter no menu de operações até que o usuário decida sair.
        while opcao_turmas != 9:
            titulo("  [TURMAS] Menu de operações ")
            opcao_turmas = int(input("1. Incluir\n2. Listar\n3. Atualizar\n4. Excluir\n9. Voltar ao menu\n"))
            print("Você digitou ", opcao_turmas)

            # If para incluir o nome de uma turma.
            if opcao_turmas == 1:
                nome_turmas = incluir_turma()
                turmas.append(nome_turmas)

            # Elif para listar os que já foram incluídos.
            elif opcao_turmas == 2:
                titulo("Listando Turmas")

                # If para mostrar que nenhuma foi cadastrada se não houver cadastros.
                if not turmas:
                    print("\nNenhuma turma cadastrada.\n")

                # For para listar quando existir alguma cadastrada.
                for turma in turmas:
                    print("- ", turma)

                input("\nPressione ENTER para continuar. ")

            # Elif para atualizar algum nome dentro dos que foram incluídos.
            elif opcao_turmas == 3:
                titulo("   Menu de atualização de turmas.")
                codigo_procurado_turma = int(input("Digite o código da turma que deseja alterar: "))

                # For para percorrer os elementos da lista e Enumerate para obter o índice "i" e o valor "turma".
                for i, turma in enumerate(turmas):
                    if turma["Código"] == codigo_procurado_turma:
                        print("Código encontrado!")
                        atualizacao_de_informacao = int(input("Qual informação deseja alterar?\n 1. Código da turma.\n 2. Código do professor.\n 3. Código da disciplina.\n "))

                        # If para atualizar o código.
                        if atualizacao_de_informacao == 1:
                            print("Código antes da edição:", turma["Código"])
                            novo_codigo_de_turma = int(input("Qual o novo código da turma?"))
                            turmas[i]["Código"] = novo_codigo_de_turma
                            print("Código após a edição:", turma["Código"])
                            titulo("Lista atualizada:")
                            print(turmas)

                        # Elif para atualizar o professor.
                        elif atualizacao_de_informacao == 2:
                            print("Código do professor antes da edição:", turma["Professor"])
                            novo_codigo_de_professor = int(input("Qual o novo código do professor? "))
                            professor_existe = False
                            for professor in professores:
                                if professor['Código'] == novo_codigo_de_professor:
                                    professor_existe = True
                                    print("Código após a edição:", professor["Código"])
                                    break

                            if professor_existe:
                                turma["Professor"] = novo_codigo_de_professor
                                titulo("Lista atualizada:")
                                print(turmas)

                            else:
                                print("Código do professor inválido. Por favor, cadastre o professor antes de editar as informações da turma.")

                        # Elif para atualizar a disciplina.
                        elif atualizacao_de_informacao == 3:
                            print("Código da disciplina antes da edição:", turma["Disciplina"])
                            novo_codigo_disciplina = int(input("Qual o novo código da disciplina? "))
                            disciplina_existe = False
                            for disciplina in disciplinas:
                                if disciplina['Código'] == novo_codigo_disciplina:
                                    disciplina_existe = True
                                    print("Código após a edição:", disciplina["Código"])
                                    break

                            if disciplina_existe:
                                turma["Disciplina"] = novo_codigo_disciplina
                                titulo("Lista atualizada:")
                                print(turmas)

                            # Else para informar que digitou uma opção inválida.
                            else:
                                print("Código de disciplina inválido. Por favor, cadastre a disciplina antes de editar as informações da turma.")

                    # Elif para informar que o código informado não foi encontrado.
                    elif turma["Código"] != codigo_procurado_turma:
                        print("Código não encontrado.")


            # Elif para excluir algum nome dentro dos que foram incluídos.
            elif opcao_turmas == 4:
                if not turmas:
                    print("Nenhuma turma cadastrada.")
                else:
                    print(turmas)
                    excluir_turma = int(input("Digite o código da turma que deseja excluir. "))
                    turma_existe = False
                    for turma in turmas:
                        if turma['Código'] == excluir_turma:
                            del turmas[turmas.index(turma)]
                            turma_existe = True
                            print("Excluindo turma...")
                            break

                    if turma_existe:
                        titulo("Lista atualizada:")
                        if not turmas:
                            print("\nNenhuma turma cadastrada.\n")
                        else:
                            print(turmas)

                    else:
                        print("Não há nenhuma pessoa com o código", excluir_turma, "na lista.")


            # Elif para informar que voltará ao menu principal.
            elif opcao_turmas == 9:
                print("Voltando ao Menu...")

            # Else para informar ao usuário que digitou uma opção inválida.
            else:
                print("Opção inválida, tente novamente")


    # Elif para entrar nas operações de Matrículas.
    elif opcao == 5:

        # Opcao de matrículas para dar o início na variável para usar no While.
        opcao_matriculas = -1

        # While para manter no menu de operações até que o usuário decida sair.
        while opcao_matriculas != 9:
            titulo("  [MATRÍCULAS] Menu de operações ")
            opcao_matriculas = int(input("1. Incluir\n2. Listar\n3. Atualizar\n4. Excluir\n9. Voltar ao menu\n"))
            print("Você digitou ", opcao_matriculas)

            # If para incluir o nome de uma matrícula.
            if opcao_matriculas == 1:
                nome_matriculas = incluir_matriculas()
                matriculas.append(nome_matriculas)

            # Elif para listar os que já foram incluídos.
            elif opcao_matriculas == 2:
                titulo("Listando Matrículas")

                # If para mostrar que nenhuma foi cadastrada se não houver cadastros.
                if not matriculas:
                    print("\nNenhuma matrícula cadastrada.\n")

                # For para listar quando existir alguma cadastrada.
                for matricula in matriculas:
                    print("- ", matricula)

                input("\nPressione ENTER para continuar. ")

            # Elif para atualizar algum nome dentro dos que foram incluídos.
            elif opcao_matriculas == 3:
                titulo("   Menu de atualização de matrículas.")
                codigo_procurado_matricula = int(input("Digite o código da matrícula que deseja alterar: "))

                for i, matricula in enumerate(matriculas):
                    if matricula['Código'] == codigo_procurado_matricula:
                        print("Código encontrado!")
                        atualizacao_de_informacao = int(input("Qual informação deseja alterar?\n1. Código da matrícula\n2. Código da turma.\n3. Código do estudante.\n"))

                        if atualizacao_de_informacao == 1:
                            print("Código antes da edição:", matricula["Código"])
                            novo_codigo_de_matricula = int(input("Qual o novo código da matrícula?"))
                            matriculas[i]["Código"] = novo_codigo_de_matricula
                            print("Código após a edição:", matricula["Código"])
                            titulo("Lista atualizada:")
                            print(matriculas)

                        elif atualizacao_de_informacao == 2:
                            print("Código antes da edição:", matricula["Turma"])
                            novo_codigo_de_turma = int(input("Qual o novo código da turma?"))
                            turma_existe = False
                            for turma in turmas:
                                if turma['Código'] == novo_codigo_de_turma:
                                    turma_existe = True
                                    print("Código após a edição:", turma["Código"])
                                    matricula["Turma"] = novo_codigo_de_turma
                                    titulo("Lista atualizada:")
                                    print(matriculas)
                                    break

                            if not turma_existe:
                                print("Código de turma inválido. Por favor, cadastre a turma antes de editar as informações da matrícula.")

                        elif atualizacao_de_informacao == 3:
                            print("Código antes da edição:", matricula["Estudante"])
                            novo_codigo_de_estudante = int(input("Qual o novo código do estudante?"))
                            estudante_existe = False
                            for estudante in estudantes:
                                if estudante['Código'] == novo_codigo_de_estudante:
                                    estudante_existe = True
                                    print("Código após a edição:", estudante["Código"])
                                    break

                            if estudante_existe:
                                matricula["Estudante"] = novo_codigo_de_estudante
                                titulo("Lista atualizada:")
                                print(matriculas)

                            else:
                                print("Código de estudante inválido. Por favor, cadastre o estudante antes de editar as informações da matrícula.")


            # Elif para excluir algum nome dentro dos que foram incluídos.
            elif opcao_matriculas == 4:
                if not matriculas:
                    print("Nenhuma matrícula cadastrada.")
                else:
                    print(matriculas)
                    excluir_matricula = int(input("Digite o código da matrícula que deseja excluir. "))
                    matricula_existe = False
                    for matricula in matriculas:
                        if matricula['Código'] == excluir_matricula:
                            del matriculas[matriculas.index(matricula)]
                            matricula_existe = True
                            print("Excluindo matrícula...")
                            break

                    if matricula_existe:
                        titulo("Lista atualizada:")
                        if not matriculas:
                            print("\nNenhuma matrícula cadastrada.\n")
                        else:
                            print(matriculas)

                    else:
                        print("Não há nenhuma matrícula com o código", excluir_matricula, "na lista.")

            elif opcao_matriculas == 9:
                print("Voltando ao Menu...")

            else:
                print("Opção inválida, tente novamente")


    # Elif para informar que está saindo.
    elif opcao == 0:
        # Salvar dados em JSON antes de sair
        salvar_dados_json(estudantes, 'estudantes.json')
        salvar_dados_json(professores, 'professores.json')
        salvar_dados_json(disciplinas, 'disciplinas.json')
        salvar_dados_json(turmas, 'turmas.json')
        salvar_dados_json(matriculas, 'matriculas.json')
        print("Programa encerrado. Até mais!")
        break

    # Else para informar ao usuário que digitou uma opção inválida.
    else:
        print("Opcão inválida, tente novamente.")

