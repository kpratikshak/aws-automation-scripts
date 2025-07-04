import random

s_char = "abcdefghijklmnopqrstuvwxyz"
b_char = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
d_char = "123456789"

class Otp:
    def __init__(self,len):
        self.len = len
        
    @property 
    def digits(self):
        num = 0
        result = []
        while num < self.len:
            rand_choice