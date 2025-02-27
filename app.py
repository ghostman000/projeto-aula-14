from classes_hotel import *
import flet as ft
from theme import custom_theme, default_headline_style

gerenciador = GerenciadorDeReservas()
gerenciador.criar_quartos()

#---------------------------------------------------------------------#
#                           Página Principal
#---------------------------------------------------------------------#
def main(page: ft.Page):
    page.controls.clear()
    page.theme = custom_theme
    page.title = "Sistema de Reservas"
    layout = ft.Column(
        [
            ft.ElevatedButton(text="Gerenciar Reservas", on_click=lambda e: gerenciar_reservas(page)),
            ft.ElevatedButton(text="Gerenciar Clientes", on_click=lambda e: gerenciar_clientes(page)),
        ],
    )
    container = ft.Container(
        content=ft.Text("Sistema de Reservas", style=default_headline_style, text_align=ft.TextAlign.CENTER),
        alignment=ft.alignment.center  # Alinhando o container no centro da página
    )
    
    quartos_blocos = []
    for quarto in gerenciador.quartos:
        quarto_info = (
            f"Número: {quarto.numero}\n"
            f"Tipo: {quarto.tipo}\n"
            f"Preço: R$ {quarto.preco:.2f}\n"
            f"Status: {quarto.status}"
        )
        quarto_bloco = ft.Container(
            content=ft.Text(quarto_info),
            padding=10,
            border=ft.border.all(1, "black"),  # Borda individual para cada bloco de quarto
            margin=5
        )
        quartos_blocos.append(quarto_bloco)
    coluna = ft.Column(
        controls=quartos_blocos,
        scroll=ft.ScrollMode.AUTO,
        expand=True
    )
    quartos_container = ft.Container(
        content=coluna,
        expand=True
    )
    container2 = ft.Container(
        content=ft.Text("Quartos Disponíveis", style=default_headline_style, text_align=ft.TextAlign.CENTER)
    )    
    
    page.add(
        container,
        layout,
        container2,
        quartos_container
    )

