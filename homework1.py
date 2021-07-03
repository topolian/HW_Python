def parse(link_str) -> dict:
    if "?" not in link_str:
        result = {}
    else:
        indx = link_str.find("?")
        new_str = link_str[indx + 1:]
        list1 = new_str.split("&")
        if "" in list1:
            list1.remove("")
        list2 = []
        for item in list1:
            list2.append(item.split("="))
        result = dict(list2)
    return result


if __name__ == '__main__':
    assert parse('https://example.com/path/to/page?name=ferret&color=purple') == {'name': 'ferret', 'color': 'purple'}
    assert parse('https://example.com/path/to/page?name=ferret&color=purple&') == {'name': 'ferret', 'color': 'purple'}
    assert parse('http://example.com/') == {}
    assert parse('http://example.com/?') == {}
    assert parse('http://example.com/?name=Dima') == {'name': 'Dima'}


def parse_cookie(text) -> dict:
    list1 = text.split(";")
    list1.remove("")
    list2 = []
    for item in list1:
        list2.append(item.split("=", 1))
    return dict(list2)


if __name__ == '__main__':
    assert parse_cookie('name=Dima;') == {'name': 'Dima'}
    assert parse_cookie('') == {}
    assert parse_cookie('name=Dima;age=28;') == {'name': 'Dima', 'age': '28'}
    assert parse_cookie('name=Dima=User;age=28;') == {'name': 'Dima=User', 'age': '28'}
