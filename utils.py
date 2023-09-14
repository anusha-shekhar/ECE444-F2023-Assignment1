class utils:
    def reversed(num):
        # int -> int
        # This function takes in an integer and returns it with its digits reversed
        reversed_num = 0
        while num>0:
            temp = num%10
            reversed_num = reversed_num*10 + temp
            num = num//10 
        return reversed_num

    def formatter(num):
        # int -> int, int
        # This function takes in an integer and returns in in its binary and octal formats
        binary_num = bin(num)
        octal_num = oct(num)
        return binary_num, octal_num