#---------------------------------------------------------------------#
#                     Página Gerenciar Clientes
#---------------------------------------------------------------------#
def gerenciar_clientes(page: ft.Page):
    page.controls.clear()
    
    # Campos de entrada para dados do cliente (usados também para cadastro)
    cliente_id_input = ft.TextField(label="ID do Cliente", autofocus=True)
    cliente_nome_input = ft.TextField(label="Nome do Cliente")
    cliente_telefone_input = ft.TextField(label="Telefone do Cliente")
    cliente_email_input = ft.TextField(label="Email do Cliente")
    
    # Container para o título da página de gerenciamento de clientes
    container1 = ft.Container(
        content=ft.Text("Gerenciar Clientes", style=default_headline_style, text_align=ft.TextAlign.CENTER),
        alignment=ft.alignment.center
    )
    
    # Container para o título da seção de clientes cadastrados
    container_titulo_clientes = ft.Container(
        content=ft.Text("Clientes Cadastrados", style=default_headline_style, text_align=ft.TextAlign.CENTER),
        alignment=ft.alignment.center
    )
    
    # Criação dos blocos individuais para cada cliente cadastrado, agora com botões de editar e excluir
    clientes_blocos = []
    for cliente in gerenciador.clientes:
        # Cria o widget de texto com as informações do cliente
        cliente_info_text = ft.Text(
            f"ID: {cliente.ID_unico}\n"
            f"Nome: {cliente.nome}\n"
            f"Telefone: {cliente.telefone}\n"
            f"Email: {cliente.email}"
        )
        # Botão para editar, passando o cliente atual para a função editar_cliente
        btn_editar_cliente = ft.ElevatedButton(
            text="Editar Cliente", 
            on_click=lambda e, c=cliente: editar_cliente(page, c)
        )
        # Botão para excluir, passando o cliente atual para a função excluir_cliente
        btn_excluir_cliente = ft.ElevatedButton(
            text="Excluir Cliente",
            on_click=lambda e, c=cliente: excluir_cliente(page, c)
        )
        # Agrupa as informações e os botões em uma Row
        cliente_row = ft.Row(
            controls=[cliente_info_text, btn_editar_cliente, btn_excluir_cliente],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN
        )
        cliente_bloco = ft.Container(
            content=cliente_row,
            padding=10,
            border=ft.border.all(1, "black"),  # Borda individual para cada bloco de cliente
            margin=5
        )
        clientes_blocos.append(cliente_bloco)
        
    # Coluna que contém todos os blocos de clientes com rolagem automática
    coluna = ft.Column(
        controls=clientes_blocos,
        scroll=ft.ScrollMode.AUTO,
        expand=True
    )
    
    client_blocks_container = ft.Container(
        content=coluna,
        expand=True
    )
    # Adiciona os controles na página
    page.add(
        container1,
        ft.ElevatedButton(text="Cadastrar Cliente", on_click=lambda e: cadastrar_cliente(page)),
        ft.ElevatedButton(text="Voltar", on_click=lambda e: main(page)),
        container_titulo_clientes,
        client_blocks_container  # Blocos de clientes dentro do container expandido
    )
    
    #---------------------------------------------------------------------#
    #          Função para editar cliente (recebe o cliente a ser editado)
    #---------------------------------------------------------------------#
    def editar_cliente(page: ft.Page, cliente):
        page.controls.clear()
        # Preenche os campos com os dados do cliente selecionado
        cliente_id_input = ft.TextField(label="ID do Cliente", value=str(cliente.ID_unico), disabled=True, autofocus=True)    
        cliente_nome_input = ft.TextField(label="Nome do Cliente", value=cliente.nome)
        cliente_telefone_input = ft.TextField(label="Telefone do Cliente", value=str(cliente.telefone))
        cliente_email_input = ft.TextField(label="Email do Cliente", value=cliente.email)
    
        container = ft.Container(
            content=ft.Text("Editar Cliente", style=default_headline_style, text_align=ft.TextAlign.CENTER),
            alignment=ft.alignment.center
        )
    
        inputs_container = ft.Container(
            content=ft.Column(
               controls=[cliente_id_input, cliente_nome_input, cliente_telefone_input, cliente_email_input],
               spacing=10
            ),
            expand=True
        )
    
        # Função interna para salvar as alterações do cliente
        def salvar_edicao(e):
            cliente.nome = cliente_nome_input.value
            cliente.telefone = int(cliente_telefone_input.value)
            cliente.email = cliente_email_input.value
            page.open(ft.SnackBar(ft.Text("Cliente atualizado com sucesso!", color='white', weight=ft.FontWeight.BOLD), bgcolor="green"))
            gerenciar_clientes(page)
            page.update()
    
        page.add(
            container, 
            inputs_container,
            ft.ElevatedButton(text="Salvar", on_click=salvar_edicao), 
            ft.ElevatedButton(text="Voltar", on_click=lambda e: gerenciar_clientes(page))
        )
        page.update()
    
    #---------------------------------------------------------------------#
    #          Função para excluir cliente
    #---------------------------------------------------------------------#
    def excluir_cliente(page: ft.Page, cliente):
        # Remove o cliente da lista, se existir
        if cliente in gerenciador.clientes:
            gerenciador.clientes.remove(cliente)
            page.open(ft.SnackBar(ft.Text("Cliente excluído com sucesso!", color='white', weight=ft.FontWeight.BOLD), bgcolor="green"))
        gerenciar_clientes(page)
        page.update()
    
    #---------------------------------------------------------------------#
    #          Funções Internas da Página Gerenciar Clientes (sem alterações)
    #---------------------------------------------------------------------#
    def cadastrar_cliente_click(e):
        if not cliente_id_input.value or not cliente_nome_input.value or not cliente_telefone_input.value or not cliente_email_input.value:
            page.open(ft.SnackBar(ft.Text("Preencha todos os campos!", color='white', weight=ft.FontWeight.BOLD), bgcolor="red"))
        elif not cliente_id_input.value.isdigit() or not cliente_telefone_input.value.isdigit():
            page.open(ft.SnackBar(ft.Text("ID e telefone devem ser números!", color='white', weight=ft.FontWeight.BOLD), bgcolor="red"))
        # Verifica se já existe um cliente com o mesmo ID usando a função any() com uma compreensão de gerador
        elif any(cliente.ID_unico == int(cliente_id_input.value) for cliente in gerenciador.clientes):
            page.open(ft.SnackBar(ft.Text("Cliente com este ID já está cadastrado!", color='white', weight=ft.FontWeight.BOLD), bgcolor="red"))                    
        else:
            cliente = Cliente(
                ID_unico=int(cliente_id_input.value),
                nome=cliente_nome_input.value,
                telefone=int(cliente_telefone_input.value),
                email=cliente_email_input.value
            )
            gerenciador.adicionar_cliente(cliente)
            page.open(ft.SnackBar(ft.Text("Cliente cadastrado com sucesso!", color='white', weight=ft.FontWeight.BOLD), bgcolor="green"))
            cliente_id_input.value = ""
            cliente_nome_input.value = ""
            cliente_telefone_input.value = ""
            cliente_email_input.value = ""
            page.update()
        
    def cadastrar_cliente(page: ft.Page):
        page.controls.clear()
        container = ft.Container(
            content=ft.Text("Cadastrar Cliente", style=default_headline_style, text_align=ft.TextAlign.CENTER),
            alignment=ft.alignment.center
        )
        page.add(
            container,
            cliente_id_input,
            cliente_nome_input,
            cliente_telefone_input,
            cliente_email_input,
            ft.ElevatedButton(text="Cadastrar", on_click=lambda e: cadastrar_cliente_click(e)),
            ft.ElevatedButton(text="Voltar", on_click=lambda e: gerenciar_clientes(page))
        )
        page.update()


