class Pigtail:
    def __init__ (self, st):
        self.s = st
    def odinp(self):
        rast = 1
        prob = 2
        sp = []
        prib = False
        for i in range(len(self.s)//2-1, 0, -1):
            if prob > 0 and prob != 1:
                prib = False
            elif prob == 0:
                prib = True
            if prib == False:
                sp.append((f'{' '*prob}{self.s[i]}{' '*abs(prob-2)*2}{self.s[i+rast]}'))
                prob -= 1
            else:
                sp.append((f'{' '*prob}{self.s[i]}{' '*abs(prob-2)*2}{self.s[i+rast]}'))
                prob += 1
            rast += 2
        return '\n'.join(sp)
    def neodinp(self):
        x = [self.s[i:i+2] for i in range(0,len(self.s), 2)]
        rast = 1
        prob = 2
        sp = []
        prib = False
        for i in range(len(x)//2-1, 0, -1):
            if prob > 0 and prob != 1:
                prib = False
            elif prob == 0:
                prib = True
            if prib == False:
                sp.append((f'{' '*prob}{x[i]}{' '*abs(prob-2)*2}{x[i+rast]}'))
                prob -= 1
            else:
                sp.append((f'{' '*prob}{x[i]}{' '*abs(prob-2)*2}{x[i+rast]}'))
                prob += 1
            rast += 2
        return '\n'.join(sp)
    def vaneodinp(self):
        x = [self.s[i:i+4] for i in range(0,len(self.s), 4)]
        rast = 1
        prob = 2
        sp = []
        prib = False
        for i in range(len(x)//2-1, 0, -1):
            if prob > 0 and prob != 1:
                prib = False
            elif prob == 0:
                prib = True
            if prib == False:
                sp.append((f'{' '*prob}{x[i]}{' '*abs(prob-2)*2}{x[i+rast]}'))
                prob -= 1
            else:
                sp.append((f'{' '*prob}{x[i]}{' '*abs(prob-2)*2}{x[i+rast]}'))
                prob += 1
            rast += 2
        return '\n'.join(sp)
pigtail = Pigtail('ABCDEFGHIJKLMNOPQRSTUVWX')