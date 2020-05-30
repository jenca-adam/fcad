import fcad
def decode(string, dicti):
        srt=""
        for i in string:
            srt+=dicti[i]
        return(srt)
print(decode('ahoj',{'a':'k','h':'q','o':'w','j':'v'}))
