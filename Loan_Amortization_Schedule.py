def get_loan_details():
    """Get loan details from the user."""
    principal = float(input("Enter the loan amount (principal): "))
    annual_interest_rate = float(input("Enter the annual interest rate (in %): "))
    term_years = int(input("Enter the loan term (in years): "))
    payments_per_year = int(input("Enter the number of payments per year: "))
    return principal, annual_interest_rate, term_years, payments_per_year

def calculate_monthly_rate(annual_interest_rate, payments_per_year):
    """Calculate the monthly interest rate."""
    return annual_interest_rate / 100 / payments_per_year

def calculate_total_payments(term_years, payments_per_year):
    """Calculate the total number of payments."""
    return term_years * payments_per_year

def calculate_fixed_payment(principal, monthly_rate, total_payments):
    """Calculate the fixed payment amount using the amortization formula."""
    return principal * (monthly_rate * (1 + monthly_rate) ** total_payments) / ((1 + monthly_rate) ** total_payments - 1)

def generate_amortization_schedule(principal, monthly_rate, fixed_payment, total_payments):
    """Generate the loan amortization schedule."""
    schedule = []
    remaining_balance = principal

    for payment_number in range(1, total_payments + 1):
        interest_payment = remaining_balance * monthly_rate
        principal_payment = fixed_payment - interest_payment
        remaining_balance -= principal_payment
        schedule.append((payment_number, interest_payment, principal_payment, remaining_balance))

    return schedule

def display_amortization_schedule(schedule):
    """Display the amortization schedule."""
    print(f"{'Payment #':<10}{'Interest':<15}{'Principal':<15}{'Remaining Balance':<20}")
    for payment in schedule:
        print(f"{payment[0]:<10}{payment[1]:<15.2f}{payment[2]:<15.2f}{payment[3]:<20.2f}")

def calculate_total_interest(schedule):
    """Calculate the total interest paid over the loan term."""
    total_interest = sum(payment[1] for payment in schedule)
    return total_interest

def simulate_extra_payments(schedule, extra_payment):
    """Simulate the effect of making extra payments on the loan."""
    for i, payment in enumerate(schedule):
        payment_number, interest_payment, principal_payment, remaining_balance = payment
        new_principal_payment = principal_payment + extra_payment
        new_remaining_balance = remaining_balance - extra_payment
        schedule[i] = (payment_number, interest_payment, new_principal_payment, new_remaining_balance)
        if new_remaining_balance <= 0:
            schedule = schedule[:i+1]
            break
    return schedule

def main():
    print("Welcome to the Loan Amortization Schedule Calculator!")

    # Step 1: Get loan details from the user
    principal, annual_interest_rate, term_years, payments_per_year = get_loan_details()

    # Step 2: Calculate basic parameters
    monthly_rate = calculate_monthly_rate(annual_interest_rate, payments_per_year)
    total_payments = calculate_total_payments(term_years, payments_per_year)
    fixed_payment = calculate_fixed_payment(principal, monthly_rate, total_payments)

    # Step 3: Generate the amortization schedule
    schedule = generate_amortization_schedule(principal, monthly_rate, fixed_payment, total_payments)

    # Step 4: Display the amortization schedule
    display_amortization_schedule(schedule)

    # Step 5: Calculate and display the total interest paid
    total_interest = calculate_total_interest(schedule)
    print(f"\nTotal interest paid over the term of the loan: ${total_interest:.2f}")

    # Step 6: Simulate extra payments (optional)
    extra_payment = float(input("\nEnter an extra payment amount (enter 0 to skip): "))
    if extra_payment > 0:
        new_schedule = simulate_extra_payments(schedule, extra_payment)
        print("\nAmortization Schedule with Extra Payments:")
        display_amortization_schedule(new_schedule)

        new_total_interest = calculate_total_interest(new_schedule)
        print(f"\nTotal interest paid with extra payments: ${new_total_interest:.2f}")
        print(f"Interest savings: ${total_interest - new_total_interest:.2f}")

    # Return values for potential further use
    return schedule, total_interest

if __name__ == "__main__":
    schedule, total_interest = main()
