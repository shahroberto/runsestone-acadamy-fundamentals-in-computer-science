"""This is a program."""


class Employee:
    """A sample employee class."""

    def __init__(self, first, last):
        """First and last name attributes."""
        self.first = first
        self.last = last

    def test_method(self):
        """Check what pass does."""
        pass

    @property
    def email(self):
        """Set email."""
        return '{}.{}@gmail.com'.format(self.first, self.last)

    @property
    def fullname(self):
        """Set full name."""
        return '{} {}'.format(self.first, self.last)


a = str(input("What is your first name?\n>"))
emp_1 = Employee(a, 'Smith')
print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)
