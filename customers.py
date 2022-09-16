"""Customers at Hackbright."""


class Customer:
    """Ubermelon customer."""

    def __init__(self, first_name, last_name, email, password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password

    def __repr__(self):
        """Convenience method to show information about melon in console."""

        return (
            f"<Customer: {self.first_name}, {self.last_name}, {self.email}, {self.password}>"
        )

def read_customer_from_file(filepath):


    customer_names = {}

    with open(filepath) as file:
        for line in file:
            (
                first_name,
                last_name,
                email,
                password
            ) = line.strip().split("|")


            customer_names[email] = Customer(
                first_name,
                last_name,
                email,
                password
            )

    return customer_names

def get_all_customers():

    return customer_names


# print(get_all_customers())

def get_by_email(email):


    return customer_names.get(email)


customer_names = read_customer_from_file("customers.txt")