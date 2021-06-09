class C32():

    S0 = 'A'

    def add(self):
        if self.S0 == 'A':
            self.S0 = 'B'
            return 0
        elif self.S0 == 'F':
            self.S0 = 'B'
            return 8
        elif self.S0 == 'G':
            self.S0 = 'B'
            return 10
        elif self.S0 == 'D':
            self.S0 = 'E'
            return 4
        elif self.S0 == 'C':
            self.S0 = 'C'
            return 3
        else:
            return None

    def warp(self):
        if self.S0 == 'B':
            self.S0 = 'C'
            return 1
        elif self.S0 == 'F':
            self.S0 = 'G'
            return 7
        elif self.S0 == 'G':
            self.S0 = 'C'
            return 11
        elif self.S0 == 'C':
            self.S0 = 'D'
            return 2
        elif self.S0 == 'E':
            self.S0 = 'F'
            return 6
        else:
            return None

    def turn(self):
        if self.S0 == 'D':
            self.S0 = 'D'
            return 5
        elif self.S0 == 'G':
            self.S0 = 'H'
            return 9
        else:
            return None