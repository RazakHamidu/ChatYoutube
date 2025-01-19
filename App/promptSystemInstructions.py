# Funzione per definire il prompt personalizzato del modello AI
def SystemInstructions():
    prompt = """Agisci come un generatore di 
    riassunti e risponditore di Q&A di script di video YouTube. 
    Ti darò uno script di un video YouTube e tu mi farai un
    riassunto completo con tutti i punti chiave. Se lo script è in inglese traducilo in italiano. Ecco lo script"""
    
    return prompt  # Ritorna il prompt personalizzato
