class data:

    prezzo_attuale = 0.0
    #order = 0.0
    spesa = 11
    spesa_tot = 0.0
    qty = 0.0
    prezzo = 0.0
    prezzo_medio = 0.0
    qty_tot = 0.0
    prezzo_per_qty_tot = 0.0
    counter_failed = 0.0
    counter_while = 0
    counter_buy = 0
    #balance = 0.0
    USDT_free = 0.0
    prossima_qty = 0.0
    incasso= 0.0
    guadagno= 0.0
    guadagno_tot= 0.0
    profitto_non_realizzato = 0.0
    current_state = 0

def reset (classe):
    classe.prezzo_attuale = 0.0
    # order = 0.0
    classe.spesa = 11
    classe.spesa_tot = 0.0
    classe.qty = 0.0
    classe.prezzo = 0.0
    classe.prezzo_medio = 0.0
    classe.qty_tot = 0.0
    classe.prezzo_per_qty_tot = 0.0
    classe.counter_failed = 0.0
    classe.counter_while = 0
    classe.counter_buy = 0
    # balance = 0.0
    classe.USDT_free = 0.0
    classe.prossima_qty = 0.0
    classe.incasso = 0.0
    classe.guadagno = 0.0
    guadagno_tot = 0.0
    classe.profitto_non_realizzato = 0.0
    current_state = 0

def controllo_file (nome_file,classe):
    file = 0
    count = 0

    if os.path.exists(nome_file):
        print("ho trovato il file")
        print(" ")
        file = 1
        classe.current_state = 1
        count = len(open(nome_file).readlines())

    if classe.qty_tot == 0:
        classe.current_state = 0

    else:
        file = 0
        classe.current_state = 0
        count = 0
        print("non ho trovato il file")
        print(" ")

    return file, count

def lettura_file (nome_file, classe, line_num):
    i = 0
    f = open(nome_file, "r")

    while i < line_num:
        label = str(f.readline())

        if label == 'prezzo_attuale\n':
            classe.prezzo_attuale = float(f.readline())
        #elif label == 'order\n':
            #classe.order = float(f.readline())
        elif label == 'spesa\n':
            classe.spesa = float(f.readline())
        elif label == 'spesa_tot\n':
            classe.spesa_tot = float(f.readline())
        elif label == 'qty\n':
            classe.qty = float(f.readline())
        elif label == 'prezzo\n':
            classe.prezzo = float(f.readline())
        elif label == 'prezzo_medio\n':
            classe.prezzo_medio = float(f.readline())
        elif label == 'qty_tot\n':
            classe.qty_tot = float(f.readline())
        elif label == 'prezzo_per_qty_tot\n':
            classe.prezzo_per_qty_tot = float(f.readline())
        elif label == 'counter_failed\n':
            classe.counter_failed = float(f.readline())
        elif label == 'counter_while\n':
            classe.counter_while = float(f.readline())
        elif label == 'counter_buy\n':
            classe.counter_buy = float(f.readline())
        #elif label == 'balance\n':
            #classe.balance = float(f.readline())
        elif label == 'USDT_free\n':
            classe.USDT_free = float(f.readline())
        elif label == 'prossima_qty\n':
            classe.prossima_qty = float(f.readline())
        elif label == 'incasso\n':
            classe.incasso = float(f.readline())
        elif label == 'guadagno\n':
            classe.guadagno = float(f.readline())
        elif label == 'guadagno_tot\n':
            classe.guadagno_tot = float(f.readline())
        elif label == 'profitto_non_realizzato\n':
            classe.profitto_non_realizzato = float(f.readline())
        elif label == 'current_state\n':
            classe.current_state = float(f.readline())
        else:
            print("ERRORE in lettura file")
            print(" ")
        i = i+2

    f.close()

def scrittura_file (nome_file, classe):

    string = ("prezzo_attuale\n" + str(classe.prezzo_attuale) + "\n" +
              #"order\n" + str(classe.order) + "\n" +
              "spesa\n" + str(classe.spesa) + "\n" +
              "spesa_tot\n" + str(classe.spesa_tot) + "\n" +
              "qty\n" + str(classe.qty) + "\n" +
              "prezzo\n" + str(classe.prezzo) + "\n" +
              "prezzo_medio\n" + str(classe.prezzo_medio) + "\n" +
              "qty_tot\n" + str(classe.qty_tot) + "\n" +
              "prezzo_per_qty_tot\n" + str(classe.prezzo_per_qty_tot) + "\n" +
              "counter_failed\n" + str(classe.counter_failed) + "\n" +
              "counter_while\n" + str(classe.counter_while) + "\n" +
              "counter_buy\n" + str(classe.counter_buy) + "\n" +
              #"balance\n" + str(classe.balance) + "\n" +
              "USDT_free\n" + str(classe.USDT_free) + "\n" +
              "prossima_qty\n" + str(classe.prossima_qty) + "\n" +
              "incasso\n" + str(classe.incasso) + "\n" +
              "guadagno\n" + str(classe.guadagno) + "\n" +
              "guadagno_tot\n" + str(classe.guadagno_tot) + "\n" +
              "profitto_non_realizzato\n" + str(classe.profitto_non_realizzato) + "\n" +
              "current_state\n" + str(classe.current_state))

    f = open(nome_file, "w")
    f.write(str(string))
    f.close()
    print("ho scritto il file")
    print(" ")

