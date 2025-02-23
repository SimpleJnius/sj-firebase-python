from jnius import autoclass


def is_jnull(obj):
    Objects = autoclass("java.util.Objects")
    return Objects.isNull(obj)
