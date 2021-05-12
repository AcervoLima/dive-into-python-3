SUFIXOS = {1000: ['KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB'],
           1024: ['KiB', 'MiB', 'GiB', 'TiB', 'PiB', 'EiB', 'ZiB', 'YiB']}

def tamanho_aproximado(tamanho, um_kilobyte_eh_1024_bytes=True):
    '''Converta um tamanho de arquivo em um formato legível.

    Argumentos keyword:
    tamanho -- tamanho do arquivo em bytes
    um_kilobyte_eh_1024_bytes -- if True (padrão), usa multiplos de 1024
                            if False, usa multiplos de 1000

    Retorna: string

    '''
    if tamanho < 0:
        raise ValueError('O número não deve ser negativo')

    multiplo = 1024 if um_kilobyte_eh_1024_bytes else 1000
    for sufixo in SUFIXOS[multiplo]:
        tamanho /= multiplo
        if tamanho < multiplo:
            return '{0:.1f} {1}'.format(tamanho, sufixo)

    raise ValueError('numero muito longo')

if __name__ == '__main__':
    print(tamanho_aproximado(1000000000000, False))
    print(tamanho_aproximado(1000000000000))