def primo_acquisto (classe, coin):

    print("-------------------- (RI) AVVIO DEL PROGRAMMA PER ", coin, "  --------------------")
    classe.prezzo_attuale = exchange.fetchTicker(coin)['last']
    order = exchange.createMarketBuyOrder(coin, float(classe.spesa) / float(classe.prezzo_attuale))
    classe.spesa_tot = float((order)['cost'])
    classe.qty = float((order)['amount'])
    classe.prezzo = float((order)['price'])
    classe.prezzo_medio = classe.prezzo
    classe.qty_tot = classe.qty
    classe.prezzo_per_qty_tot = classe.prezzo * classe.qty_tot
    classe.current_state = 1
    print("Il primo acquisto è appena stato effettuato al prezzo di:", classe.prezzo)
    print("La quantità acquistata nel primo ordine è pari a:", classe.qty)
    print("sono stati spesi un numero di USDT pari a:", classe.spesa_tot)
    print(" ")

def BUY (classe, coin, percentuale_BUY, moltiplicatore):

    balance = exchange.fetch_balance()
    classe.USDT_free = balance['free']['USDT']
    classe.prezzo_attuale = exchange.fetchTicker(coin)['last']
    classe.prossima_qty = float(classe.spesa + moltiplicatore * classe.counter_failed) / float(classe.prezzo_attuale)
    print("-------------------- CONTROLLO DI ", coin, " N° ", classe.counter_while, " --------------------")
    print("Prezzo e ora :   ", classe.prezzo_attuale, "    ", time.strftime("%H:%M:%S"))
    print(" ")

    if classe.prezzo_attuale < (classe.prezzo_medio - (classe.prezzo_medio * percentuale_BUY / 100.00)) and (
            classe.USDT_free > float(classe.spesa + moltiplicatore * classe.counter_failed)):
        classe.counter_buy = classe.counter_buy + 1
        print("-------------------- SI è VERIFICATA LA CONDIZIONE DI BUY PER ", coin, ",  N° ", classe.counter_buy,
              "  --------------------")
        order = exchange.createMarketBuyOrder(coin, classe.prossima_qty)
        classe.spesa_ultima = float((order)['cost'])
        classe.spesa_tot = classe.spesa_tot + classe.spesa_ultima
        classe.qty = float((order)['amount'])
        classe.prezzo = float((order)['price'])
        classe.qty_tot = classe.qty_tot + classe.qty
        classe.prezzo_per_qty_tot = classe.prezzo_per_qty_tot + classe.prezzo * classe.qty
        classe.prezzo_medio = (classe.prezzo_per_qty_tot) / classe.qty_tot
        classe.counter_failed = 0
        classe.current_state = 1
        print("prezzo = ", classe.prezzo)
        print("quantità = ", classe.qty)
        print("spesa = ", classe.spesa_ultima)
        print("il prezzo medio di carico di tutti gli acquisti è pari a:", classe.prezzo_medio)
        print("la quantità totale acquistata fino ad ora è pari a:", classe.qty_tot)
        print("sono stati spesi in totale, USDT = ", classe.spesa_tot)
        print(" ")

def SELL (classe, coin, percentuale_SELL):

    if classe.prezzo_attuale > (classe.prezzo_medio + (classe.prezzo_medio * percentuale_SELL / 100)):

        print("-------------------- SI è VERIFICATA LA CONDIZIONE DI SELL PER ", coin, " --------------------")
        order = exchange.createMarketSellOrder(coin, classe.qty_tot)
        classe.incasso = float((order)['cost'])
        classe.guadagno = classe.incasso - classe.spesa_tot
        classe.guadagno_tot = classe.guadagno_tot + classe.guadagno
        print(
            "è stato venduta tutta la quantità di coin acquistata a partire dall'esecuzione del programma, ovvero pari a:",
            classe.qty_tot)
        print("al prezzo di ", (order)['price'])
        print("il guadagno della singola operazione è, USDT = ", classe.guadagno)
        print(" ")
        classe.counter_failed = 0

    else:
        classe.counter_failed = classe.counter_failed + 1

