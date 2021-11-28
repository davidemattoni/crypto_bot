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

def controllo_file (nome_file,variabili):
    file = 0
    count = 0

    if os.path.exists(nome_file):
        print("ho trovato il file")
        file = 1
        variabili.current_state = 1
        count = len(open(nome_file).readlines())

    if variabili.qty_tot == 0:
        variabili.current_state = 0

    else:
        file = 0
        variabili.current_state = 0
        count = 0
        print("non ho trovato il file")

    return file, count

def lettura_file (nome_file, variabili, line_num):
    i = 0
    f = open(nome_file, "r")

    while i < line_num:
        label = str(f.readline())

        if label == 'prezzo_attuale\n':
            variabili.prezzo_attuale = float(f.readline())
        #elif label == 'order\n':
            #variabili.order = float(f.readline())
        elif label == 'spesa\n':
            variabili.spesa = float(f.readline())
        elif label == 'spesa_tot\n':
            variabili.spesa_tot = float(f.readline())
        elif label == 'qty\n':
            variabili.qty = float(f.readline())
        elif label == 'prezzo\n':
            variabili.prezzo = float(f.readline())
        elif label == 'prezzo_medio\n':
            variabili.prezzo_medio = float(f.readline())
        elif label == 'qty_tot\n':
            variabili.qty_tot = float(f.readline())
        elif label == 'prezzo_per_qty_tot\n':
            variabili.prezzo_per_qty_tot = float(f.readline())
        elif label == 'counter_failed\n':
            variabili.counter_failed = float(f.readline())
        elif label == 'counter_while\n':
            variabili.counter_while = float(f.readline())
        elif label == 'counter_buy\n':
            variabili.counter_buy = float(f.readline())
        #elif label == 'balance\n':
            #variabili.balance = float(f.readline())
        elif label == 'USDT_free\n':
            variabili.USDT_free = float(f.readline())
        elif label == 'prossima_qty\n':
            variabili.prossima_qty = float(f.readline())
        elif label == 'incasso\n':
            variabili.incasso = float(f.readline())
        elif label == 'guadagno\n':
            variabili.guadagno = float(f.readline())
        elif label == 'guadagno_tot\n':
            variabili.guadagno_tot = float(f.readline())
        elif label == 'profitto_non_realizzato\n':
            variabili.profitto_non_realizzato = float(f.readline())
        elif label == 'current_state\n':
            variabili.current_state = float(f.readline())
        else:
            print("ERRORE in lettura file")
        i = i+2

    f.close()

def scrittura_file (nome_file, variabili):

    string = ("prezzo_attuale\n" + str(variabili.prezzo_attuale) + "\n" +
              #"order\n" + str(variabili.order) + "\n" +
              "spesa\n" + str(variabili.spesa) + "\n" +
              "spesa_tot\n" + str(variabili.spesa_tot) + "\n" +
              "qty\n" + str(variabili.qty) + "\n" +
              "prezzo\n" + str(variabili.prezzo) + "\n" +
              "prezzo_medio\n" + str(variabili.prezzo_medio) + "\n" +
              "qty_tot\n" + str(variabili.qty_tot) + "\n" +
              "prezzo_per_qty_tot\n" + str(variabili.prezzo_per_qty_tot) + "\n" +
              "counter_failed\n" + str(variabili.counter_failed) + "\n" +
              "counter_while\n" + str(variabili.counter_while) + "\n" +
              "counter_buy\n" + str(variabili.counter_buy) + "\n" +
              #"balance\n" + str(variabili.balance) + "\n" +
              "USDT_free\n" + str(variabili.USDT_free) + "\n" +
              "prossima_qty\n" + str(variabili.prossima_qty) + "\n" +
              "incasso\n" + str(variabili.incasso) + "\n" +
              "guadagno\n" + str(variabili.guadagno) + "\n" +
              "guadagno_tot\n" + str(variabili.guadagno_tot) + "\n" +
              "profitto_non_realizzato\n" + str(variabili.profitto_non_realizzato) + "\n" +
              "current_state\n" + str(variabili.current_state))

    f = open(nome_file, "w")
    f.write(str(string))
    f.close()
    print("ho scritto il file")

