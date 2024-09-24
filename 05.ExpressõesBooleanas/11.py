def funcao(data):
    dia, mes, ano = 0, 0, 0
    
    if len(data) == 10 and data[2] == '/' and data[5] == '/':
        dia_str = data[:2]
        mes_str = data[3:5]
        ano_str = data[6:]
        
        if (dia_str.isdigit() and mes_str.isdigit() and ano_str.isdigit() and
            len(dia_str) == 2 and len(mes_str) == 2 and len(ano_str) == 4):
            
            mes = int(mes_str)
            ano = int(ano_str)
            
            if 1 <= mes <= 12:
                dias_por_mes = [31, 29 if (ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0)) else 28,
                                31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
                
                # do intervalo válido para o mês
                if 1 <= dia <= dias_por_mes[mes - 1]:
                    return dia, mes, ano
    return 0, 0, 0