from crm.utils import validate_id,validate_email,vaidate_status

class Customer:
    def __init__(self, cid, name, email, status):
        self.cid = cid
        self.name = name
        self.email = email
        self.status = status

    def is_valid(self):
        if not validate_id(self.cid):
            print("Invalid ID")
            return False
        if not validate_email(self.email):
            print("Invalid Email")
            return False
        if not vaidate_status(self.status):
            print("Invalid Status")
            return False
        return True

    def display(self):
        print("ID:", self.cid)
        print("Name:", self.name)
        print("Email:", self.email)
        print("Status:", self.status)
