const passwordLengthInput = document.getElementById('password-length');
const savedPasswordLength = sessionStorage.getItem('passwordLength');
const password = document.getElementById('password');
const copyBtn = document.getElementById('copy-btn');
const modal = document.createElement('div');
modal.classList.add('modal');

if (savedPasswordLength) {
    passwordLengthInput.value = savedPasswordLength;
}

passwordLengthInput.addEventListener('change', () => {
    sessionStorage.setItem('passwordLength', passwordLengthInput.value);
});


if (password.textContent.length == 0) {
    copyBtn.style.display = 'none';
} else {
    copyBtn.style.display = 'initial';
}

copyBtn.addEventListener('click', () => {
    const range = document.createRange();
    range.selectNode(password);
    window.getSelection().addRange(range);

    const successful = document.execCommand('copy');
    if (successful) {
        modal.textContent = 'Password copied to clipboard!';
        document.body.appendChild(modal);
        setTimeout(() => {
            modal.remove();
        }, 2000);
    }

    window.getSelection().removeAllRanges();
});

const numbersCheckbox = document.getElementById('numbers');
const savedNumbers = sessionStorage.getItem('NumbersCheck');

if (savedNumbers === 'false') {
    numbersCheckbox.checked = false;
}

numbersCheckbox.addEventListener('change', () => {
    const isChecked = numbersCheckbox.checked;
    sessionStorage.setItem('NumbersCheck', isChecked);
});

const symbolsCheckbox = document.getElementById('symbols');
const savedSymbols = sessionStorage.getItem('SymbolsCheck');

if (savedSymbols === 'false') {
    symbolsCheckbox.checked = false;
}

symbolsCheckbox.addEventListener('change', () => {
    const isChecked = symbolsCheckbox.checked;
    sessionStorage.setItem('SymbolsCheck', isChecked);
});

const alphaCheckbox = document.getElementById('alphabet');
const savedAlpha = sessionStorage.getItem('AlphaCheck');

if (savedAlpha === 'false') {
    alphaCheckbox.checked = false;
}

alphaCheckbox.addEventListener('change', () => {
    const isChecked = alphaCheckbox.checked;
    sessionStorage.setItem('AlphaCheck', isChecked);
});


