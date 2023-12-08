FILE = r"day_3_input.txt"

class Parser:
    LINES = []
    HASH = {}
    N = 0
    RESULT = []

    def __init__(self, path):
        self.LINES = [line.strip() for line in open(path, "r").readlines()]
        self.N = len(self.LINES)
        self.RESULT = [self.partOne(), self.partTwo()]

    def check_left(self, l, line, line_ind, st):
        if line[l-1] != ".":
            if line[l-1] == "*":
                coords = (line_ind, l - 1)
                if self.HASH.get(coords) is None:
                    self.HASH[coords] = []
                self.HASH[coords].append(int(st))
            return True
        return False
    
    def check_right(self, r, line, line_ind, st):
        if line[r+1] != ".":
            if line[r+1] == "*":
                coords = (line_ind, r + 1)
                if self.HASH.get(coords) is None:
                    self.HASH[coords] = []
                self.HASH[coords].append(int(st))
            return True
        return False
    
    def check_mid(self, l, r, line_ind, st):
        for i in range(l - 1, r + 2):
            try:
                if line_ind > 0:
                    if self.LINES[line_ind-1][i] != "." and not self.LINES[line_ind-1][i].isdigit():
                        if self.LINES[line_ind-1][i] == "*":
                            coords = (line_ind - 1, i)
                            if self.HASH.get(coords) is None:
                                self.HASH[coords] = []
                            self.HASH[coords].append(int(st))
                        return True
                if line_ind < self.N - 1:
                    if self.LINES[line_ind+1][i] != "." and not self.LINES[line_ind+1][i].isdigit():
                        if self.LINES[line_ind+1][i] == "*":
                            coords = (line_ind+1, i)
                            if self.HASH.get(coords) is None:
                                self.HASH[coords] = []
                            self.HASH[coords].append(int(st))
                        return True
            except:
                continue
        return False
    
    def partOne(self):
        s = 0
        for i in range(self.N):
            curr = self.LINES[i]
            l, r = -1, 0
            st = ""
            for j in range(len(curr)):
                if curr[j].isdigit():
                    st += curr[j]
                    if l == -1:
                        l = j
                    r = j
                else:
                    if st:
                        sym_flag = False
                        if l > 0:
                            sym_flag = self.check_left(l, curr, i, st)
                        if r < len(curr) - 1 and not sym_flag:
                            sym_flag = self.check_right(r, curr, i, st)
                        if not sym_flag:
                            sym_flag = self.check_mid(l, r, i, st)
                        
                        if sym_flag:
                            s += int(st)  
                    st = ""
                    l = -1
            if r == len(curr) - 1:
                sym_flag = self.check_left(l, curr, i, st)
                if not sym_flag:
                    sym_flag = self.check_mid(l, r, i, st)
                
                if sym_flag and st:
                    s += int(st)
        return s
    
    def partTwo(self):
        s = 0
        for item in self.HASH.values():
            if len(item) == 2:
                s += (item[0] * item[1])
        return s

if __name__ == "__main__":
    parser = Parser(FILE)
    print(*parser.RESULT, sep="\n")