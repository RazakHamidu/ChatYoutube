# SumTube

## Descrizione del progetto

**Problema**: Quando non hai abbastanza tempo per guardare lunghi podcast o vuoi solo farti un'idea dei punti principali di un video YouTube, trovare queste informazioni rapidamente può essere complicato e richiede troppo tempo.

**Soluzione**: SumTube è un'applicazione progettata per risolvere questo problema, consentendo di generare riassunti dettagliati dei video YouTube. L'app utilizza il modello AI gemini-2.0-flash-exp per elaborare i contenuti dei video e creare riassunti chiari e utili, permettendoti di risparmiare tempo e accedere direttamente alle informazioni principali.

L'app è stata sviluppata con **Streamlit** per un'interfaccia utente interattiva e **Google Generative AI (gemini-2.0-flash-exp)** per il processo di generazione del contenuto.

---

## Struttura del progetto

La struttura del progetto è la seguente:

```
App/
|-- __pycache__/                  # File compilati dal sistema
|-- .env                         # File contenente le variabili di ambiente
|-- main.py                      # File principale dell'app Streamlit
|-- model.py                     # Funzione principale per generare i contenuti
|-- promptSystemInstructions.py  # Prompt per le istruzioni del modello AI
|-- YouTubeTranscripts.py        # Modulo per estrarre trascrizioni da YouTube
                           
|-- ...
.gitignore                       
README.md                        
requirements.txt                 
```

### Dettagli dei file principali

1. **main.py**:

   - File principale che definisce l'interfaccia utente utilizzando Streamlit.
   - Consente di inserire un link YouTube e visualizza il video con il riassunto generato.

2. **model.py**:

   - Configura l'API di Google Generative AI (gemini-2.0-flash-exp).
   - Integra i prompt e i transcript per generare il contenuto finale.

3. **promptSystemInstructions.py**:

   - Contiene le istruzioni del sistema per il modello AI gemini-2.0-flash-exp, specificando come agire.

4. **YouTubeTranscripts.py**:

   - Usa **LangChain** per estrarre trascrizioni dai video di YouTube.

5. **requirements.txt**:

   - Specifica le dipendenze necessarie per eseguire il progetto, come Streamlit, LangChain e altre librerie correlate.

6. **.env**:

   - Contiene la chiave API di Google (ad es., `GOOGLE_API_KEY`).

---

## Installazione

Per utilizzare l'applicazione, segui i passaggi seguenti:

### 1. Clona il repository

```bash
$ git clone <URL_DEL_REPOSITORY>
$ cd SumTube
```

### 2. Crea un ambiente virtuale

```bash
$ python -m venv venv
$ source venv/bin/activate   # Su Windows: venv\Scripts\activate
```

### 3. Installa le dipendenze

```bash
$ pip install -r requirements.txt
```

### 4. Configura le variabili di ambiente

Crea un file `.env` nella directory principale e aggiungi la tua chiave API di Google:

```
GOOGLE_API_KEY=la_tua_chiave_api
```

### 5. Avvia l'applicazione

```bash
$ streamlit run App/main.py
```

---

## Utilizzo

1. Inserisci il link di un video YouTube nell'app.
2. L'app mostrerà il video e genererà automaticamente:
   - Un riassunto completo con i punti chiave.

---

## Licenza

Questo progetto è rilasciato sotto la [MIT License](LICENSE).