#---------------------------------------------------------------------#
#                      Página Gerenciar Reservas
#---------------------------------------------------------------------#
def cancelar_reserva(page: ft.Page, reserva):
    # Verifica se a reserva existe na lista e a remove
    if reserva in gerenciador.reservas:
        gerenciador.reservas.remove(reserva)
        # Opcional: atualizar o status do quarto para "Disponível"
        reserva.quarto_reservado.status = "Disponível"
        page.open(ft.SnackBar(ft.Text(f"Reserva de {reserva.cliente.nome} cancelada com sucesso!",color='white', weight=ft.FontWeight.BOLD,),bgcolor="green",))
    else:
        print("Reserva não encontrada!")
    # Atualiza a página para refletir a remoção da reserva
    gerenciar_reservas(page)

def gerenciar_reservas(page: ft.Page):
    page.controls.clear()
    reservas_blocos = []
    
    for reserva in gerenciador.reservas:
        reserva_info_text = ft.Text(
        f"ID: {reserva.cliente.ID_unico}\n"
        f"Cliente: {reserva.cliente.nome}\n"
        f"Quarto: {reserva.quarto_reservado.numero}\n"
        f"Check-in: {reserva.checkin}\n"
        f"Check-out: {reserva.checkout}\n"
        f"Status: {reserva.status}"
        )

        
        # Cria o botão de cancelar e associa a função cancelar_reserva, passando a reserva atual
        btn_cancelar = ft.ElevatedButton(
            text="Cancelar Reserva", 
            on_click=lambda e, r=reserva: cancelar_reserva(page, r)
        )
        
        # Agrupa o texto e o botão em um Row para exibi-los juntos
        reserva_row = ft.Row(
            controls=[reserva_info_text, btn_cancelar],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN
        )
        
        # Container para o bloco de cada reserva
        reserva_bloco = ft.Container(
            content=reserva_row,
            padding=10,
            border=ft.border.all(1, "black"),
            margin=5
        )
        reservas_blocos.append(reserva_bloco)
    
    # Cria a coluna contendo os blocos de reservas com rolagem automática
    coluna = ft.Column(
        controls=reservas_blocos,
        scroll=ft.ScrollMode.AUTO,
        expand=True
    )
    
    container1 = ft.Container(
        content=ft.Text("Gerenciar Reservas", style=default_headline_style, text_align=ft.TextAlign.CENTER),
        alignment=ft.alignment.center
    )
    
    container2 = ft.Container(
        content=ft.Text("Reservas Cadastradas", style=default_headline_style, text_align=ft.TextAlign.CENTER),
        alignment=ft.alignment.center
    )
    
    page.add(
        container1,
        ft.ElevatedButton(text="Fazer Reserva", on_click=lambda e: fazer_reserva(page)),
        ft.ElevatedButton(text="Voltar", on_click=lambda e: main(page)),
        container2,
        coluna
    )
    page.update()
