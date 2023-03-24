# import ndef
# from ndef.message import message_encoder, message_decoder
# import nfc

#reader0-2, left to right

#epic


from src import nfc
from threading import Thread
import time

dice_table = [[[25, 12, 182, 110],1],[[89, 22, 180, 109],2],[[57, 175, 190, 110],3],[[70, 230, 97, 249],4],[[23, 43, 95, 179],5],[[133, 22, 249, 194],6]]


def parse_data(data_in):
    dice_id =   data_in[0]
    position = data_in[1]
    dice_number = compare_id(dice_table, dice_id)
    print("number",dice_number )
    

def compare_id(list_in, id_in):
    for sublist in list_in:
        if id_in in sublist[0]:
            index = sublist[0].index(id_in)
            if index < len(sublist[0])-1:
                return sublist[0][index+1]
            else:
                return None



while(1):
    time.sleep(0.1)
    try:
        reader0 = nfc.Reader(0)
        readerData0 = reader0.get_data(reader0.get_uid())
        print(readerData0, "reader0")
    except:
        ""
    try:
        reader1 = nfc.Reader(1)
        readerData1 = reader1.get_data(reader1.get_uid())
        print(readerData1, "reader1")
    except:
        ""
    try:
        reader2 = nfc.Reader(2)
        readerData2 = reader2.get_data(reader2.get_uid())
        print(parse_data(readerData2), "reader2")
        
        
    except:
        ""


