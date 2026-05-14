def f1():
    try:
        print("Inside try...")
        #print(10/0)
        return 100
    except Exception as e:
        print("Excption caught...")    
        return 200
    finally:
        return 300

print(f1())