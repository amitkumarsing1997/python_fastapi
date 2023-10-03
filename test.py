
class Test:
    def reverse(self, x: int) -> int:
        ans = 0
        min_range = -2**31
        max_range = 2**31 - 1  
        
        if x>0:
             while x != 0:
              print(x)
              digit = x % 10
              print("digit",digit)
              if ans > max_range // 10 or ans < min_range // 10:
                 return 0
              ans = ans * 10 + digit
              x = x // 10       
              return ans
        elif x<0:
            x=x*(-1)
            while x != 0:
             print(x)
             digit = x % 10
             print("digit",digit)
             if ans > max_range // 10 or ans < min_range // 10:
                return 0
             ans = ans * 10 + digit
             x = x // 10       
             return ans*(-1)
           
    
test_instance = Test()

# Call the reverse method with an integer argument and print the result
input_number = -123  # Replace this with the integer you want to reverse
result = test_instance.reverse(input_number)
print("Reversed:", result)

print("hello amit")