from jnius import autoclass


def is_jnull(obj):
    Objects = autoclass("java.util.Objects")
    return Objects.isNull(obj)


def uri_parse(url):
    Uri = autoclass('android.net.Uri')
    return Uri.parse(url)