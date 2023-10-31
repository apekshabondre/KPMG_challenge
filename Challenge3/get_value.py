def get_value(obj, key):
    if not key:
        return obj    
    keys = key.split('/')
    val = obj
    for k in keys:
        if k in val:
            val = val[k]
        else:
            return None
    return val


if __name__ == "__main__":
    object = {"a":{"b":{"c":"d"}}}
    key = "a/b/c"
    print("The Expected Value: ", get_value(object, key))

    object = {"x":{"y":{"z":"a"}}} 
    key = "x/y/z"
    print("The Expected Value: ", get_value(object, key))
