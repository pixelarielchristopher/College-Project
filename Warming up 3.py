socks = input("Input colored socks = ").replace(',',' ')
wordlist = socks.split()

def histogram(text):
    histo = dict()
    print("Sell-able socks")
    for word in wordlist:
        if word in histo:
            histo[word] += 1
        else:
            histo[word] = 1
        h = histo[word]//2
        if h > 0:
            print(word,"=",h)

myHisto = histogram(socks)