# **kwargs: id and name are required, everything else goes into `extra` (a regular dict)
def get_product(id: str, name: str, **extra: str) -> dict:
    product = {'id': id, 'name': name}
    product.update(extra)
    return product
