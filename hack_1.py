"""
generic script

text: "fooziman" output => "fOozIman" 
text: "qux" output => "qUx" 
text: "eq" output => "eq" 
"""


def fn_hack_1(result):
    if len(result)==3:
        result = result[0] + result[1].upper() + result[2]
    elif len(result)>=4:
        result= result.replace("oo", "Oo")
        result = result.replace("i", "I")

    return result