#---------------------------------------------------------------------#
#                  Pagina Fazer Reserva
#---------------------------------------------------------------------#
def fazer_reserva(page: ft.Page):
    page.controls.clear()
    cliente_id_input = ft.TextField(label="ID do cliente", autofocus=True)
    Quarto_input = ft.TextField(label="numero do quarto")
    checkin_input = ft.TextField(label="Check-in")
    checkout_input = ft.TextField(label="Check-out")
    
    
    container = ft.Container(
        content=ft.Text("Fazer Reserva", style=default_headline_style, text_align=ft.TextAlign.CENTER),
        alignment=ft.alignment.center  # Alinhando o container no centro da página
    )
    
    inputs_container = ft.Container(
        content=ft.Column(
            controls=[
                cliente_id_input,
                Quarto_input,
                checkin_input,
                checkout_input
            ],
            spacing=10
        ),
        expand=True        
    )
    
    page.add(
        container,
        inputs_container,
        ft.ElevatedButton(text="Reservar", on_click=lambda e: fazer_reserva_click(e)),
        ft.ElevatedButton(text="Voltar", on_click=lambda e: gerenciar_reservas(page))
    )
    
    page.update()
#---------------------------------------------------------------------#
#                  Funçao interna de pagina fazer reserva
#---------------------------------------------------------------------#    

    def fazer_reserva_click(e):
        if not cliente_id_input.value or not Quarto_input.value or not checkin_input.value or not checkout_input.value: 
            page.open(ft.SnackBar(ft.Text("Preencha todos os campos!", color='white', weight=ft.FontWeight.BOLD,), bgcolor="red",))
        elif not cliente_id_input.value.isdigit():
            page.open(ft.SnackBar(ft.Text("ID do cliente deve ser um número!", color='white', weight=ft.FontWeight.BOLD,), bgcolor="red",))
        elif not Quarto_input.value.isdigit():
            page.open(ft.SnackBar(ft.Text("Número do quarto deve ser um número!", color='white', weight=ft.FontWeight.BOLD,), bgcolor="red",))
        else: 
            
            id = int(cliente_id_input.value)
            quarto = int(Quarto_input.value)
            checkin = checkin_input.value
            checkout = checkout_input.value

            gerenciador.criar_reserva(id, quarto, checkin, checkout)
            
            cliente_id_input.value = ""
            Quarto_input.value = ""
            checkin_input.value = ""
            checkout_input.value = ""
            page.open(ft.SnackBar(ft.Text("Reserva realizada com sucesso!",color='white', weight=ft.FontWeight.BOLD,),bgcolor="green",))
            gerenciar_reservas(page)
            page.update()
#---------------------------------------------------------------------#
#                  Inicialização da Aplicação
#---------------------------------------------------------------------#
ft.app(target=main)
