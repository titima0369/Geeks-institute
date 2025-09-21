const fromCurrency = document.getElementById("fromCurrency");
const toCurrency = document.getElementById("toCurrency");
const amountInput = document.getElementById("amount");
const convertBtn = document.getElementById("convertBtn");
const switchBtn = document.getElementById("switchBtn");
const resultDiv = document.getElementById("result");

const API_KEY = "YOUR_API_KEY_HERE"; 
const BASE_URL = "https://v6.exchangerate-api.com/v6";

async function getCurrencies() {
  try {
    const response = await fetch(`${BASE_URL}/${API_KEY}/codes`);
    if (!response.ok) throw new Error("Network response was not ok");

    const data = await response.json();
    const codes = data.supported_codes;

    codes.forEach(code => {
      const option1 = document.createElement("option");
      option1.value = code[0];
      option1.textContent = `${code[0]} - ${code[1]}`;
      fromCurrency.appendChild(option1);

      const option2 = document.createElement("option");
      option2.value = code[0];
      option2.textContent = `${code[0]} - ${code[1]}`;
      toCurrency.appendChild(option2);
    });

    fromCurrency.value = "USD";
    toCurrency.value = "EUR";
  } catch (error) {
    console.error("Error fetching currencies:", error);
  }
}

async function convertCurrency() {
  const from = fromCurrency.value;
  const to = toCurrency.value;
  const amount = parseFloat(amountInput.value);

  try {
    const response = await fetch(`${BASE_URL}/${API_KEY}/pair/${from}/${to}/${amount}`);
    if (!response.ok) throw new Error("Network response was not ok");

    const data = await response.json();
    resultDiv.textContent = `${amount} ${from} = ${data.conversion_result.toFixed(2)} ${to}`;
  } catch (error) {
    resultDiv.textContent = " Error converting currency.";
    console.error(error);
  }
}

function switchCurrencies() {
  const temp = fromCurrency.value;
  fromCurrency.value = toCurrency.value;
  toCurrency.value = temp;
  convertCurrency();
}

convertBtn.addEventListener("click", convertCurrency);
switchBtn.addEventListener("click", switchCurrencies);

getCurrencies();
