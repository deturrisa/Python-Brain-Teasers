def round_decimals_down(number: float, decimals: int = 2):
    """
    Returns a value rounded down to a specific number of decimal places.
    """
    import math

    if not isinstance(decimals, int):
        raise TypeError("decimal places must be an integer")
    elif decimals < 0:
        raise ValueError("decimal places has to be 0 or more")
    elif decimals == 0:
        return math.floor(number)
    factor = 10 ** decimals
    return math.floor(number * factor) / factor

def cash_reg(customer_money, item_price):
    from decimal import Decimal, getcontext
    getcontext().prec = 3

    uk_money_dic = {
        5000: 'fifty pound',
        2000: 'twenty pound',
        1000: 'ten pound',
        500: 'five pound',
        200: 'two pound',
        100: 'one pound',
        50: 'fifty pence',
        20: 'twenty pence',
        10: 'ten pence',
        5: 'five pence',
        2: 'two pence',
        1: 'one pence'
    }

    uk_money_list = list(uk_money_dic.keys())

    output = ''
    change = int(customer_money*100) - int(round(item_price*100,2))
    # print(int(customer_money*100))
    # print((item_price*100))
    # print('Total change to give out is %s' % change)

    for uk_money in uk_money_list:
        change = round(change,2)
        # print('uk money :' + str(uk_money))
        # print('     Change to give: ' + str(change))

        times_uk_money_in_change = int(change / uk_money)
        # print('     number of uk_money in change : ' + str(times_uk_money_in_change))

        f = str(change)
        # print ('    number of decimal places in change: '+ str(f[::-1].find('.')))

        if times_uk_money_in_change >= 1:
            change = float(Decimal(change) - (Decimal(uk_money) * times_uk_money_in_change))
            # print('     take change away by %s' % uk_money * times_uk_money_in_change)
            output += str(times_uk_money_in_change) + ' ' + str(uk_money_dic.get(uk_money)) + ', '
        else:
            pass

    print(output)