#https://github.com/Ahamed-Fahim29/HIT137-Assignment-02_Group-125-SYD
def main():
    crypto_text="VZ FRYSVFU VZCNGVRAG NAQ N YVGGYR VAFRPHER V ZNXR ZVFGNXRF V NZ BHG BS PBAGEBY NAQNG GVZRF UNEQ GB UNAQYR OHG VS LBH PNAG UNAQYR ZR NG ZL JBEFG GURA LBH FHER NF URYYQBAG QRFREIR ZR NG ZL ORFG ZNEVYLA ZBAEBR"
    key=input("Give the shift key value :")
    original_text=""
    iterate=0
    while(True):
        try:
            Int_key=int(key)
        except ValueError:
            return 0
        cryptogram_to_original(crypto_text,int(key),original_text,iterate)
        key=input("If you still do not get the original text, Again give the shift key value :")
    return 0
def cryptogram_to_original(crypto_text,key,original_text,iterate):
    if(iterate<=len(crypto_text)-1):
        if crypto_text[iterate].isalpha()==True:
            if crypto_text[iterate].isupper==True:
                a=chr((((ord(crypto_text[iterate]))-65-key)%26)+65)
            else:
                a=chr((((ord(crypto_text[iterate]))-97-key)%26)+97)

            original_text=original_text+a
        else:
            original_text=original_text+crypto_text[iterate]
        iterate=iterate+1
        cryptogram_to_original(crypto_text,key,original_text,iterate)
    else:
        print (original_text)
        return original_text
main()