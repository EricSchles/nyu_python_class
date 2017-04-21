def text_processing(string):
    return string.replace(",","_")

print(text_processing("Hello there, how are you?"))
print(text_processing("1,512,312,351,233,125,412"))
