class LetterAttr():
    name = ''
    isSet = False

    def __getattr__(self, arg):
        if LetterAttr.name or LetterAttr.isSet:
            return LetterAttr.name
        return arg

    def __setattr__(self, attr, val):
        new = ''
        for i in val:
            if i in attr:
                new += i
        LetterAttr.name = new
        LetterAttr.isSet = True
        return new
