class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        arr1 = []
        for i in range(1,n+1):
            if i % 3 == 0 and i % 5 == 0:
                arr1.append("FizzBuzz")
                continue
            elif i % 5 == 0:
                arr1.append("Buzz")
                continue
            elif i % 3 == 0:  
                arr1.append("Fizz")  
            else:
                arr1.append(f"{i}")  
        return arr1        

        