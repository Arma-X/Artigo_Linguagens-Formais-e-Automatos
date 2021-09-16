# -------------------------------------------- Define-se a Classe Estado --------------------------------------------- #

class Estado:
    def __init__(self, termo, caminho_0, caminho_1, saida):
        self.termo = termo
        self.caminho_0 = caminho_0
        self.caminho_1 = caminho_1
        self.saida = saida

# ------------------------------------------ Define-se a Máquina de Estados Finitos (MEF) --------------------------------- #

def MEF(Entrada, Estados):

    print('\n Entrada \u2192',Entrada)
    Comprimento_Entrada = len(Entrada)
    saida = ['b']*Comprimento_Entrada    
    m = 0

    # --- Primeiro estado --- #
    
    n = 0
    while n < len(Estados):
        if Estados[n].termo == 0:
            Estado_atual = Estados[n]
            break
        n+=1
        
    print('\n* Estado_inicial \u2192', Estado_atual.termo,'\n')
    
    # ---  quebra da MEF -> falso --- #

    Estado_de_quebra = 0 
        
    # --- Computação da Entrada --- #
    
    print('Estados e saidas de cada etapa de computação da MEF:\n')   
    while (len(Entrada) != 0):
        aux = Entrada[0]
        Entrada.pop(0)
                
        if (aux == 0):
            
            if (Estado_atual.caminho_0 != 'Estado_de_quebra'):
                Prox_estado = Estado_atual.caminho_0
            else:
                Estado_de_quebra = 1
                
        elif (aux == 1):
            
            if (Estado_atual.caminho_1 != 'Estado_de_quebra'):
                Prox_estado = Estado_atual.caminho_1
            else:
                Estado_de_quebra = 1
        
        if (Estado_de_quebra != 1):
            n = 0
            while (n < len(Estados)):
                if (Estados[n].termo == Prox_estado):
                    Estado_atual = Estados[n]
                    break
                n += 1            
            print('* Estado_atual \u2192' ,Estado_atual.termo, '| Saida \u2192', Estado_atual.saida)

        saida[m] = Estado_atual.saida
        m +=1

    print('\n Saida \u2192',saida)

    # ---  quebra da MEF -> verdadeiro --- #

    if (Estado_de_quebra == 1): 
        print('\n *** A MEF quebrou, entrou em um estado onde não consegue computar. ***\n')   

    # ---  MEF reconhece a Entrada -> verdadeiro --- #
  
    elif (Estado_atual.termo == 0): #(Criterio de aceitação, Estado_atual == *Estado de aceitação* )
        print('\n *** A MEF reconhece a Entrada ***\n')
           
    # ---  MEF reconhece a Entrada -> falso --- #

    else:
        print('\n *** A Entrada não é reconhecida pela MEF ***\n')
    
    
# ------------------------------------------ Main: definir parametros e decalrar a MEF --------------------------------- #

if __name__ == '__main__':
   
    # --- vetor de entrada  --- #
    entrada = input('\n Digite uma entrada (Apenas 0s e 1s): ')
    Entrada = [int(e) for e in entrada] 

    # --- Estados da Máquina *(alterar estados aqui)* --- #
    
    Estados = [Estado(0,1,0,0), 
               Estado(1,2,1,1), 
               Estado(2,2,0,1)]
             
    # --- Chamar a MEF para os parametros de Entrada e Estados --- #
    
    # Entrada utilizada no exemplo ilustrativo = "01101"

    MEF(Entrada,Estados)


