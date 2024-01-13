#https://github.com/Ahamed-Fahim29/HIT137-Assignment-02_Group-125-SYD
def main():
    crypto_text="""tybony_inevnoyr = 100 
zl_qvpg= {'xr11': 'inyhr1', 'xr12': 'inyhr2', 'xr13': 'inyhr3'}

qrs cebprff_ahzoref():
    tybony tybony_inevnoyr 
    ybpny inevnoyr = 5
    ahzoref [1, 2, 3, 4, 5]

    juvyr ybpny_inevnoyr > 0:
        vs ybpny_inevnoyr % 2 == 0:
            ahzoref.erzbir(ybpny_inevnoyr)
        ybpny_inevnoyr -= 1

    erghea ahzoref

zl_frg = {1, 2, 3, 4, 5, 5, 4, 3, 2, 1} 
erfhyg = cebprff_ahzoref (ahzoref=zl_frg)

qrs zbqvsl_qvpg(): 
    ybpny_inevnoyr = 10 
    zl_qvpg['xr14'] = ybpny_inevnoyr

zbqvsl_qvpg(5)

qrs hcqngr_tybony():
    tybony tybony_inevnoyr
    tybony_inevnoyr += 10

sbe v va enatr(5):
    cevag(v)
    V += 1

vs zl_frg vf abg Abar naq z1_qvpg['xr14'] == 10: 
    cevag("Pbaqvgvba zrg!")

vs 5 abg va zl_qvpg:
    cevag("5 abg sbhaq va gur qvpgvbanel!")

cevag(tybony_inevnoyr)
cevag(zl_qvpg)
cevag(z1_frg)"""
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
        f = open("question3_sub1.py", "w")#change the file name to question3_sub to question3_sub1, to not erasing the corrected code
        f.write(original_text)
        f.close()
        return original_text
main()