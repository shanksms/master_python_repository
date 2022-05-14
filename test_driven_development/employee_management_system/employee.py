from dataclasses import dataclass

@dataclass
class Employee:
    name: str
    employee_id: int
    pay_rate: float = 100.00
    hours_worked: float = 0.0
    employer_cost: float = 1000.00
    has_commission: bool = True
    commission: float = 100.00
    contracts_landed: int = 0

    def compute_payout(self) -> float:
        """
        Compute how much employee is paid
        """
        payout = self.pay_rate * self.hours_worked + self.employer_cost
        if self.has_commission:
            payout += self.commission * self.contracts_landed
        return payout


