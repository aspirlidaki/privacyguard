import logging
import sys

def setup_logger():
    """Ρυθμίζει το πώς θα φαίνονται τα μηνύματα του προγράμματος."""
    
    # Δημιουργούμε έναν logger με το όνομα του project μας
    logger = logging.getLogger("PrivacyGuard")
    logger.setLevel(logging.INFO) # Ορίζουμε ότι θέλουμε να βλέπουμε από INFO και πάνω

    # Ορίζουμε το format: [Ώρα] [Επίπεδο] Μήνυμα
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

    # Handler για να φαίνονται τα logs στην οθόνη (Terminal)
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    # Handler για να αποθηκεύονται τα logs σε αρχείο (για forensics)
    file_handler = logging.FileHandler("scanner.log")
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger

# Δημιουργούμε ένα instance που θα χρησιμοποιούμε παντού
logger = setup_logger()