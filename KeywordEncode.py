#############################################
# BENJAMIN HANNAH | ENCODE / DECODE | MAY 4 #
#############################################
#-------------------------------------------#
UPPER = tuple([chr(n) for n in range (65, 91)])
LOWER = tuple([chr(n) for n in range (97, 123)])
DIGIT = tuple([chr(n) for n in range (48, 58)])

def Modulated_Word(x):
    global MODULATOR
    
    MODULATOR = []
    for c in x:
        if c in UPPER:
            MODULATOR.append(ord(c) - 64)
        if c in LOWER:
            MODULATOR.append(ord(c) - 96)
        if c in DIGIT:
            MODULATOR.append(ord(c) - 48)
    print "Modulator =",MODULATOR


#Encode

h = "Good morning"

#MODULATOR
Modulated_Word("cow")
M = 0

encode = list()
encode_str = str()
c_list = list(h)


for c in c_list:
    if M >= 3:
       M = 0
    if c in UPPER:
       x = chr(ord(c) + MODULATOR[M])
       if x in UPPER:
           encode.append(x)
       if ord(x) > ord(UPPER[-1]):
           encode.append(chr(ord(x) - 26))
       if ord(x) < ord(UPPER[0]):
           encode.append(chr(ord(x) + 26))
    elif c in LOWER:
       x = chr(ord(c) + MODULATOR[M])
       if x in LOWER:
           encode.append(x)
       if ord(x) > ord(LOWER[-1]):
           encode.append(chr(ord(x) - 26))
       if ord(x) < ord(LOWER[0]):
           encode.append(chr(ord(x) + 26))
    elif c in DIGIT:
       x = chr(ord(c) + MODULATOR[M])
       if x in DIGIT:
           encode.append(x)
       if ord(x) > ord(DIGIT[-1]):
           encode.append(chr(ord(x) - 10))
       if ord(x) < ord(DIGIT[0]):
           encode.append(chr(ord(x) + 10))
    else:
       encode.append(c)
       M += -1
    M += 1
    
for c in encode:
    encode_str += c
print "Encoded Message =",encode_str

#-----------------------------------------------------#
#Decode

h = encode_str
decode = list()
decode_str = str()
d_list = list(h)

UPPER_D = tuple([chr(n) for n in range (65 , 91)])
LOWER_D = tuple([chr(n) for n in range (97, 123)])
DIGIT_D = tuple([chr(n) for n in range (48, 58)])

DMODULATOR = MODULATOR #COW
DM = 0 

for d in d_list:
    if DM >= 3:
       DM = 0
    if d in UPPER_D:
       x = chr(ord(d) - DMODULATOR[DM])
       if x in UPPER:
           decode.append(x)
       if ord(x) > ord(UPPER[-1]):
           decode.append(chr(ord(x) - 26))
       if ord(x) < ord(UPPER[0]):
           decode.append(chr(ord(x) + 26))
    elif d in LOWER_D:
       x = chr(ord(d) - DMODULATOR[DM])
       if x in LOWER:
           decode.append(x)
       if ord(x) > ord(LOWER[-1]):
           decode.append(chr(ord(x) - 26))
       if ord(x) < ord(LOWER[0]):
           decode.append(chr(ord(x) + 26))
    elif d in DIGIT_D:
       x = chr(ord(d) - DMODULATOR[DM])
       if x in DIGIT:
           decode.append(x)
       if ord(x) > ord(DIGIT[-1]):
           decode.append(chr(ord(x) - 10))
       if ord(x) < ord(DIGIT[0]):
           decode.append(chr(ord(x) + 10))
    else:
           decode.append(d)
           DM += -1
    DM += 1

for d in decode:
    decode_str += d
print "Decoded Message =", decode_str
