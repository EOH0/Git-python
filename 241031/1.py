morse = { 
'.-':'a','-...':'b','-.-.':'c','-..':'d','.':'e','..-.':'f',
'--.':'g','....':'h','..':'i','.---':'j','-.-':'k','.-..':'l',
'--':'m','-.':'n','---':'o','.--.':'p','--.-':'q','.-.':'r',
'...':'s','-':'t','..-':'u','...-':'v','.--':'w','-..-':'x',
'-.--':'y','--..':'z'
}

# 테스트

msg =  ['..', '.-..', '---', '...-', '.', '.--.', '-.--', '-', '....', '---', '-.']
for val in msg:
    print(morse[val], end=" ")
morse_r = dict()
for key in morse:
    print(key, morse[key])
    morse_r[morse[key]] = key
# print(morse_r)
for ch in "ilovepython":
    print(ch, morse_r[ch], end=" / ")