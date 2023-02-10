def data_types(random_input):
    integer_type = 0
    float_type = 0
    string_type = ""
    result = ""

    if input_type == "int":
        integer_type = int(input())
        result = integer_type * 2
    elif input_type == "real":
        float_type = float(input())
        result = f"{float_type * 1.50:.2f}"
    elif input_type == "string":
        string_type = str(input())
        result = f"${string_type}$"
    return result


input_type = input()

print(data_types(input_type))
