def somar(a, b):
    """Soma dois números."""
    return a + b

def subtrair(a, b):
    """Subtrai dois números, retornando sempre um valor positivo."""
    if a > b:
        return a - b
    else:
        # Esta linha não será testada no nosso primeiro teste
        return b - a 
        # Commit para forçar o CI teste final