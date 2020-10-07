def get_account_info(accounts, account_name: str):
    for account in accounts:
        if account["account"] == account_name:
            return account