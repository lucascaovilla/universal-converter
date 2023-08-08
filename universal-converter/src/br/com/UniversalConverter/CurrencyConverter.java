package br.com.UniversalConverter;

public class CurrencyConverter {
	public static double convert(double value, String currentCurrency, String toConvertToCurrency) {

		double realToDollar = 0.2;
		double realToEuro = 0.19;
		double realToArgentinianPeso = 57.79;

		switch (currentCurrency) {
		case "Dollar":
			value = value / realToDollar;
			break;
		case "Euro":
			value = value / realToEuro;
			break;
		case "Argentinian Peso":
			value = value / realToArgentinianPeso;
			break;
		default:
			break;
		}

		switch (toConvertToCurrency) {
		case "Dollar":
			return value * realToDollar;
		case "Euro":
			return value * realToEuro;
		case "Argentinian Peso":
			return value * realToArgentinianPeso;
		default:
			return value;
		}

	}

}
