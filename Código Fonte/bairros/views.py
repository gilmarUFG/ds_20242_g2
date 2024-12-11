from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Endereco  # Importe a model Endereco
import requests

# Função para consultar o CEP
def consulta_cep(cep):
    response = requests.get(f"http://www.viacep.com.br/ws/{cep}/json/")
    if response.ok:
        return response.json()
    else:
        raise ValueError("CEP inválido")

# View principal
def index(request):
    address = None
    error = None
    if request.method == 'POST':
        cep = request.POST.get('cep')
        try:
            address = consulta_cep(cep)
        except ValueError as e:
            error = str(e)
    return render(request, 'bairro_selecao.html', {'address': address, 'error': error})

# View para salvar o endereço
def salvar_endereco(request):
    if request.method == 'POST':
        cep = request.POST.get('cep')
        logradouro = request.POST.get('logradouro')
        bairro = request.POST.get('bairro')
        numero = request.POST.get('numero')
        complemento = request.POST.get('complemento')
        observacao = request.POST.get('observacao')

        # Cria e salva o novo objeto Endereco
        Endereco.objects.create(
            cep=cep,
            logradouro=logradouro,
            bairro=bairro,
            numero=numero,
            complemento=complemento,
            observacao=observacao
        )

        return HttpResponse("Endereço salvo com sucesso!")  # Redirecionar ou renderizar uma página de sucesso
    
    from django.shortcuts import render
from .models import Endereco

