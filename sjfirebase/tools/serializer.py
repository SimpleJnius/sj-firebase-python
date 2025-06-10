from jnius import autoclass


def serialize_map_to_dict(hash_map):
    map_to_dict_data = {}

    for key, value in zip(hash_map, hash_map.values()):
        if hasattr(value, "put"):
            map_to_dict_data[key] = serialize_map_to_dict(value)
        elif hasattr(value, "iterator"):
            map_to_dict_data[key] = serialize_array_to_list(value)
        else:
            map_to_dict_data[key] = value
    return map_to_dict_data


def serialize_array_to_list(array):
    array_to_list_data = []

    for value in array:
        if hasattr(value, "iterator"):
            data = serialize_array_to_list(value)
            array_to_list_data.append(data)
        elif hasattr(value, "put"):
            data = serialize_map_to_dict(value)
            array_to_list_data.append(data)
        else:
            array_to_list_data.append(value)
    return array_to_list_data


def serialize_dict_to_map(dictionary):
    dict_to_map_data = autoclass("java.util.HashMap")()

    for key, value in dictionary.items():
        if isinstance(value, dict):
            data = serialize_dict_to_map(value)
            dict_to_map_data.put(key, data)
        elif isinstance(value, list):
            data = serialize_list_to_array(value)
            dict_to_map_data.put(key, data)
        elif isinstance(value, bool):
            Boolean = autoclass("java.lang.Boolean")
            dict_to_map_data.put(key, Boolean(value))
        elif isinstance(value, int):
            Long = autoclass("java.lang.Long")
            dict_to_map_data.put(key, Long(value))
        elif isinstance(value, float):
            Double = autoclass("java.lang.Double")
            dict_to_map_data.put(key, Double(value))
        elif isinstance(value, str):
            String = autoclass("java.lang.String")
            dict_to_map_data.put(key, String(value))
        else:
            dict_to_map_data.put(key, value)
    return dict_to_map_data


def serialize_list_to_array(list_):
    list_to_array_data = autoclass("java.util.ArrayList")()

    for value in list_:
        if isinstance(value, list):
            data = serialize_list_to_array(value)
            list_to_array_data.add(data)
        elif isinstance(value, dict):
            data = serialize_dict_to_map(value)
            list_to_array_data.add(data)
        elif isinstance(value, bool):
            Boolean = autoclass("java.lang.Boolean")
            list_to_array_data.add(Boolean(value))
        elif isinstance(value, int):
            Long = autoclass("java.lang.Long")
            list_to_array_data.add(Long(value))
        elif isinstance(value, float):
            Double = autoclass("java.lang.Double")
            list_to_array_data.add(Double(value))
        elif isinstance(value, str):
            String = autoclass("java.lang.String")
            list_to_array_data.add(String(value))
        else:
            list_to_array_data.add(value)
    return list_to_array_data


def serialize(data, raw_python=False):
    if raw_python:
        if not isinstance(data, list):
            raise Exception(f"raw `{type(data)}` serialization not supported")
        raw_data = []
        for value in data:
            if isinstance(value, list):
                data = serialize_list_to_array(value)
                raw_data.append(data)
            elif isinstance(value, dict):
                data = serialize_dict_to_map(value)
                raw_data.append(data)
            elif isinstance(value, bool):
                Boolean = autoclass("java.lang.Boolean")
                raw_data.append(Boolean(value))
            elif isinstance(value, int):
                Long = autoclass("java.lang.Long")
                raw_data.append(Long(value))
            elif isinstance(value, float):
                Double = autoclass("java.lang.Double")
                raw_data.append(Double(value))
            elif isinstance(value, str):
                String = autoclass("java.lang.String")
                raw_data.append(String(value))
            else:
                raw_data.append(value)
        return raw_data
    if isinstance(data, dict):
        return serialize_dict_to_map(data)
    if isinstance(data, list):
        return serialize_list_to_array(data)
    if hasattr(data, "iterator"):
        return serialize_array_to_list(data)
    if hasattr(data, "put"):
        return serialize_map_to_dict(data)
    return data


if __name__ == "__main__":
    # Serialize Java map to Python dictionary
    hm = autoclass("java.util.HashMap")()
    hm.put("ada", "kene")
    hm.put("kene", "ada")

    bm = autoclass("java.util.HashMap")()
    bm.put("ken", 1)
    bm.put(2, 3)

    cm = autoclass("java.util.HashMap")()

    ar = autoclass("java.util.ArrayList")()
    ar.add(1)
    ar.add(2)
    ar.add(bm)
    # cm.put("hj", ar)
    #
    # bm.put("extras", cm)
    hm.put("extra", ar)
    print(serialize_map_to_dict(hm))

    # Serialize Java array to Python list
    al = autoclass("java.util.ArrayList")()
    al.add(1)
    al.add("ada")

    dm = autoclass("java.util.HashMap")()
    dm.put("ada", "kene")

    al.add(dm)
    print(serialize_array_to_list(al))

    # Serialize Python dictionary to Java map
    dt = {"ada": "kene", 1: [{"1": "ada"}]}
    print(serialize_dict_to_map(dt).get(1).get(0).get("1"))

    # Serialize Python list to Java Array
    lt = [1, 2, 3, {"ada": "kene"}]
    print(serialize_list_to_array(lt))
