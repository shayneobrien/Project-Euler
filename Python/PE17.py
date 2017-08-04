# PE17 If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?
# very hacky code

def translate(digit): 
    return {
        0: '',
        1: 'one',
        2: 'two',
        3: 'three',
        4: 'four',
        5: 'five',
        6: 'six',
        7: 'seven',
        8: 'eight',
        9: 'nine',
        10: 'ten',
        11: 'eleven',
        12: 'twelve',
        13: 'thirteen',
        14: 'fourteen',
        15: 'fifteen',
        16: 'sixteen',
        17: 'seventeen',
        18: 'eighteen',
        19: 'nineteen',
        20: 'twenty',
        30: 'thirty',
        40: 'forty',
        50: 'fifty',
        60: 'sixty',
        70: 'seventy',
        80: 'eighty',
        90: 'ninety',
        100: 'hundred',
        1000: 'onethousand'
    }.get(digit, -1)

def spell(number):
    if number > 20:
        keep = ''
        number = str(number)
        if len(number) == 2: # case for 21-99
            keep += translate(int(number[0] + '0'))
            keep += translate(int(number[1]))
        elif len(number) == 3: 
            keep += translate(int(number[0]))
            keep += translate(100)
            if int(number) % 100 != 0:
                keep += 'and'
                if int(number[1:]) > 20:
                    keep += (translate(int(number[1] + '0')))
                    keep += translate(int(number[2]))
                else:
                    keep += translate(int(number[1:]))
        elif int(number) >= 1000:
            keep += translate(1000)
        return keep
    else:
        return translate(number)
    
count = 0
for i in xrange(1001):
    count += len(spell(i))
    
print count
