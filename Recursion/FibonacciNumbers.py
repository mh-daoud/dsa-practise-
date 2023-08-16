def fibonacciNumbers(index) : 
        assert index >= 0 and index == int(index), "please enter a positive integer"
        if (index == 0 or index == 1) : 
            return index
        return fibonacciNumbers(index - 1) + fibonacciNumbers(index -2);


print(fibonacciNumbers(5))