# Dicionário de bairros por região
bairros_goiania = {
    "Norte": [
        "Alice Barbosa", "Antônio Barbosa", "Antônio Carlos Pires", "Asa Branca", "Atalaia", "Caraíbas",
        "Felicidade", "Gentil Meireles", "Goiânia 2", "Granja Cruzeiro do Sul", "Guarema", "Hugo de Moraes",
        "Humaitá", "Itanhangá", "Vila Itatiaia", "Itamaracá", "Setor Jaó", "Jardim Balneário Meia Ponte",
        "Jardim Bom Jesus", "Jardim Diamantina", "Jardim Gramado", "Jardim Guanabara", "Jardim Guanabara II",
        "Jardim Guanabara III", "Jardim Ipê", "Vila Jardim Pompéia", "Jardim Santa Cecília", "João Paulo II",
        "José Viandeli", "Licardino Ney", "Mansões do Campus", "Mansões Goianas", "Maria Dilce", "Maria Lourença",
        "Maria Rosa", "Morada do Bosque", "Morada do Ipê", "Morumbi", "Morada dos Sonhos", "Nossa Morada",
        "Orlando de Morais", "Panorama Parque", "Parque Balneário", "Parque das Flores", "Parque das Nações",
        "Parque dos Cisnes", "Perim", "Pindorama", "Portal da Mata", "Progresso", "Residencial Balneário",
        "Residencial das Acácias", "Residencial dos Ipês", "Residencial Guanabara", "Residencial Itália",
        "Santa Genoveva", "São Geraldo", "Vila Jardim São Judas Tadeu", "Sevene", "Shangri-lá",
        "Setor Urias Magalhães", "Vale da Serra", "Residencial Vale dos Sonhos", "Residencial Vale dos Sonhos I",
        "Vila Clemente", "Vila Cristina", "Vila dos Oficiais", "Vila Industrial Pedro Abraão", "Vila Militar",
        "Vila Nossa Senhora Aparecida", "Vila Roriz", "Vila Santa Cruz", "Village Atalaia"
    ],
    "Centro Oeste": [
        "Setor Aeroporto", "Aeroviário", "Setor Campinas", "Castelo Branco", "Setor Central", "Setor Centro Oeste",
        "Cidade Jardim", "Setor Coimbra", "Setor Criméia Leste", "Setor Criméia Oeste", "Elísios Campos",
        "Esplanada do Anicuns", "Setor dos Funcionários", "Guadalajara", "Industrial Mooca", "Jardim Ana Flávia",
        "Jardim Xavier", "Setor Marechal Rondon", "Morada Nova", "Morais", "Setor Negrão de Lima",
        "Nossa Senhora de Fátima", "Nova Vila", "Setor Norte Ferroviário", "Operário", "Padre Pelágio",
        "Parque Industrial de Goiânia", "Rodoviário", "Romildo F. R. Amaral", "Setor Santos Dumont", "Setor São Jose",
        "Setor Sul", "Tocafundo", "Setor Leste Universitário", "Vila Abajá", "Vila Adélia", "Vila Aguiar",
        "Vila Aurora", "Vila Bethel", "Vila Boa Sorte", "Vila Canaa", "Vila Colemar Natal e Silva", "Vila Fernandes",
        "Vila Froes", "Vila Irany", "Vila Isaura", "Vila Jacaré", "Vila Jaraguá", "Vila Megale", "Vila Monticelli",
        "Vila Mooca", "Setor Leste Vila Nova", "Vila Nova Canaã", "Vila Ofugi", "Vila Oswaldo Rosa", "Vila Paraíso",
        "Vila Perdiz", "Vila Santa Helena", "Vila Santa Isabel", "Vila Santa Rita", "Vila Santa Tereza",
        "Vila Santana", "Vila Santo Antônio", "Vila São Francisco", "Vila São José", "Vila São Luiz",
        "Vila Vera Cruz", "Vila Viana", "Vila Viandelli", "Yara", "Bertim Belchior"
    ],
    "Noroeste": [
        "Alto do Vale", "Anglo", "da Vitória", "Barravento", "Boa Vista", "Residencial Brisas da Mata",
        "Setor Candida de Morais", "Chácaras Maria Dilce", "Conjunto Primavera", "Empresarial", "Setor Estrela D'Alva",
        "Vila Finsocial", "Floresta", "Fonte das Águas", "Green Park", "Jardim Belvedere", "Jardim Camargo",
        "Jardim Colorado", "Jardim Curitiba", "Jardim das Hortências", "Jardim das Rosas", "Jardim Fonte Nova",
        "Jardim Helou", "Jardim Lago Azul", "Jardim Liberdade", "Jardim Nova Esperanca", "Jardim Vista Bela",
        "Juscelino Kubitschek", "Malibu", "Mansões Paraíso", "Mansões Rosas de Ouro", "Marabá", "Setor Morada do Sol",
        "Noroeste", "Setor Novo Planalto", "Parque Aeronáutico Antônio Sebba Filho", "Parque Maracanã", "Parque Santa Rita",
        "Privê Norte", "Residencial Recanto do Bosque", "Setor Parque Tremendão", "Paulo Pacheco", "Recreio Estrela D'Alva",
        "Recreio Panorama", "Residencial Fortaleza", "Residencial Maringá", "Residencial Mirante", "São Carlos",
        "São Domingos", "Setor Estrela Dalva", "São Joaquim", "Senador Albino Boaventura", "Solange Parque",
        "Solange Parque I", "Terra Nova", "Vila Mutirão", "Vila Mutirão I"
    ],
    "Sul": [
        "Alto da Glória", "Areião", "Areião II", "Setor Bela Vista", "Setor Bueno", "Jardim América",
        "Jardim das Esmeraldas", "Jardim Goiás", "Jardim Santo Antônio", "Jardim Vitória", "Setor Marista",
        "Nova Suíça", "Setor Oeste", "Parque Amazônia", "Setor Pedro Ludovico", "Serrinha", "Setor dos Afonsos",
        "Vila Americano do Brasil", "Vila Divino Pai Eterno", "Vila Maria Isabel", "Vila Maria José", "Vila Redenção",
        "Vila Santa Efigênia", "Vila São João", "Vila São Tomaz", "Vila Teófilo Neto"
    ],
    "Oeste": [
        "14 Bis", "Alto Boa Vista", "Ana Moraes", "Anicuns", "Araguaia Park", "Bairro das Nações", "Barra da Tijuca",
        "Beatriz Nascimento", "Bosque dos Buritis", "Buena Vista", "Capuava", "Capuava Residencial Privê", "Carla Cristina",
        "Carolina Parque", "Celina Parque", "Chácara Anhanguera", "Chácara Buritis", "Chácara Maringá", "Chácara Santa Rita",
        "Chácara São José", "Cidade Verde", "Condomínio do Lago", "Conjunto Anhanguera", "Conjunto Vera Cruz",
        "Coronel Álvaro Alves Júnior", "Costa Verde", "Della Pena", "Dezopi", "Dom Rafael", "Goiá", "Goiá 2", "Goiá 3",
        "Goiá 4", "Residencial Goiânia Viva", "Goyaz Park", "Ipiranga", "Jardim Aritana", "Jardim Bonanza", "Jardim Botânico",
        "Jardim Clarissa", "Jardim Corte Real", "Jardim das Oliveiras", "Jardim das Rosas", "Jardim Imperial",
        "Jardim Leblon", "Jardim Marques de Abreu", "Jardim Mirabel", "Jardim Novo Petrópolis", "Jardim Real",
        "Jardim São José", "Jardins do Cerrado", "João Bueno", "Vila João Vaz", "Junqueira", "Lorena Parque",
        "Lírios do Campo", "London Park", "Luana Park", "Maysa", "Monte Pascoal", "Jardim Mundo Novo", "Nova Aurora",
        "Nunes de Morais", "Jardim Petrópolis", "Park Solar", "Parque Bom Jesus", "Parque Buriti", "Parque Eldorado Oeste",
        "Parque Industrial João Braz", "Parque Industrial Paulista", "Parque Mendanha", "Parque Oeste", "Parque Paraíso",
        "Pilar dos Sonhos", "Ponta Negra", "Portal Anhanguera", "Quinta da Boa Vista", "Residencial Recanto das Garças",
        "Recreio São Joaquim", "Residencial Mendanha", "Residencial Noroeste", "Residencial Petropolis", "Residencial Portinari",
        "Residencial Primavera", "Residencial Real", "Residencial Santa Maria", "Rio Branco", "San Marino", "São Bernardo",
        "São Francisco", "São Joaquim", "São Marcos", "Santa Rita", "Santos Dumont", "Serra Azul", "Solange Parque",
        "Solange Parque I", "Solar Ville", "Tempo Novo", "Tuzimoto", "Tropical Verde", "Tropical Ville", "Vila Planalto",
        "Vila Santa Efigênia", "Vila São Joaquim", "Vila Taquaral"
    ],
    "Leste": [
        "Água Branca", "Residencial Aldeia do Vale", "Alphaville Flamboyant", "Arco Verde", "Aruanã", "Aruanã Park",
        "Bairro Feliz", "Belo Horizonte", "Brisas do Cerrado", "Carlos de Freitas", "Cléa Borges", "Conjunto Anhanguera",
        "Costa Paranhos", "Chácara Botafogo", "Chácara do Governador", "Colônia Santa Marta", "Conjunto Caiçara",
        "Conjunto Fabiana", "Conjunto Palmares", "Conjunto Riviera", "Goiânia Golfe Clube", "Grande Retiro",
        "Housing Flamboyant", "Irisville", "Jardim Abaporu", "Jardim Atenas", "Jardim Bela Vista", "Jardim Brasil",
        "Jardim Califórnia", "Jardim Califórnia Industrial", "Jardim Conquista", "Jardim da Luz", "Jardim das Aroeiras",
        "Jardim Dom Fernando", "Jardim Lajeado", "Jardim Maria Helena", "Jardim Mariliza", "Jardim Novo Mundo",
        "Jardim Paris", "Jardim Santa Cecília", "Jardim Valência", "Jardim Verona", "Jardim Vitória", "Jardins Milão",
        "Jardins Munique", "Lucy Pinheiro", "Mansões Bernardo Sayão", "Mar del Plata", "Monte Verde", "Park Lozandes",
        "Parque Acalanto", "Parque Atheneu", "Parque das Amendoeiras", "Parque das Laranjeiras", "Parque Flamboyant",
        "Parque Santa Cruz", "Parque Santa Maria", "Paulo Estrela", "Portal do Sol", "Portal do Sol II", "Portal Petrópolis",
        "Privê dos Girassóis", "Setor Recanto das Minas Gerais", "Recanto dos Buritis", "Residencial Havaí", "Residencial Olinda",
        "Residencial Ouro Preto", "Residencial Português", "Rio Jordão", "Santa Bárbara", "Santo Hilário", "São Francisco de Assis",
        "São Leopoldo", "São Silvestre", "Senador Paranhos", "Serra Park", "Sonho Dourado", "Sonho Verde", "Tupinambá dos Reis",
        "Vale das Brisas", "Vale do Araguaia", "Vila Alto da Glória", "Vila Bandeirantes", "Vila Concórdia", "Vila Legionárias",
        "Vila Maria Luíza", "Vila Martins", "Vila Matilde", "Vila Morais", "Vila Pedroso", "Vila Romana", "Ville de France"
    ],
    "Sudoeste": [
        "Alphaville Residencial", "Alto Oriente", "Amin Camargo", "Ana Clara", "Andréia", "Parque Anhanguera",
        "Aquários", "Atibaia", "Baliza", "Bonanza", "Bosque Sumaré", "Brasil Central", "Cachoeira Dourada",
        "Campos Dourados", "Celina Park", "Center Ville", "Conjunto das Esmeraldas", "Condomínio das Esmeraldas",
        "Cristina", "Dona Gê", "Residencial Eldorado", "Eli Forte", "Faicalville", "Forteville", "Setor Garavelo",
        "Grajaú", "Residencial Granville", "Jardim Alvaphille", "Jardim Atlântico", "Jardim Ana Lúcia", "Jardim Caravelas",
        "Jardim Eli Forte", "Jardim Europa", "Jardim Florença", "Jardim Gardênia", "Jardim Ipanema", "Jardim Itaipú",
        "Jardim Madri", "Jardim Planalto", "Jardim Presidente", "Jardim Sônia Maria", "Jardim Tancredo Neves",
        "Jardim Vila Boa", "Jardins Lisboa", "Linda Vista", "Madre Germana 2", "Maria Celeste", "Marlene",
        "Moinho dos Ventos", "Monte Carlo", "Setor Novo Horizonte", "Orientville", "Parque Anhanguera",
        "Parque Oeste Industrial", "Parque Santa Rita", "Porto Seguro", "Privê Atlântico", "Privê Ilhas do Caribe",
        "Real Conquista", "Recanto das Emas", "Recreio do Funcionário Público", "Residencial Barcelona",
        "Residencial Canadá", "Residencial Eldorado", "Residencial Escócia", "Residencial Espanha", "Residencial Fidélis",
        "Residencial Flamingo", "Residencial Flórida", "Residencial Itaipú", "Residencial Kátia", "Residencial Manhattan",
        "Residencial Sevilha", "Residencial Talismã", "Residencial Valência", "Rio Formoso", "Rio Verde",
        "Residencial Santa Fé I", "Santa Rita", "Salinos", "Setor dos Dourados", "Solar Bougainville",
        "Solar Santa Rita", "Setor Sudoeste", "Três Marias", "Ulisses Guimarães", "Setor União", "Vereda dos Buritis",
        "Vila Adélia", "Vila Alpes", "Vila Alvorada", "Vila Anchieta", "Vila Bela", "Vila Luciana", "Vila Lucy",
        "Vila Mauá", "Vila Rosa", "Vila Rezende", "Vila Santa Rita", "Vila São Paulo", "Village Green Park",
        "Village Santa Rita", "Village Veneza"
    ]
}

def enderecos_por_regiao(request):
    # Obter todos os endereços salvos
    enderecos = Endereco.objects.all()

    # Criar um dicionário para armazenar os endereços por região
    enderecos_por_regiao = {regiao: [] for regiao in bairros_goiania.keys()}

    # Organizar os endereços por região
    for endereco in enderecos:
        for regiao, bairros in bairros_goiania.items():
            if endereco.bairro in bairros:
                enderecos_por_regiao[regiao].append(endereco)
                break  # Para evitar que o mesmo endereço seja adicionado a mais de uma região

    return render(request, 'enderecos_por_regiao.html', {'enderecos_por_regiao': enderecos_por_regiao})