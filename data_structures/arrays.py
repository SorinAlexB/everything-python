"""
Python arrasys are homogeneous 
Python lists are heterogeneous

While lists are versatile, they use more memmory because of data types size and padding. Arrays are the best choice when you need to use only one datatype and also when you need to do numerical computations on them (for the second, numpy arrays be better)

Also arrays uses less memmory than lists!
"""
import array as arr

def classifier(t: str) -> str:
    match t:
        case 'i' | 'I' | 'b' | 'B' | 'l' : return 'int'
        case 'f' | 'd' : return 'float'
        case _: raise Exception("Invalid array type!")

def create_arr(t: str ) -> arr.array:
    return arr.array(t, [])

# The arrays does not store pointers like lists. Acts like C arrays with contiguous store in memory.
# inserting on the last position is like using a.append() -> same outcome, different mechanism
def insert_element(a: arr.array, pos: int, e=None) -> arr.array:
    try:
        if e is None:
            raise Exception("Element can't be None!")
        a.insert(pos, e)
    except Exception as e:
        print(f"Unexpected expection {e}")
        raise # for pytest testing
    finally:
        print(f"The current array is {a}")  
    return a

# Extends the array with another one or list
def extend(a: arr.array, b: arr.array) -> arr.array:
    try:
        a.extend(b)
    except Exception as e:
        print(f"Unexpected expection {e}")
    finally:
        print(f"The current array is {a}")
        raise # for pytest testing
    return a

if __name__ == "__main__":
    a = arr.array('i', [1,2])
    a = insert_element(a, 1, 3)
    a = extend(a, [1,2,3])
