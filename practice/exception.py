# index error 
lst=[0,1,2,3]
# try:
#     print(lst[4])
# except:
#     print("An error occurred")

# arithmetic error
import sys
def div():
    n1=int(input("Enter First Number "))
    n2=int(input("Enter Second number "))
    
    try:
        print("Divison is ",n1/n2)
    except ArithmeticError:  
        print("hahahahahah")
        div()
    except:
        print("An Error Occurred")
        div()
    else:
       sys.exit(0)
    # finally:
    #      div()  
div()
        

