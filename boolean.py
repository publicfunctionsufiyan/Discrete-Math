import random


def checkNegation(string):
    if '~' in string:
        s = string.replace("~", "not ")
        return " " + s + " "
    else:
        s = " " + string + " "
        return string


def checkImplication(string):
    a_string = string[:0] + 'not ' + string[0:]
    b_string = a_string.replace('->', 'or ')
    return " " + b_string + " "


def checkDisjunction(string):
    a_string = string.replace('\/', 'or')
    return " " + a_string + " "


def someStuff(text):
    clause = text.split('/\ ')
    clauses = []
    afterneg = []
    whole_text = str()
    for i in clause:
        if i.startswith("("):
            ind1 = i.find('(')
            ind2 = i.find(')')
            clauses.append(i[ind1 + 1:ind2])
        else:
            clauses.append(i)
    for j in clauses:
        checked_negation = checkNegation(j)
        afterneg.append(checked_negation)

    result = []
    for k in afterneg:
        if "->" in k:
            result.append(checkImplication(k))
        elif "\/" in k:
            result.append(checkDisjunction(k))
        else:
            result.append(" " + k)

    return result


def generate_dict(text):
    s = set()
    d = dict()
    list_of_dicts = list()
    for character in text:
        is_letter = character.isalpha()
        if is_letter:
            s.add(character)
            ls = len(s)
            listt = list(s)
    for i in range(pow(2, ls)):
        for j in range(ls):
            d[listt[j]] = bool(random.getrandbits(1))
        list_of_dicts.append(dict(d))
    return list_of_dicts


def is_satisfiable(cnf):
    phrases = someStuff(cnf)
    list_of_dicts = generate_dict(cnf)
    for dict_order in list_of_dicts:
        fl = True
        for phrase in phrases:
            for key in dict_order.keys():
                if " {} ".format(key) in phrase:
                    phrase = phrase.replace(" {} ".format(key), ' dict_order["{}"] '.format(key))
            result = eval(phrase)
            if not result:
                fl = False
                break
        if fl:
            return True
    return False


def sat_assignment(cnf):
    phrases = someStuff(cnf)
    list_of_dicts = generate_dict(cnf)
    for dict_order in list_of_dicts:
        fl = True
        for phrase in phrases:
            for key in dict_order.keys():
                if " {} ".format(key) in phrase:
                    phrase = phrase.replace(" {} ".format(key), ' dict_order["{}"] '.format(key))
            result = eval(phrase)
            if not result:
                fl = False
                break
        if fl:
            return dict_order

