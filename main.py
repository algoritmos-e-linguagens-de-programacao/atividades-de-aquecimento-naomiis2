def maxtroca_de_figurinhas(fig_da_maria, fig_do_joao):
    i = 0
    j = 0
    control = 0
    quant = 0

    if len(fig_da_maria) < len(fig_do_joao):  
        for i in range(len(fig_da_maria)):
            for j in range(len(fig_do_joao)):
                if fig_da_maria[i] == fig_do_joao[j]:
                    control += 1
        quant = len(fig_da_maria) - control

    elif len(fig_do_joao) < len(fig_da_maria):
        for i in range(len(fig_do_joao)):
            for j in range(len(fig_da_maria)):
                if fig_do_joao[i] == fig_da_maria[j]:
                    control += 1
        quant = len(fig_do_joao) - control
                                                          
    else:
        for i in range(len(fig_da_maria)):
            for j in range(len(fig_do_joao)):
                if fig_da_maria[i] == fig_do_joao[j]:
                    control += 1
        quant = len(fig_da_maria) - control

    return quant1