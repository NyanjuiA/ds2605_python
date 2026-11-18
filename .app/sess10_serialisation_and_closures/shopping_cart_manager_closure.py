
"""
Shopping Basket Manager Using Python Closures.

This program demonstrates how Python closures can maintain
independent shopping totals for multiple customers.

Each customer receives a dedicated shopping basket function
that remembers their accumulated spending.

The programme demonstrates:
    1. Nested functions.
    2. Variable scope and closures.
    3. The nonlocal keyword.
    4. State management without global variables.
    5. Independent state for multiple customers.

Author: Nyanjui
"""


def create_shopping_basket(customer_name):
    """
    Create an independent shopping basket for a customer.

    The enclosing function maintains the customer's shopping
    total. The nested function can access and modify this total
    using the nonlocal keyword.

    Args:
        customer_name (str): The name of the customer.

    Returns:
        function: A closure that manages the customer's basket.
    """
    shopping_total = 0.0

    def manage_basket(product_name, price):
        """
        Add a product to the basket and update the running total.

        The function remembers the shopping_total variable
        from its enclosing scope, even after the outer function
        has finished executing.

        Args:
            product_name (str): The name of the purchased product.
            price (float): The price of the product.

        Returns:
            str: A summary of the purchase and current basket total.

        Raises:
            ValueError: If the product price is negative or zero.
        """
        nonlocal shopping_total

        if price <= 0:
            raise ValueError(
                "The product price must be greater than zero."
            )

        shopping_total += price

        return (
            f"{customer_name} purchased {product_name} "
            f"for KES {price:,.2f}. "
            f"Current basket total: KES {shopping_total:,.2f}"
        )

    return manage_basket


def main():
    """
    Demonstrate independent shopping baskets for four customers.

    Each customer has a separate closure, ensuring that their
    shopping totals do not interfere with one another.
    """

    # Create four independent shopping baskets.
    shopper_1 = create_shopping_basket("Amina")
    shopper_2 = create_shopping_basket("Kimani")
    shopper_3 = create_shopping_basket("Veronica")
    shopper_4 = create_shopping_basket("David")

    print("=" * 65)
    print("          ONLINE SHOPPING BASKET MANAGER")
    print("=" * 65)

    # Amina's purchases.
    print("\n--- Amina's Shopping Basket ---")
    print(shopper_1("Laptop", 85000.00))
    print(shopper_1("Wireless Mouse", 2500.00))
    print(shopper_1("Laptop Bag", 3500.00))

    # Kimani's purchases.
    print("\n--- Kimani's Shopping Basket ---")
    print(shopper_2("Smartphone", 45000.00))
    print(shopper_2("Headphones", 5000.00))

    # Veronica's purchases.
    print("\n--- Veronica's Shopping Basket ---")
    print(shopper_3("Office Chair", 18000.00))
    print(shopper_3("Desk Lamp", 2500.00))
    print(shopper_3("Notebook", 500.00))

    # David's purchases.
    print("\n--- David's Shopping Basket ---")
    print(shopper_4("Television", 65000.00))
    print(shopper_4("Soundbar", 12000.00))
    print(shopper_4("HDMI Cable", 1500.00))

    print("\n" + "=" * 65)
    print("Each shopper has maintained an independent shopping total.")
    print("=" * 65)


if __name__ == "__main__":
    main()
