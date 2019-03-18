from dump1 import dump

@dump
def double(*args, **kwargs):
    "Double every argument"
    output_list = [ arg * 2 for arg in args ]
    output_dict  = { k:2*v for k,v in kwargs.items() }
    return output_list, output_dict

if __name__ == "__main__":
    output = double(3, 5, first=100, next=98.6, last=-40)

                         
