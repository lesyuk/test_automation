"""
splitAndMerge("My name is John", " ")  ==  "M y n a m e i s J o h n"
splitAndMerge("My name is John", "-")  ==  "M-y n-a-m-e i-s J-o-h-n"
splitAndMerge("Hello World!", ".")     ==  "H.e.l.l.o W.o.r.l.d.!"
splitAndMerge("Hello World!", ",")     ==  "H,e,l,l,o W,o,r,l,d,!"
"""


def split_and_merge(string_, separator):
    split_str = string_.split()
    for i in range(len(split_str)):
        split_str[i] = separator.join(split_str[i])
    return ' '.join(split_str)


print(split_and_merge("Hello World!", "."))