
#criar uma interface com o Tkinter e, se quiser estéticamente melhor, criar com Custom 

import os
from datetime import datetime

equipe = []

def adicionar_membro():
    nome = input("Nome do membro: ")
    cargo = input("Cargo: ")

    membro = {
        "nome": nome,
        "cargo": cargo,
        "tarefas": []
    }

    equipe.append(membro)
    print("✅ Membro adicionado!")


def remover_membro():
    nome = input("Nome do membro para remover: ")

    for membro in equipe:
        if membro["nome"] == nome:
            equipe.remove(membro)
            print("❌ Membro removido!")
            return

    print("Membro não encontrado.")


def editar_cargo():
    nome = input("Nome do membro: ")

    for membro in equipe:
        if membro["nome"] == nome:
            novo_cargo = input("Novo cargo: ")
            membro["cargo"] = novo_cargo
            print("✏️ Cargo atualizado!")
            return

    print("Membro não encontrado.")


def atribuir_tarefa():
    nome = input("Nome do membro: ")

    for membro in equipe:
        if membro["nome"] == nome:

            tarefa_nome = input("Nome da tarefa: ")

            prazo_str = input("Prazo da tarefa (dd/mm/aaaa): ")

            print("Prioridade:")
            print("1 - Alta")
            print("2 - Média")
            print("3 - Baixa")

            p = input("Escolha: ")

            if p == "1":
                prioridade = "Alta"
            elif p == "2":
                prioridade = "Média"
            else:
                prioridade = "Baixa"

            try:
                prazo = datetime.strptime(prazo_str, "%d/%m/%Y")
            except:
                print("Formato de data inválido!")
                return

            tarefa = {
                "nome": tarefa_nome,
                "prazo": prazo,
                "status": "pendente",
                "prioridade": prioridade
            }   

            membro["tarefas"].append(tarefa)
            print("📋 Tarefa atribuída!")
            return

    print("Membro não encontrado.")

def alterar_status():
    nome = input("Nome do membro: ")

    for membro in equipe:
        if membro["nome"] == nome:

            if not membro["tarefas"]:
                print("Esse membro não possui tarefas.")
                return

            print("\nTarefas:")

            for i, t in enumerate(membro["tarefas"], start=1):
                print(f"{i} - {t['nome']} ({t['status']})")

            indice = int(input("Escolha o número da tarefa: ")) - 1

            print("\nStatus disponíveis:")
            print("1 - pendente")
            print("2 - fazendo")
            print("3 - concluída")

            escolha = input("Novo status: ")

            if escolha == "1":
                membro["tarefas"][indice]["status"] = "pendente"
            elif escolha == "2":
                membro["tarefas"][indice]["status"] = "fazendo"
            elif escolha == "3":
                membro["tarefas"][indice]["status"] = "concluída"

            print("📊 Status atualizado!")
            return

    print("Membro não encontrado.")


def listar_equipe():

    print("\n===== EQUIPE =====")

    if not equipe:
        print("Nenhum membro cadastrado.")
        return

    hoje = datetime.now()

    for membro in equipe:

        print(f"\n👤 Nome: {membro['nome']}")
        print(f"💼 Cargo: {membro['cargo']}")

        if not membro["tarefas"]:
            print("Sem tarefas.")
        else:
            print("📋 Tarefas:")

            for t in membro["tarefas"]:

                prazo = t["prazo"]
                dias_restantes = (prazo - hoje).days

                if dias_restantes < 0:
                    situacao = "⚠️ ATRASADA"
                else:
                    situacao = f"{dias_restantes} dias restantes"

                print(
                    f"- {t['nome']} | Prazo: {prazo.strftime('%d/%m/%Y')} | "
                    f"Status: {t['status']} | {situacao}"
                )

                print(f"Prioridade: {t['prioridade']}")


def dashboard():

    total = 0
    concluidas = 0
    pendentes = 0
    atrasadas = 0

    hoje = datetime.now()

    for membro in equipe:
        for t in membro["tarefas"]:

            total += 1

            if t["status"] == "concluída":
                concluidas += 1
            else:
                pendentes += 1

            if t["prazo"] < hoje and t["status"] != "concluída":
                atrasadas += 1

    print("\n📊 DASHBOARD DO PROJETO")
    print("Total de tarefas:", total)
    print("Concluídas:", concluidas)
    print("Pendentes:", pendentes)
    print("Atrasadas:", atrasadas)


while True:

    print("=== GERENCIADOR DE PROJETOS ===\n")

    print("MENU")
    print("1 - Adicionar membro")
    print("2 - Remover membro")
    print("3 - Editar cargo")
    print("4 - Atribuir tarefa")
    print("5 - Alterar status da tarefa")
    print("6 - Listar equipe")
    print("7 - Dashboard")
    print("0 - Sair")

    opcao = input("\nEscolha uma opção: ")

    if opcao == "1":
        adicionar_membro()

    elif opcao == "2":
        remover_membro()

    elif opcao == "3":
        editar_cargo()

    elif opcao == "4":
        atribuir_tarefa()

    elif opcao == "5":
        alterar_status()

    elif opcao == "6":
        listar_equipe()

    elif opcao == "7":
        dashboard()

    elif opcao == "0":
        print("Encerrando sistema...")
        break

    else:
        print("Opção inválida!")