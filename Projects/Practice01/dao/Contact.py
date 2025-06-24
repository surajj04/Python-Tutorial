class Contact:
    def __init__(self, cid, name, phoneNo, email, address):
        self.cid = cid
        self.name = name
        self.phoneNo = phoneNo
        self.email = email
        self.address = address

    def __str__(self):
        return f"Contact[ID={self.cid}, Name={self.name}, Phone={self.phoneNo}, Email={self.email}, Address={self.address}]"
