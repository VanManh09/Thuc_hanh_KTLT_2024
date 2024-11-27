print("Sinh viên Nguyễn Văn Mạnh")
print("Mssv: 23575202161009")

class RomanToInteger:
    def __init__(self, roman):
        self.roman = roman  

    def convert(self):
        roman_numerals = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        total = 0
        prev_value = 0
        
        for char in reversed(self.roman): 
            value = roman_numerals[char]  
            
            if value < prev_value:
                total -= value  
            else:
                total += value  
            
            prev_value = value 

        return total  


roman_number = "MCMXCIV"  
converter = RomanToInteger(roman_number)
print(converter.convert())  
