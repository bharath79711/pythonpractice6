def fun_app(file):
    try:
        with open(file,'a') as obj:
            data = obj.write("\n iam fine\n just reach now")
        return data
    except Exception as error:
        print("error is:",error)
x= fun_app("ab.txt")
print(x)
