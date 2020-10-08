def get_account_info(accounts, account_name: str):
    for account in accounts:
        if account["account"] == account_name:
            return account

def check_for_pass(accounts, password: str):
    for pw in accounts:
        if pw["password"] == password:
            return True

def check_for_account(accounts, account_name: str):
    for account in accounts:
        if account["account"] ==  account_name:
            return False
        else:
            return True