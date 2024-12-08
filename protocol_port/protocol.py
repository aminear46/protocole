# protocol_port/protocol_port/protocol.py

def get_protocol_port(protocol):
    # Dictionnaire des protocoles et des ports associés
    protocols = {
        "http": 80,
        "https": 443,
        "ftp": 21,
        "ssh": 22,
        "smtp": 25,
        "dns": 53,
        "pop3": 110,
        "imap": 143,
        "telnet": 23
    }

    # Retourne le port associé au protocole ou un message si inconnu
    return protocols.get(protocol.lower(), "Protocole non reconnu")
