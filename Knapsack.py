class KnapSack(object):
    def __init__(self,n,q,w,valores,tamanhos):
        self.n = n # numero de itens no problema
        self.q = [q for i in range(n)] # quantidade de cada item
        self.w = w # espaço na mochila
        self.valores = valores # valor de cada item
        self.tamanhos = tamanhos # tamanho ocupado por cada item

    def solve(self):
        m = [[0 for x in range(self.w+1)] for y in range(self.n+1)] # memoria matriz NxW
        pre = [[(-1,-1) for x in range(self.w+1)]for y in range(self.n+1) ] # memoria matriz NxW

        for i in range(1,self.n + 1):
            for tamanhoRestante in range(self.w + 1):
                print(i,tamanhoRestante)
                naoInclui = m[i-1][tamanhoRestante]
                if tamanhoRestante < self.tamanhos[i-1]:
                    m[i][tamanhoRestante] = naoInclui
                    pre[i][tamanhoRestante] = (i - 1, tamanhoRestante)
                else:
                    inclui_e_troca = self.valores[i-1] + m[i-1][ tamanhoRestante -self.tamanhos[i-1] ]
                    inclui_e_continua = self.valores[i-1] + m[i][tamanhoRestante - self.tamanhos[i-1]]
                    melhorOpcao = max( naoInclui, inclui_e_continua, inclui_e_troca)
                    if melhorOpcao == inclui_e_troca and self.q[i-1] > 0:
                        self.q[i - 1] -= 1
                        pre[i][tamanhoRestante] = (i-1,tamanhoRestante -self.tamanhos[i-1])
                        m[i][tamanhoRestante] = inclui_e_troca
                    elif melhorOpcao == inclui_e_continua and self.q[i-1] > 0:
                        self.q[i - 1] -= 1
                        pre[i][tamanhoRestante] = (i,tamanhoRestante -self.tamanhos[i-1])
                        m[i][tamanhoRestante] = inclui_e_continua
                    else:
                        pre[i][tamanhoRestante] = (i - 1, tamanhoRestante)
                        m[i][tamanhoRestante] = naoInclui
        #print('lalalsdlasldaldas', self.q)
        self.printMatriz(m)
        self.printMatriz(pre)

        solucao = []
        anterior = pre[self.n][self.w]
        item = self.n
        tam = self.w
        while anterior != (-1,-1):
            if anterior[1] != tam:
                solucao.append(item)
            tam = anterior[1]
            item = anterior[0]
            anterior = pre[item][tam]


        solucao.sort()
        return solucao

    def printMatriz(self,m):
        for l in m:
            for e in l:
                print(e,end=' ')
            print()



a = KnapSack(2,10,22,[5,1],[2,1])
#a = KnapSack(2,10,8,[2,1],[3,2])
path = a.solve()
print('path recebido',str(path))

