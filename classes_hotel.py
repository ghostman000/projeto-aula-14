# Classe que representa um cliente do sistema
class Cliente:
    def __init__(self, ID_unico, nome, telefone, email):
        # Inicializa os atributos do cliente
        self.ID_unico = ID_unico   # Identificador único do cliente
        self.nome = nome           # Nome do cliente
        self.telefone = telefone   # Telefone do cliente
        self.email = email         # E-mail do cliente


# Classe que representa um quarto do hotel
class Quarto:
    def __init__(self, numero, tipo, preco):
        # Inicializa os atributos do quarto
        self.numero = numero       # Número identificador do quarto
        self.tipo = tipo           # Tipo do quarto (ex.: Simples, Duplo, Suíte, Luxuoso)
        self.preco = preco         # Preço do quarto
        self.status = 'Disponível' # Status inicial do quarto (Disponível)


# Classe que representa uma reserva realizada por um cliente
class Reserva:
    def __init__(self, cliente, quarto_reservado, checkin, checkout):
        self.cliente = cliente                   # Cliente que realizou a reserva
        self.quarto_reservado = quarto_reservado # Quarto reservado pelo cliente
        self.checkin = checkin     # Datas de check-in e check-out da reserva
        self.checkout = checkout   # Datas de check-in e check-out da reserva   
        self.status = 'Reservado'  # Status inicial da reserva (Reservado)

# Classe que gerencia clientes, quartos e reservas do sistema
class GerenciadorDeReservas:
    def __init__(self):
        # Inicializa as listas para armazenar clientes, quartos e reservas
        self.clientes = []  # Lista de objetos do tipo Cliente
        self.quartos = []   # Lista de objetos do tipo Quarto
        self.reservas = []  # Lista de objetos do tipo Reserva


    def adicionar_cliente(self, cliente):
        # Adiciona um novo cliente à lista de clientes
        self.clientes.append(cliente)


    def adicionar_quarto(self, quarto):
        # Adiciona um novo quarto à lista de quartos
        self.quartos.append(quarto)

    def criar_quartos(self):
        # Cria automaticamente um conjunto de quartos com tipos e preços predefinidos
        tipos = ['Simples', 'Duplo', 'Suíte', 'Luxuoso']      # Tipos de quartos disponíveis
        precos = [100.0, 150.0, 200.0, 300.0]                    # Preços correspondentes a cada tipo

        # Para cada tipo de quarto, cria 25 quartos
        for i in range(4):        # Itera sobre os 4 tipos de quartos
            for j in range(25):   # Cria 25 quartos para cada tipo (totalizando 100 quartos)
                numero = i * 25 + j + 1      # Gera o número do quarto de forma sequencial (1 a 100)
                tipo = tipos[i]              # Seleciona o tipo do quarto de acordo com o índice
                preco = precos[i]            # Seleciona o preço correspondente ao tipo
                quarto = Quarto(numero=numero, tipo=tipo, preco=preco)  # Cria uma instância de Quarto
                self.adicionar_quarto(quarto)   # Adiciona o quarto criado à lista de quartos

    def criar_reserva(self, cliente_id, quarto_numero, checkin, checkout):
        # Cria uma reserva para um cliente em um quarto específico

        # Verifica se o cliente existe baseado no ID fornecido
        cliente_encontrado = None
        for cli in self.clientes:
            if cliente_id == cli.ID_unico:
                cliente_encontrado = cli
                break
        if not cliente_encontrado:
            return 'Cliente não encontrado'
        
        

        # Verifica se o quarto existe baseado no número fornecido
        quarto_encontrado = None
        for quarto in self.quartos:
            if quarto_numero == quarto.numero:
                quarto_encontrado = quarto
                break
        if not quarto_encontrado:
            return 'Quarto não encontrado'

        # Verifica se o quarto está disponível para reserva
        if quarto_encontrado.status != 'Disponível':
            return 'Quarto não disponível'

        # Cria uma nova reserva associando o cliente e o quarto, e define as datas de check-in e check-out
        nova_reserva = Reserva(cliente_encontrado, quarto_encontrado, checkin, checkout)
        self.reservas.append(nova_reserva)  # Adiciona a nova reserva à lista de reservas

        # Atualiza o status do quarto para indicar que ele está reservado
        quarto_encontrado.status = 'Reservado'

        return 'Reserva criada com sucesso'

    def listar_reservas(self):
        # Retorna uma lista formatada com as informações de todas as reservas realizadas
        reservas_listadas = []
        for reserva in self.reservas:
            reservas_listadas.append(
                f'Cliente: {reserva.cliente.nome}, Quarto: {reserva.quarto_reservado.numero}, ' +
                f'Checkin: {reserva.checkin}, Checkout: {reserva.checkout}, Status: {reserva.status}'
            )
        return reservas_listadas
