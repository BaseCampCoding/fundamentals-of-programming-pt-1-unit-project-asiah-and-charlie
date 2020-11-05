



def check_for_pass(cur, password: str):
    cur.execute(""" SELECT * FROM passwords WHERE Password = ? """, (password,))
    rows = cur.fetchall()
    print(rows)
    return len(rows) > 0

def check_for_account(accounts, account_name: str):
    for account in accounts:
        if account["account"] ==  account_name:
            return False
        else:
            return True