
class KnapSack(object):
    def __init__(self,n,q,w,valores,tamanhos):
        self.n = n # numero de itens no problema
        self.q = q # quantidade de cada item
        self.w = w # espaço na mochila
        self.valores = valores # valor de cada item
        self.tamanhos = tamanhos # tamanho ocupado por cada item

    def solve(self):
        m = [[0 for x in range(self.w+1)] for y in range(self.n+1)] # memoria matriz NxW
        #print(m)
        pre = [[(-1,-1,-1) for x in range(self.w+1)]for y in range(self.n+1) ] # memoria matriz NxW

        for i in range(1,self.n + 1): # for de 1 até n, o item da posicao 0 é considerado o item 1
            for tamanhoRestante in range(self.w + 1):
                #Se tamanho do item for maior que o tamanho restante
                if(self.tamanhos[i-1] > tamanhoRestante):
                    m[i][tamanhoRestante] =  m[i-1][tamanhoRestante]
                    pre[i][tamanhoRestante] = (i-1,tamanhoRestante)
                else:
                    maximo = m[i-1][tamanhoRestante]
                    premax = (i-1,tamanhoRestante)
                    for k in range(1,self.q+1):
                        if(k*self.tamanhos[i - 1] > tamanhoRestante):
                            break
                        else:
                            incluiItem = m[i-1][tamanhoRestante - (k*self.tamanhos[i-1])] + k*self.valores[i-1]
                            if (m[i-1][tamanhoRestante] > maximo):
                                maximo = m[i-1][tamanhoRestante]
                                premax = (i-1,tamanhoRestante)
                            elif (incluiItem > maximo):
                                maximo = incluiItem
                                premax = (i-1,tamanhoRestante - k*self.tamanhos[i-1])
                    m[i][tamanhoRestante] = maximo
                    pre[i][tamanhoRestante] = premax

        #printMatriz(self,m)
        #printMatriz(self,pre)
        solucao = []
        anterior = pre[self.n][self.w]
        item = self.n
        tam = self.w
        while anterior != (-1,-1,-1):
            qt = (int) ((tam-anterior[1]) / self.tamanhos[item-1])
            if(qt != 0):
                solucao.append([item,qt])
            tam = anterior[1]
            item = anterior[0]
            anterior = pre[item][tam]
        print('[Indice do item,quantidade]',solucao)
        return m[self.n][self.w]

def printMatriz(self,m):
    for l in m:
        for e in l:
            print(e,end=' ')
        print()



