def fa_grouped(datos, lim_inf, lim_sup):
    fa = [0] * len(lim_inf)
    clases = list(range(1,len(lim_inf)+1))

    for elemento in datos:
        for j in range(0, len(lim_inf)):
            if j == len(lim_inf)-1:
            #if j == 0:
                if lim_inf[j] <= elemento <= lim_sup[j]:
                    fa[j] += 1
                    break
            else:
                if lim_inf[j] <= elemento < lim_sup[j]:
                #if lim_inf[j] < elemento <= lim_sup[j]:
                    fa[j] += 1
                    break
    return fa, clases