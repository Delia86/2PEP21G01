# unittest



def my_area_function(lenght:int,width:int):
    if type(lenght) not in (int, float) or type(width) not in (int, float):
        raise TypeError
    if lenght< 0 or width<0:
        raise ValueError
    return lenght* width