def report (classe, coin, percentuale_BUY, percentuale_SELL, moltiplicatore):

    classe.profitto_non_realizzato = (classe.prezzo_attuale * classe.qty_tot)
    balance = exchange.fetch_balance()
    classe.USDT_free = balance['free']['USDT']
    print("-------------------- REPORT PER ", coin, " --------------------")
    print("*****  il guadagno della singola coin dall'avvio del programma, USDT =    ", classe.guadagno_tot)
    print("*****  il controvalore è in questo momento, USDT =                        ", classe.profitto_non_realizzato)
    print("*****  prezzo medio di carico :                                           ", classe.prezzo_medio)
    print("*****  prossimo BUY al prezzo di :                                        ",
          (classe.prezzo_medio - (classe.prezzo_medio * percentuale_BUY / 100.00)))
    print("*****  prossimo SELL al prezzo di :                                       ",
          (classe.prezzo_medio + (classe.prezzo_medio * percentuale_SELL / 100)))
    print("*****  USDT spesi =                                                       ", classe.spesa_tot)
    print("*****  il prossimo acquisto avrà un importo pari a USDT =                 ",
          float(classe.spesa + moltiplicatore * classe.counter_failed))
    print("*****  budget residuo, USDT =                                             ", classe.USDT_free)
    print(" ")



if __name__ == '__main__':

    import time
    import config
    import ccxt
    import os

    exchange = ccxt.binance({
        'apiKey': config.BINANCE_API_KEY,
        'secret': config.BINANCE_SECRET_KEY,
        'enableRateLimit': True,
    })

    g_percentuale_BUY_1 = 3.0
    g_percentuale_BUY_2 = 3.0

    g_percentuale_SELL_1 = 5.0
    g_percentuale_SELL_2 = 5.0

    g_moltiplicatore_1 = 0.5
    g_moltiplicatore_2 = 0.5

    classe_coin_1 = data()
    classe_coin_2 = data()

    g_coin_1 = 'LUNA/USDT'
    g_coin_2 = 'BNB/USDT'

    g_nome_file_coin_1 = "backup_classe_1.txt"
    g_nome_file_coin_2 = "backup_classe_2.txt"

    g_file_1, g_line_num_1 = controllo_file(g_nome_file_coin_1, classe_coin_1)
    g_file_2, g_line_num_2 = controllo_file(g_nome_file_coin_2, classe_coin_2)

    if g_file_1 == 1:
        lettura_file(g_nome_file_coin_1, classe_coin_1, g_line_num_1)

    if g_file_2 == 1:
        lettura_file(g_nome_file_coin_2, classe_coin_2, g_line_num_2)

    while True:

        status_API = exchange.fetch_status()['status']
        #print(status_API)
        if status_API == 'ok':

            if classe_coin_1.current_state == 0:
                primo_acquisto(classe_coin_1, g_coin_1)
            else:
                BUY(classe_coin_1,g_coin_1,g_percentuale_BUY_1,g_moltiplicatore_1)
                SELL(classe_coin_1, g_coin_1, g_percentuale_SELL_1)

            if classe_coin_2.current_state == 0:
                primo_acquisto(classe_coin_2, g_coin_2)
            else:
                BUY(classe_coin_2, g_coin_2, g_percentuale_BUY_2, g_moltiplicatore_2)
                SELL(classe_coin_2, g_coin_2, g_percentuale_SELL_2)

            report(classe_coin_1, g_coin_1, g_percentuale_BUY_1, g_percentuale_SELL_1, g_moltiplicatore_1)
            report(classe_coin_2, g_coin_2, g_percentuale_BUY_2, g_percentuale_SELL_2, g_moltiplicatore_2)

                #buy_the_deep(classe_coin_1, g_coin_1, g_moltiplicatore_1, g_percentuale_BUY_1,g_percentuale_SELL_1)
                #buy_the_deep(classe_coin_2, g_coin_2, g_moltiplicatore_2 ,g_percentuale_BUY_2,g_percentuale_SELL_2)

            scrittura_file(g_nome_file_coin_1, classe_coin_1)
            scrittura_file(g_nome_file_coin_2, classe_coin_2)

            g_gain = classe_coin_1.guadagno_tot + classe_coin_2.guadagno_tot

            f = open("GAIN.txt", "a")
            f.write(str(g_gain) + "\n")
            f.close()

            print("GUADAGNO COMPLESSIVO SU TUTTE LE CRYPTO =   ", g_gain)
            print(" ")

            if classe_coin_1.current_state == 2:
                os.remove(g_nome_file_coin_1)
                classe_coin_1.current_state = 0
                reset(classe_coin_1)

            if classe_coin_2.current_state == 2:
                os.remove(g_nome_file_coin_2)
                classe_coin_2.current_state = 0
                reset(classe_coin_2)

            time.sleep(600)

        else:
            print("CONNESSIONE CADUTA, RIAVVIARE IL SISTEMA")
            exchange = ccxt.binance({
                'apiKey': config.BINANCE_API_KEY,
                'secret': config.BINANCE_SECRET_KEY,
                'enableRateLimit': True,
            })
            print("HO TENTATO LA RICONNESSIONE")
            print(" ")