// script.js

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

const numbersCheckbox = document.getElementById('numbers');
const symbolsCheckbox = document.getElementById('symbols');
const alphaCheckboxLower = document.getElementById('alphabet_lower');
const alphaCheckboxUpper = document.getElementById('alphabet_upper');

const checkboxes = [numbersCheckbox, symbolsCheckbox, alphaCheckboxLower, alphaCheckboxUpper];

checkboxes.forEach(checkbox => {
  checkbox.addEventListener('change', () => {
    const isChecked = checkbox.checked;
    sessionStorage.setItem(checkbox.id, isChecked);
  });

  const savedState = sessionStorage.getItem(checkbox.id);
  checkbox.checked = savedState === 'true';
});

if (password.textContent.length === 0) {
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
