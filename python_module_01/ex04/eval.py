class Evaluator:
    @staticmethod
    def validate(coefs, words):
        if not isinstance(coefs, list):
                return "First argument has to be a list"
        if not isinstance(words, list):
                return "Second argument has to be a list"
        if not all(isinstance(i, str) for i in words):
            return "Second argument must only contain strings"
        if not all(isinstance(i, (float, int)) for i in coefs):
            return "Second argument must only contain integers or floats"
        return False
       
    @staticmethod
    def zip_evaluate(coefs, words):
        if Evaluator.validate(coefs, words):
            raise ValueError(Evaluator.validate(coefs, words))
        if len(coefs) is not len(words):
            print -1
        ret = 0
        for i, j in zip(coefs, words):
             ret += i * len(j)
        return (ret)

    @staticmethod
    def enumerate_evaluate(coefs, words):
        if Evaluator.validate(coefs, words):
            raise ValueError(Evaluator.validate(coefs, words))
        if len(coefs) is not len(words):
            print -1
        ret = 0
        for i, j in enumerate(coefs, 0):
            ret += j * len(words[i])
        return(ret)