def buy_the_deep (variabili, coin,moltiplicatore, percentuale_BUY, percentuale_SELL):

    if variabili.current_state == 0:

        print("-------------------- (RI) AVVIO DEL PROGRAMMA PER ", coin, "  --------------------")
        variabili.prezzo_attuale = exchange.fetchTicker(coin)['last']
        order = exchange.createMarketBuyOrder(coin, float(variabili.spesa) / float(variabili.prezzo_attuale))
        variabili.spesa_tot = float((order)['cost'])
        variabili.qty = float((order)['amount'])
        variabili.prezzo = float((order)['price'])
        variabili.prezzo_medio = variabili.prezzo
        variabili.qty_tot = variabili.qty
        variabili.prezzo_per_qty_tot = variabili.prezzo * variabili.qty_tot
        variabili.current_state = 1
        print("Il primo acquisto è appena stato effettuato al prezzo di:", variabili.prezzo)
        print("La quantità acquistata nel primo ordine è pari a:", variabili.qty)
        print("sono stati spesi un numero di USDT pari a:", variabili.spesa_tot)
        print(" ")
        variabili.counter_failed = 0.0
        variabili.counter_while = 0
        variabili.counter_buy = 0
        variabili.guadagno_tot = 0.0


    else:

        balance = exchange.fetch_balance()
        variabili.USDT_free = balance['free']['USDT']
        variabili.prezzo_attuale = exchange.fetchTicker(coin)['last']
        variabili.prossima_qty = float(variabili.spesa + variabili.counter_failed) / float(variabili.prezzo_attuale)
        variabili.counter_while = variabili.counter_while + 1
        print("-------------------- CONTROLLO DI ", coin, " N° ", variabili.counter_while, " --------------------")
        print("Prezzo e ora :   ", variabili.prezzo_attuale, "    ", time.strftime("%H:%M:%S"))
        print(" ")

        if variabili.prezzo_attuale < (variabili.prezzo_medio - (variabili.prezzo_medio * percentuale_BUY / 100.00)) and (
                variabili.USDT_free > float(variabili.spesa + moltiplicatore * variabili.counter_failed)):
            variabili.counter_buy = variabili.counter_buy + 1
            print("-------------------- SI è VERIFICATA LA CONDIZIONE DI BUY PER ", coin, ",  N° ", variabili.counter_buy,
                  "  --------------------")
            order = exchange.createMarketBuyOrder(coin, variabili.prossima_qty)
            variabili.spesa_ultima = float((order)['cost'])
            variabili.spesa_tot = variabili.spesa_tot + variabili.spesa_ultima
            variabili.qty = float((order)['amount'])
            variabili.prezzo = float((order)['price'])
            variabili.qty_tot = variabili.qty_tot + variabili.qty
            variabili.prezzo_per_qty_tot = variabili.prezzo_per_qty_tot + variabili.prezzo * variabili.qty
            variabili.prezzo_medio = (variabili.prezzo_per_qty_tot) / variabili.qty_tot
            variabili.counter_failed = 0.0
            print("prezzo = ", variabili.prezzo)
            print("quantità = ", variabili.qty)
            print("spesa = ", variabili.spesa_ultima)
            print("il prezzo medio di carico di tutti gli acquisti è pari a:", variabili.prezzo_medio)
            print("la quantità totale acquistata fino ad ora è pari a:", variabili.qty_tot)
            print("sono stati spesi in totale, USDT = ", variabili.spesa_tot)
            print(" ")

        elif variabili.prezzo_attuale > (variabili.prezzo_medio + (variabili.prezzo_medio * percentuale_SELL / 100)):
            print("-------------------- SI è VERIFICATA LA CONDIZIONE DI SELL PER ", coin, " --------------------")
            order = exchange.createMarketSellOrder(coin, variabili.qty_tot)
            variabili.incasso = float((order)['cost'])
            variabili.guadagno = variabili.incasso - variabili.spesa_tot
            variabili.guadagno_tot = variabili.guadagno_tot + variabili.guadagno
            print(
                "è stato venduta tutta la quantità di coin acquistata a partire dall'esecuzione del programma, ovvero pari a:",
                variabili.qty_tot)
            print("al prezzo di ", (order)['price'])
            print("il guadagno della singola operazione è, USDT = ", variabili.guadagno)
            variabili.qty_tot = 0.0
            variabili.counter_failed = 0.0
            variabili.counter_buy = 0
            variabili.spesa_tot = 0.0
            variabili.current_state = 2
            variabili.prezzo_medio = 0.0
            print(" ")

        else:
            variabili.counter_failed = variabili.counter_failed + 1

        variabili.profitto_non_realizzato = (variabili.prezzo_attuale * variabili.qty_tot)
        balance = exchange.fetch_balance()
        variabili.USDT_free = balance['free']['USDT']

        if (variabili.counter_failed == 0):
            print("-------------------- REPORT PER ", coin, " --------------------")
            print("*****  il guadagno complessivo dall'avvio del programma, USDT =    ", variabili.guadagno_tot)
            print("*****  il controvalore è in questo momento, USDT =                 ", variabili.profitto_non_realizzato)
            print("*****  prezzo medio di carico :                                    ", variabili.prezzo_medio)
            print("*****  prossimo BUY al prezzo di :                                 ",
                  (variabili.prezzo_medio - (variabili.prezzo_medio * percentuale_BUY / 100.00)))
            print("*****  prossimo SELL al prezzo di :                                ",
                  (variabili.prezzo_medio + (variabili.prezzo_medio * percentuale_SELL / 100)))
            print("*****  USDT spesi =                                                ", variabili.spesa_tot)
            print("*****  il prossimo acquisto avrà un importo pari a USDT =          ",
                  float(variabili.spesa + moltiplicatore * variabili.counter_failed))
            print("*****  budget residuo, USDT =                                      ", variabili.USDT_free)
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

    g_percentuale_BUY_1 = 2.0
    g_percentuale_BUY_2 = 2.0

    g_percentuale_SELL_1 = 2.0
    g_percentuale_SELL_2 = 2.0

    g_moltiplicatore_1 = 1
    g_moltiplicatore_2 = 1

    classe_coin_1 = data()
    classe_coin_2 = data()

    g_coin_1 = 'LUNA/USDT'
    g_coin_2 = 'BNB/USDT'

    g_nome_file_coin_1 = "backup_variabili_1.txt"
    g_nome_file_coin_2 = "backup_variabili_2.txt"


    g_file_1, g_line_num_1 = controllo_file(g_nome_file_coin_1, classe_coin_1)
    g_file_2, g_line_num_2 = controllo_file(g_nome_file_coin_2, classe_coin_2)



    if g_file_1 == 1:
        lettura_file(g_nome_file_coin_1, classe_coin_1, g_line_num_1)


    if g_file_2 == 1:
        lettura_file(g_nome_file_coin_2, classe_coin_2, g_line_num_2)

    while True:

        status_API = exchange.fetch_status()['status']
        print(status_API)
        if status_API == 'ok':

            buy_the_deep(classe_coin_1, g_coin_1, g_moltiplicatore_1, g_percentuale_BUY_1,g_percentuale_SELL_1)
            buy_the_deep(classe_coin_2, g_coin_2, g_moltiplicatore_2 ,g_percentuale_BUY_2,g_percentuale_SELL_2)

            scrittura_file(g_nome_file_coin_1, classe_coin_1)
            scrittura_file(g_nome_file_coin_2, classe_coin_2)


            if classe_coin_1.current_state == 2:
                os.remove(g_nome_file_coin_1)
                classe_coin_1.current_state = 0

            if classe_coin_2.current_state == 2:
                os.remove(g_nome_file_coin_2)
                classe_coin_2.current_state = 0

            g_gain = classe_coin_1.guadagno_tot + classe_coin_2.guadagno_tot

            f = open("GAIN.txt", "a")
            f.write(str(g_gain))
            f.close()

            print("GUADAGNO COMPLESSIVO SU TUTTE LE CRYPTO =   ", g_gain)
            print(" ")

            time.sleep(600)

        else:
            print("CONNESSIONE CADUTA, RIAVVIARE IL SISTEMA")
            exchange = ccxt.binance({
                'apiKey': config.BINANCE_API_KEY,
                'secret': config.BINANCE_SECRET_KEY,
                'enableRateLimit': True,
            })
            print("HO TENTATO LA RICONNESSIONE")
