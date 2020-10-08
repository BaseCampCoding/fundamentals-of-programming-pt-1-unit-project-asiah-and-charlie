def get_account(accounts, account_name: str):
    for account in accounts:
        if accounts["account"] == account_name:
            return account