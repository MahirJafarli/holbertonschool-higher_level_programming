#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    """
    Divides element by element two lists.

    Args:
        my_list_1: The first list.
        my_list_2: The second list.
        list_length: The number of elements to process.

    Returns:
        A new list of length list_length containing the division results.
    """
    new_list = []
    for i in range(list_length):
        div_result = 0
        try:
            val_1 = my_list_1[i]
            val_2 = my_list_2[i]
            div_result = val_1 / val_2
        except TypeError:
            print("wrong type")
        except ZeroDivisionError:
            print("division by 0")
        except IndexError:
            print("out of range")
        finally:
            new_list.append(div_result)
    return new_list
