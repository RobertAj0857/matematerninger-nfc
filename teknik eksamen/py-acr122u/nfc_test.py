# import ndef
# from ndef.message import message_encoder, message_decoder
# import nfc

#epic
from src import nfc
from threading import Thread
import time



while(1):
    time.sleep(0.1)
    readers = []
    for reader in nfc.Reader.get_all_readers():
        readers.append(reader)
    for reader in readers:
        reader.print_data(reader.get_uid())
    try:
        reader0 = nfc.Reader(0)
        reader0.print_data(reader0.get_uid())
        reader0.info()
        print("Denne her kør nr0")
    except:
        ""
    try:
        #print("start of nr1")
        reader1 = nfc.Reader(1)
        reader1.print_data(reader1.get_uid())
        reader1.info()
        print("Denne her kør nr1")
    except:
        ""