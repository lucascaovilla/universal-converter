package br.com.UniversalConverter;

public class TemperatureConverter {
	public static double convert(double value, String currentTemperatureUnit, String toConvertToTemperatureUnit) {
		switch (currentTemperatureUnit) {
		case "Celsius":
			if (toConvertToTemperatureUnit == "Kelvin") {
				return celsiusToKelvin(value);
			} else {
				return celsiusToFahrenheit(value);
			}
		case "Kelvin":
			if (toConvertToTemperatureUnit == "Celsius") {
				return kelvinToCelsius(value);
			} else {
				return kelvinToFahrenheit(value);
			}
		case "Fahrenheit":
			if (toConvertToTemperatureUnit == "Celsius") {
				return fahrenheitToCelsius(value);
			} else {
				return fahrenheitToKelvin(value);
			}
		default:
			return 00.0;
		}

	}

	private static double celsiusToFahrenheit(double celsius) {
		return (celsius * 9 / 5) + 32;
	}

	private static double fahrenheitToCelsius(double fahrenheit) {
		return (fahrenheit - 32) * 5 / 9;
	}

	private static double celsiusToKelvin(double celsius) {
		return celsius + 273.15;
	}

	private static double kelvinToCelsius(double kelvin) {
		return kelvin - 273.15;
	}

	private static double kelvinToFahrenheit(double kelvin) {
		return celsiusToFahrenheit(kelvinToCelsius(kelvin));
	}

	private static double fahrenheitToKelvin(double fahrenheit) {
		return fahrenheitToCelsius(celsiusToKelvin(fahrenheit));
	}
}
