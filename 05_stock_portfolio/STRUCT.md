class Portfolio
    methods:
        do_transaction(Transaction)
        add(Company, count, operation_date)
        remove(Company, count, operation_date)
        print(PriceProvider, Formatter)

class PriceProvider
    get_current_price(Company): Dollar

class Company // оборачивает имя компании

class Dollar // оборачивает деньши

class Transaction
    Company
    count
    transaction_date
    transaction_type: ADD | REMOVE
