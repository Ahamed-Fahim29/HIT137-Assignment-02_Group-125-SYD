#https://github.com/Ahamed-Fahim29/HIT137-Assignment-02_Group-125-SYD
def main():
    long_string= input("Assume String :")
    iterate=0
    number_string=""
    letter_string=""
    Ascii_upper_case=""
    Separate_string(iterate,long_string,number_string,letter_string,Ascii_upper_case)
    return 0

#Recursive function used to optimize the code
def Separate_string(iterate,long_string,number_string,letter_string,Ascii_upper_case):
    if(iterate<=len(long_string)-1):
        if((long_string[iterate]>='0')and(long_string[iterate]<='9')):
            number_string=number_string + long_string[iterate]
        if((long_string[iterate]>='A')and(long_string[iterate]<='Z')):
            letter_string=letter_string + long_string[iterate]
            a=ord(long_string[iterate])
            Ascii_upper_case=Ascii_upper_case+str(a)+" "
        if((long_string[iterate]>='a')and(long_string[iterate]<='z')):
            letter_string=letter_string + long_string[iterate]
        iterate=iterate+1
        Separate_string(iterate,long_string,number_string,letter_string,Ascii_upper_case)
    else:
        print("Number String :"+number_string)
        print("Letter String :"+letter_string)
        iterate = 0
        Ascii_even_number=""
        Even_ascii(iterate,number_string,Ascii_even_number)
        print("Upper Case Letter Ascii Value :"+Ascii_upper_case)
        return 0
    
def Even_ascii(iterate,number_string,Ascii_even_number):
    if(iterate<=len(number_string)-1):
        a=int(number_string[iterate])
        if(a%2==0):
            Ascii_even_number=Ascii_even_number+str(a+48)+" "
        iterate=iterate+1
        Even_ascii(iterate,number_string,Ascii_even_number)
    else:
        print("Even Number Ascii value :"+Ascii_even_number)
        return 0

main()