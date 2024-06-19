from cryptography.fernet import Fernet
from getmac import get_mac_address as gma

import datetime
import pandas as pd
from datetime import datetime, timedelta

print(gma())

def decrypt (dec_msg):
    crypto_key = b'9tvb2SoOaB11TA4YN3CydnGq4IfvSVSZJy25B6bdskM='

    # Initialize Fernet with the encryption key
    fernet = Fernet(crypto_key)
    # Encrypt the MAC address

    enc_macid = dec_msg.encode('utf-8')
    print("Print Enc mac " ,enc_macid)
    # Decrypt the encrypted MAC address (optional)
    dec_mac = fernet.decrypt(enc_macid).decode()
    return dec_mac

def authentication_main(df):
    mac, softwaretype, Software_sold_date = licence_dec(df)
    day_bal, auth_status = validate(mac, softwaretype, Software_sold_date)
    return day_bal, auth_status, softwaretype   

def licence_dec(df):
    try:
        Activation_Key = df.loc[4, 'Info']

        dec_key = decrypt(Activation_Key)
        mac= dec_key[1:]
        softwaretype = int(dec_key[0])
        software_date= df.loc[3, 'Info']
        dec_sold_date = decrypt(software_date)
        Software_sold_date = datetime.strptime(dec_sold_date, '%d/%m/%Y')

    except Exception as e:
        print(f"Error updating license: {e}")
    return mac, softwaretype, Software_sold_date

def validate(mac, softwaretype, Software_sold_date):          
    try:
        # Assuming the date format is 'DD/MM/YYYY'
        print(mac, softwaretype, Software_sold_date)
        auth_status = 0
        current_date = datetime.now()
        if gma(0) == mac:
            auth_status = 1 
            if softwaretype == 0:
                day_bal = (current_date - Software_sold_date).days
                # Check if the software is within the allowed time period (1 month)
                if (current_date - Software_sold_date ).days > 30:
                    auth_status = 2                                 
            else:
                day_bal = 0
                
    except ValueError as e:
        print("Error parsing release date:", e)
    return day_bal, auth_status 