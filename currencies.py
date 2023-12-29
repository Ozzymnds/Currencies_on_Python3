import tkinter as tk

class GUI(tk.Tk):
    def __init__(self):
        # Initialize the main GUI window
        tk.Tk.__init__(self)

        # Basic properties
        self.title("Currency Converter")

        # List available currencies
        self.currencies = ["GBP", "USD", "EUR", "INR", "JPY", "CAD", "AUD", "CHF", "CNY", "SEK", "NZD", "BRL", "ZAR"]

        # List conversion rates for February 2, 2022
        self.conversion_rates = dict(zip(self.currencies, [1.36, 1.00, 1.13, 0.014, 0.0092, 0.78, 0.74, 1.10, 0.16, 0.12, 0.69, 0.18, 0.067]))

        # Register the method to handle user input
        self.handle_input = self.register(self._handle_input)

        # Configure the interface
        self.setup()

    def convert_currency(self, event, n=None):
        # Method to convert the entered amount to the output currency

        # If a specific value is not provided, use the value from the input variable
        if n is None:
            n = self.input_amount_var.get()

        # Calculate the conversion rate using the selected currency ratios
        rate = (self.conversion_rates[self.output_currency_var.get()]) / self.conversion_rates[self.input_currency_var.get()]

        # Calculate the output amount and round it to 2 decimals
        self.output_amount_var.set(round(float(n) * rate, 2))

    def _handle_input(self, n):
        # Method to handle user input and validate it

        # Check if the input is a valid decimal number or is empty
        if n.replace(".", "").isdigit() and n.count(".") < 2 or n == "":
            # If it's valid, perform the conversion
            if n != "":
                self.convert_currency(None, n)
            else:
                self.convert_currency(None, "0")

            return True

        return False
    
    def setup(self):
        # Configure interface elements and their associated variables

        self.input_currency_var = tk.StringVar()
        self.input_currency_var.set("GBP")

        self.output_currency_var = tk.StringVar()
        self.output_currency_var.set("EUR")
        
        self.input_amount_var = tk.StringVar()
        self.input_amount_var.set("")

        self.output_amount_var = tk.StringVar()
        self.output_amount_var.set("")

        # Input box for the amount to convert
        input_currency_box = tk.Entry(self, textvariable=self.input_amount_var)
        input_currency_box.config(validate="key", validatecommand=(self.handle_input, "%P"))
        input_currency_box.pack(side=tk.LEFT, padx=5, pady=5, expand=True, fill=tk.X)

        # Dropdown menu to select the input currency
        input_currency_menu = tk.OptionMenu(self, self.input_currency_var, *self.currencies, command=self.convert_currency)
        input_currency_menu.pack(side=tk.LEFT, padx=5, pady=5)

        # Output box to display the conversion result
        output_currency_box = tk.Entry(self, textvariable=self.output_amount_var)
        output_currency_box.config(validate="key", validatecommand=(self.handle_input, "%P"))
        output_currency_box.pack(side=tk.LEFT, padx=5, pady=5, expand=True, fill=tk.X)

        # Dropdown menu to select the output currency
        output_currency_menu = tk.OptionMenu(self, self.output_currency_var, *self.currencies, command=self.convert_currency)
        output_currency_menu.pack(side=tk.LEFT, padx=5, pady=5)

        # Set column weights for responsiveness
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)

# Create an instance of the GUI class and run the main interface loop
gui = GUI().mainloop()
