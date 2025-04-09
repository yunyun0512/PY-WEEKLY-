def perform_integer_division():
    try:
        a,b=map(int,input().split())
        result=a/b
        print(result)
    except ZeroDivisionError:
        print("Error Code:division by zero")
    except ValueError as e:
        print(f"Error Code:{str(e)}")

if __name__=="__main__":
    perform_integer_division()