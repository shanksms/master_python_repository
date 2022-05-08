from enum import Enum, auto


class EmployeeType(Enum):
    """
    auto assigns auto incrementing numbers
    """
    VICE_PRESIDENT= auto()
    ASSOCIATE = auto()


if __name__ == '__main__':
   print(EmployeeType.VICE_PRESIDENT.name, EmployeeType.VICE_PRESIDENT.value)
   for emp_type in EmployeeType:
       print(emp_type.name, emp_type.value)