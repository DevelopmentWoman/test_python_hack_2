"""
text: {"foo":"fookziman","bar":"barziman"} output => {"Foo":"Fooziman"}
"""


def fn_hack_9(result):
    result.pop("bar",None)
    result ={k.capitalize() if k == "foo" else k: (v.capitalize()).replace("ook","oo") for k,v in result.items()}
    return result



# print(fn_hack_9({"foo":"fookziman","bar":"barziman"}))