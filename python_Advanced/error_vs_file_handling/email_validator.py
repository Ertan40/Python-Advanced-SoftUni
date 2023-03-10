class NameTooShort(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass

class InvalidDomainError(Exception):
    pass


email = input()
while email != 'End':
    name = email[:email.find('@')]
    domain = email[email.find('.'):]

    if len(name) < 4:
        raise NameTooShort("Name must be more than 4 characters")

    elif domain not in ['.com', '.bg', '.org', '.net']:
        raise InvalidDomainError("Domain must be one of the folowing: .com, .bg, .org, .net")

    else:
        if email.find('@') < 0:
            raise MustContainAtSymbolError("Email must contain @")
        else:
            print('Email is valid')

    email = input()