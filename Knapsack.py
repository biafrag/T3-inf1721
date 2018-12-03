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
        qtAnt = 1
        for i in range(1,self.n + 1):
            for tamanhoRestante in range(self.w + 1):
                #Se tamanho da mochila for maior que o tamanho restante
                if(self.tamanhos[i-1] > tamanhoRestante):
                    m[i][tamanhoRestante] =  m[i-1][tamanhoRestante]
                    pre[i][tamanhoRestante] = (i-1,tamanhoRestante,qtAnt)
                else:
                    max = m[i-1][tamanhoRestante]
                    premax = (i-1,tamanhoRestante)
                    incluiItem = False
                    for k in range(1,self.q+1):
                        if(k*self.tamanhos[i - 1] > tamanhoRestante):
                            break
                        else:
                            incluiItem = m[i-1][tamanhoRestante - (k*self.tamanhos[i-1])] + k*self.valores[i-1]
                            if (m[i-1][tamanhoRestante] > max):
                                max = m[i-1][tamanhoRestante]
                                premax = (i-1,tamanhoRestante,1)
                                incluiItem = False
                            elif (incluiItem > max):
                                max = incluiItem
                                premax = (i-1,tamanhoRestante - k*self.tamanhos[i-1],qtAnt)
                                incluiItem = True
                    m[i][tamanhoRestante] = max
                    pre[i][tamanhoRestante] = premax
                    if(incluiItem == True):
                       qtAnt = k
                       print("incluiu\n")
                    else:
                        qtAnt = 1
                        print("Nao inluiu\n")

        printMatriz(self,m)
        printMatriz(self,pre)
        solucao = []
        anterior = pre[self.n][self.w]
        item = self.n
        tam = self.w
        while anterior != (-1,-1,-1):
            print(anterior[2])
            for r in range(0,anterior[2]):
                solucao.append(anterior[0]+1)
               # print (solucao)
            item = anterior[0]
            tam = anterior[1]
            anterior = pre[item][tam]



        #solucao.sort()
        print(solucao)
        return m[self.n][self.w]

def printMatriz(self,m):
    for l in m:
        for e in l:
            print(e,end=' ')
        print()


if __name__ == '__main__':
    a = KnapSack(2,10,22,[5,1],[2,1])
    #a = KnapSack(2,10,8,[2,1],[3,2])
    solucao = a.solve()
    print('Solucao ',str(solucao))

