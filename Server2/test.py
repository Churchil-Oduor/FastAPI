def get_user_details(firstname, lastname):
    return firstname.title() + " " + lastname.title()


def get_name_with_age(name: str, age: int):
    name_with_age = name + " aged: " +  str(age)
    return name_with_age

def info():
    return 3, "hello"

f_name = "churhcil"
l_name = "okech"
age = 24


fullname = get_user_details(f_name, l_name)
details = get_name_with_age(f_name, age)


