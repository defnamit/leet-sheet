def checkDivisibility(self, n):
        n_list = list(map(int, str(n)))

        product = 1
        for x in n_list:
            product *= x

        return n % (sum(n_list) + product) == 0
