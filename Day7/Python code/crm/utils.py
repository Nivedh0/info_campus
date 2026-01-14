def validate_id(cid):
    cid = int(cid)
    return cid > 0

def validate_email(email):
    return "@" in email and email.endswith(".com")

def vaidate_status(status):
    sta=["lead","customer","client"]
    if status in sta:
        return True
    else:
        return False