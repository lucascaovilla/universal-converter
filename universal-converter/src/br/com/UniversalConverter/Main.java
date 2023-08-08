package br.com.UniversalConverter;

import javax.swing.JOptionPane;

public class Main {
	public static void main(String[] args) {
		boolean execute = true;
		while (execute) {
			Object[] options = { "Currencies", "Temperature" };
			String converter = JOptionPane.showInputDialog(null, "Choose your converter", "Main Menu",
					JOptionPane.INFORMATION_MESSAGE, null, options, options[0]).toString();

			switch (converter) {
			case "Currencies":
				currenciesConverter();
				break;
			case "Temperature":
				temperatureConverter();
				break;

			}

			int decision = JOptionPane.showConfirmDialog(null, "Would you like to do another convertion?");

			switch (decision) {
			case 1:
				execute = false;
				JOptionPane.showMessageDialog(null, "Program finished!");
				break;
			default:
				execute = true;
			}

		}
	}

	public static boolean verify(String input) {
		try {
			double value = Double.parseDouble(input);
			if (value >= 0 || value < 0)
				;
			return true;
		} catch (NumberFormatException e) {
			return false;
		}

	}

	private static void currenciesConverter() {
		String currencyInput = JOptionPane.showInputDialog("Insert a value: ");
		if (!verify(currencyInput)) {
			JOptionPane.showMessageDialog(null, "Invalid input! Try again with a numeral value.");
		} else {
			String[] currencies = { "Real", "Dollar", "Euro", "Argentinian Peso" };
			double value = Double.parseDouble(currencyInput);
			String currentCurrency = (String) JOptionPane.showInputDialog(null, "Choose your current Currency",
					"Operation selection", JOptionPane.QUESTION_MESSAGE, null, currencies, currencies[0]);
			String toConvertToCurrency = (String) JOptionPane.showInputDialog(null, "Choose the currency to convert to",
					"Operation selection", JOptionPane.QUESTION_MESSAGE, null, currencies, currencies[0]);
			double convertedValue = CurrencyConverter.convert(value, currentCurrency, toConvertToCurrency);
			JOptionPane.showMessageDialog(null, "The value of " + value + " " + currentCurrency + " is "
					+ convertedValue + " " + toConvertToCurrency);
		}
	}

	private static void temperatureConverter() {
		String temperatureInput = JOptionPane.showInputDialog("Insert a value: ");
		if (!verify(temperatureInput)) {
			JOptionPane.showMessageDialog(null, "Invalid input! Try again with a numeral value.");
		} else {
			String[] temperautreUnits = { "Celsius", "Fahrenheit", "Kelvin" };
			double value = Double.parseDouble(temperatureInput);
			String currentTemperatureUnit = (String) JOptionPane.showInputDialog(null,
					"Choose your current Temperature Unit", "Operation selection", JOptionPane.QUESTION_MESSAGE, null,
					temperautreUnits, temperautreUnits[0]);
			String toConvertToTempreatureUnit = (String) JOptionPane.showInputDialog(null,
					"Choose the Temperature Unit to convert to", "Operation selection", JOptionPane.QUESTION_MESSAGE,
					null, temperautreUnits, temperautreUnits[0]);
			double convertedValue = TemperatureConverter.convert(value, currentTemperatureUnit,
					toConvertToTempreatureUnit);
			JOptionPane.showMessageDialog(null, "The value of " + value + " " + currentTemperatureUnit + " is "
					+ convertedValue + " " + toConvertToTempreatureUnit);
		}
	}
}
