# ------------------------------------------------ Define-se a Classe Quintupla ------------------------------------------------ #

class Quintupla:
    def __init__(self, Estado_atual, leitura, Escrita, Proximo_Estado, Direcao):
        self.Estado_atual = Estado_atual
        self.leitura = leitura
        self.Escrita = Escrita
        self.Proximo_Estado = Proximo_Estado
        self.Direcao = Direcao

# ------------------------------------------------ Define-se a Máquina de Turing (MT) ------------------------------------------- #

def MT(Fita, Quintuplas,max_de_passos):
    print('\nFita \u2192', Fita, '\n')
    Estado_atual = 0
    saida = 0
    aux = 0
    Estados = []
    Leituras = []
    posicao_Fita = 0

    # --- Tratamento dos Estados  --- #
    
    for quint in Quintuplas:
        Estados.append(Quintuplas[aux].Estado_atual)
        aux +=1
    aux = 0
    
    # --- Tratamento das Leituras  --- #
    
    for quint in Quintuplas:
        Leituras.append(Quintuplas[aux].leitura)
        aux +=1
    aux = 0
    
    # --- Posição inicial (cabeçote inicial da Fita)  --- #

    while (Fita[posicao_Fita] == 'b'):
        posicao_Fita += 1        
    
    # --- Computação da MF  --- #
    
    print('-----------------------------------------*Computação da MF*--------------------------------------------\n')

    print('Estado, posição na Fita, valor de leitura e valor de escrita em cada passo de camputação da MF:\n')
    
    m = 0
    while (Estado_atual in Estados and posicao_Fita >= 0 and posicao_Fita < len(Fita)):
        if aux >= len(Quintuplas):
            Estado_atual = 'Saída'
            break
            
        elif (Quintuplas[aux].leitura not in Leituras):
            Estado_atual = 'Saída'
            break
            
        elif (Estado_atual == Quintuplas[aux].Estado_atual and Fita[posicao_Fita] == Quintuplas[aux].leitura and m < max_de_passos):
            Fita[posicao_Fita] = Quintuplas[aux].Escrita
            Estado_atual = Quintuplas[aux].Proximo_Estado
            print('Estado \u2192', Estado_atual,' | Posição na fita \u2192', posicao_Fita,' | Valor de leitura \u2192', Quintuplas[aux].leitura, ' | Valor de Escrita \u2192', Quintuplas[aux].Escrita)
            posicao_Fita += 1 if (Quintuplas[aux].Direcao == 'R') else -1
            aux = -1 
            m += 1
        aux += 1
        
    print('\n-------------------------------------------------------------------------------------------------\n')
   
    print('Fita (depois da computação da MF) \u2192', Fita,'\n')    

# ------------------------------------------------ Main: definir parametros e decalrar a MT -------------------------------------- #

if __name__ == '__main__':
    
    # ---------------- construindo a fita ---------------- #
    entrada = input('\n Digite a entrada (Parte não vazia da fita): ')
    Parte_com_dados= [int(e) for e in entrada]
    Comprimento_Fita = len(Parte_com_dados)*3
  
    Fita = ['b']*Comprimento_Fita # (fita preenchida com espaços vazios'b')  
    
    for i,parte in enumerate(Parte_com_dados):
        Fita[Comprimento_Fita//2-len(Parte_com_dados)//2 + i] = parte
    # Sabemos que uma fita é infinita, mas para sua representação
    # temos somente um pedaço que comporta os dados (parte relevante)
      
    # ------------ maximo de passos ---------------- #

    max_de_passos = input('\n Digite o maximo de passos: ')
    max_de_passos = int(max_de_passos)

    # ---- Quintuplas da Máquina de Turing *(Alterar Quintuplas aqui)* ----- #
    
    Quintuplas = [Quintupla( 0 , 0 , 1 , 0 ,'R'),
                  Quintupla( 0 , 1 , 0 , 0 ,'R'),
                  Quintupla( 0 ,'b', 1 , 1 ,'L'),
                  Quintupla( 1 , 0 , 0 , 1 ,'R'),
                  Quintupla( 1 , 1 , 0 , 1 ,'R')]
    
    # --- Chamar a MT para os parametros da Fita e Quintuplas --- #
    
    # entrada utilizada no exemplo ilustrativo = "0110" , número máximo de passos do exemplo ilustrativo = "20"  

    MT(Fita,Quintuplas,max_de_passos)
    