from data import ProductSale


class SalesDataProcessor:
    """
    Class to process sales data.

    This class calculates the revenue for each product,
    sorts the products by revenue (descending order),
    and computes the total revenue.
    """
    def __init__(self, sales_data: dict):
        """
        Initialize with the raw sales data.

        Args:
            sales_data (dict): Dictionary with product names as keys and a dict of 
                               quantity and price as values.
        """
        self.sales_data = sales_data
        self.sorted_data = []
        self.total_revenue = 0

    def process_data(self):
        """
        Process the sales data to calculate revenue and sort the data.

        Returns:
            tuple: A tuple containing:
                - sorted_data (list of dict): List of dictionaries with keys
                  'product', 'quantity', 'price', and 'revenue', sorted in descending order by revenue.
                - total_revenue (float): Total revenue from all products.
        """
        data_list = []
        total = 0

        product_items = self.sales_data.items()

        for product, info in self.sales_data.items():
            try:
                quantity = info.get("quantity", 0)
                price = info.get("price", 0)
                revenue = quantity * price
            except Exception as e:
                print(f"Error processing product '{product}': {e}")
                continue

            sale = ProductSale(
                product=product,
                quantity=quantity,
                price=price,
                revenue=revenue
            )
            data_list.append(sale)
            total += revenue

        self.sorted_data = sorted(data_list, key=lambda sale: sale.revenue, reverse=True)
        self.total_revenue = total

        return self.sorted_data, self.total_revenue