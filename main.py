from threading import Thread
from selenium import webdriver
from sources.cnn import CnnReader
from sources.g1 import G1Reader
from sources.uol import UOLReader
from sources.trending import TrendingReader
from sources.report import NewsReport

# Estrutura inicial do relatório
report = {
    'economy': [],
    'sports': [],
    'entertainment': [],
    'politics': [],
    'trending-topics': [],
}

def run_cnn_reader(report):
    driver = webdriver.Chrome()  
    cnn_reader = CnnReader(driver)
    try:
        cnn_reader.attatch_news(report)
    finally:
        cnn_reader.driver.quit()

def run_g1_reader(report):
    driver = webdriver.Chrome()  
    g1_reader = G1Reader(driver)
    try:
        g1_reader.attatch_news(report)
    finally:
        g1_reader.driver.quit()

def run_uol_reader(report):
    uol_reader = UOLReader()
    try:
        uol_reader.attach_news(report)
    finally:
        uol_reader.quit()
        
def run_trending_reader(report):
    driver = webdriver.Chrome()  
    trending_reader = TrendingReader(driver)
    try:
        trending_reader.attatch_trending(report)
    finally:
        trending_reader.driver.quit()

def main():
    # cnn_thread = Thread(target=run_cnn_reader, args=(report,))
    # g1_thread = Thread(target=run_g1_reader, args=(report,))
    # uol_thread = Thread(target=run_uol_reader, args=(report,))
    # trending_thread = Thread(target=run_trending_reader, args=(report,))

    # cnn_thread.start()
    # g1_thread.start()
    # uol_thread.start()
    # trending_thread.start()

    # cnn_thread.join()
    # g1_thread.join()
    # uol_thread.join()
    # trending_thread.join()
    
    report = {'economy': [{'title': 'Semana do Consumidor: Guia de Compras ajuda na escolha do produto ideal com mais de 450 dicas, listas e testes', 'description': 'Curadoria do g1 ajuda a descomplicar suas compras: de A a Z, busque pelo produto que você deseja.', 'imageUrl': 'https://s2-g1.glbimg.com/wdB67LC0uHSrI6LOYwzWWh31_FY=/540x304/top/smart/https://i.s3.glbimg.com/v1/AUTH_59edd422c0c84a879bd37670ae4f538a/internal_photos/bs/2023/y/h/QfAPG4TeWdISZZ01vZQg/pexels-emirkhan-bal-953864.jpg', 'url': 'https://g1.globo.com/guia/guia-de-compras/semana-do-consumidor-guia-de-compras-ajuda-na-escolha-do-produto-ideal-com-mais-de-450-dicas-listas-e-testes.ghtml'}, {'title': 'Suspensa pela Anac, Voepass é 4ª maior aérea e perdeu espaço após acidente', 'description': 'Companhia fica atrás somente das três "gigantes" que controlam mercado e movimentou 729 mil passageiros no último ano', 'imageUrl': None, 'url': 'http://www.cnnbrasil.com.br/economia/macroeconomia/suspensa-pela-anac-voepass-e-4a-maior-aerea-e-perdeu-espaco-apos-acidente/'}, {'title': 'Trump não descarta possível recessão nos EUA, e Bolsas caem; dólar sobe', 'data': '10/03/2025 14h59', 'description': 'As bolsas de Nova York e também a de São Paulo caem forte nesta segunda-feira após declarações do presidente americano Donald Trump no fim de semana. Ele se recusou, em uma entrevista divulgada neste domingo, a prever se haverá ou não uma recessão nos Estados Unidos este ano.', 'url': 'https://economia.uol.com.br/noticias/redacao/2025/03/10/trump-nao-descarta-possivel-recessao-nos-eua-e-bolsas-caem-dolar-sobe.htm'}], 'sports': [{'title': 'PC de Oliveira discorda de pênalti marcado para o Palmeiras', 'description': 'Flávio Rodrigues de Souza assinalou falta de Arboleda em Vitor Roque', 'imageUrl': 'https://s2-ge.glbimg.com/Ha3DGN-jlC1YQyrKM4e06lFdQoo=/0x0:1920x1080/540x304/smart/filters:max_age(3600)/http://s01.video.glbimg.com/deo/vi/99/82/13408299', 'url': 'https://ge.globo.com/futebol/times/sao-paulo/noticia/2025/03/11/pc-de-oliveira-discorda-de-penalti-marcado-para-o-palmeiras-contato-provocado-pelo-atacante.ghtml'}, {'title': 'Palmeiras enfrenta problemas com datas das finais contra o Corinthians', 'description': 'Federação Paulista de Futebol tomará últimas decisões sobre as finais nesta terça-feira (11)', 'imageUrl': 'https://www.cnnbrasil.com.br/wp-content/uploads/sites/12/2025/03/palmeiras-sao-paulo-allianz-parque-e1741688657770.jpg?w=1220&h=674&crop=1&quality=85', 'url': 'http://www.cnnbrasil.com.br/esportes/futebol/palmeiras/palmeiras-enfrenta-problemas-com-datas-das-finais-contra-o-corinthians/'}, {'title': 'Palmeiras e Corinthians querem comprar briga da FPF por data de final', 'data': '', 'description': '', 'url': 'https://www.uol.com.br/esporte/colunas/danilo-lavieri/2025/03/11/palmeiras-e-corinthians-querem-comprar-briga-da-fpf-por-data-de-final.htm'}], 'entertainment': [{'title': "Tadeu Schmidt interrompe discussão entre Gracyanne e Aline: 'Passaram do ponto'", 'description': 'Sisters continuam embate após o tempo previsto na dinâmica desta segunda-feira (10)', 'imageUrl': 'https://s2-gshow.glbimg.com/sw2N0GLSOVUV_ReInVgdSseSvYg=/540x304/top/smart/https://i.s3.glbimg.com/v1/AUTH_e84042ef78cb4708aeebdf1c68c6cbd6/internal_photos/bs/2025/J/u/4D204ERFGzbNsy8LRNAg/qxsmtkpg-gif-1-.gif', 'url': 'https://gshow.globo.com/realities/bbb/bbb-25/sincerao/noticia/tadeu-schmidt-separa-discussao-entre-gracyanne-barbosa-e-aline-passaram-do-ponto.ghtml'}, {'title': 'Guilherme dispara para Aline no BBB25: “Não consegue escutar as pessoas”', 'description': 'Aliados, brother aconselhou a sister a ouvir mais as outras após o Sincerão de segunda-feira (10)', 'imageUrl': 'https://www.cnnbrasil.com.br/wp-content/uploads/sites/12/2025/03/guilherme-bbb25.png?w=504&h=301&crop=1&quality=85', 'url': 'http://www.cnnbrasil.com.br/entretenimento/bbb/guilherme-dispara-para-aline-no-bbb25-nao-consegue-escutar-as-pessoas/'}, {'title': 'BBB 25 - Enquete UOL - Quem você quer eliminar no Paredão?', 'data': '10/03/2025 00h41', 'description': 'Aline, Thamiris e Vinícius estão no oitavo Paredão da edição. Quem você quer eliminar? Vote na enquete UOL. O mais votado será eliminado na terça-feira (11).', 'url': 'https://www.uol.com.br/splash/bbb/enquetes/2025/03/10/bbb-25---enquete-uol---8-paredao.htm'}], 'politics': [{'title': "Após 'trauma' sobre emendas, Câmara discute 'superpoderes' para líderes partidários sobre presidências de comissões", 'description': 'Minuta de proposta que foi levada às lideranças prevê que líderes indiquem e destituam presidentes. STF agora exige que indicação dos recursos seja aprovada nos colegiados.', 'imageUrl': 'https://s2-g1.glbimg.com/sZ2dfNZ1iq7EWa10wVwlkYY-9_M=/540x304/top/smart/https://i.s3.glbimg.com/v1/AUTH_59edd422c0c84a879bd37670ae4f538a/internal_photos/bs/2024/0/r/eaos1LTaeBgzpDZ0orxA/35685238476-ac5825152a-k.jpg', 'url': 'https://g1.globo.com/politica/noticia/2025/03/11/apos-trauma-sobre-emendas-camara-discute-superpoderes-para-lideres-partidarios-sobre-presidencias-de-comissoes.ghtml'}, {'title': 'Falta de rumo é fazer plano para matar o presidente, diz Marina Silva', 'description': 'Em entrevista, ministra fez menção ao plano "Punhal Verde e Amarelo" que, segundo investigações da Polícia Federal (PF), previa a morte de Lula, Geraldo Alckmin e Alexandre de Moraes', 'imageUrl': 'https://www.cnnbrasil.com.br/wp-content/uploads/sites/12/2025/03/Captura-de-tela-2025-03-11-074337-e1741689902158.png?w=1220&h=674&crop=1&quality=85', 'url': 'http://www.cnnbrasil.com.br/politica/falta-de-rumo-e-fazer-plano-para-matar-o-presidente-diz-marina-silva/'}, {'title': 'Bolsonaro lança marca de capacetes após atos sem o equipamento obrigatório', 'data': '11/03/2025 05h30', 'description': 'O ex-presidente Jair Bolsonaro (PL) cruzou o Brasil fazendo motociatas sem capacete. Hoje, ele ignora o histórico pessoal e lança uma marca do equipamento, obrigatório para motociclistas.', 'url': 'https://noticias.uol.com.br/politica/ultimas-noticias/2025/03/11/bolsonaro-lanca-marca-de-capacetes-apos-atos-sem-o-equipamento-obrigatorio.htm'}], 'trending-topics': [], 'coins': []}
    
    report_generator = NewsReport(report)
    report_generator.generate_pdf()

main()
print(report)