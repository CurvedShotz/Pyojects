#test

import customtkinter as ctk
import unittest
from tkinter import Tk


class TestCalculatorApp(unittest.TestCase):

    def setUp(self):
        """Setup the GUI environment for each test."""
        self.root = Tk()
        self.root.geometry("500x500")
        self.root.update()

        global display_widget
        display_widget = ctk.CTkTextbox(self.root, width=300, height=50, corner_radius=5, fg_color="grey")
        display_widget.grid(rowspan=5, padx=10, pady=10)

    def tearDown(self):
        """Destroy the GUI after each test."""
        self.root.destroy()

    def test_update_calculation(self):
        """Test if buttons update the calculation properly."""
        global calculation
        calculation = ""
        update_calculation('5')
        self.assertEqual(display_widget.get("1.0", ctk.END).strip(), '5')

    def test_evaluate_calculation(self):
        """Test if calculation is evaluated correctly."""
        display_widget.insert(ctk.END, '2+3')
        evaluate_calculation()
        self.assertEqual(display_widget.get("1.0", ctk.END).strip(), '5')

    def test_clear_screen(self):
        """Test if clear screen works."""
        display_widget.insert(ctk.END, '123')
        clear_screen()
        self.assertEqual(display_widget.get("1.0", ctk.END).strip(), '')

if __name__ == "__main__":
    unittest.main()
