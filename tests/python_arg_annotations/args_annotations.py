class MyThing:
    pass

def hello(a: int, b: str, c: Optional[MyThing]) -> None:
    pass


def long_annotation(my_long_variable_name_aaaaaaaaaaaaaaaaaaa: MyLongTypeNameAAAAAAAAAAAAAAAAAAAAA) -> None:
    pass


def ellipses(arg:Tuple[str,...])->Optional[Tuple[str,...]]:
    return None


def default_args(verbose: bool=False):
    pass


def annotation_with_long_default(
    my_long_variable_name_aaaaaaaaaaaaaaaaaaa: MyTypeName = my_long_default_value_aa
):
    pass


def long_annotation_with_long_default(
    my_long_variable_name_aaaaaaaaaaaaaaaaaaa:
        MyLongTypeNameAAAAAAAAAAAAAAAAAAAAA = my_long_default_value_aaaaaaaaaaaaaa
):
    pass
