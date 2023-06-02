const slideElement = document.querySelector('.slide');
const slideHeading = slideElement.querySelector('h2');
const slideParag = slideElement.querySelector('p')
let isLogin = false; 

slideElement.addEventListener('click', () => {
  slideElement.classList.toggle('slide-active');

  if (isLogin) {
    setTimeout(() => {
        if(slideHeading.textContent == 'Login'){
            slideHeading.textContent = 'Register';
            slideParag.textContent = 'click to register';
        }else{
            slideHeading.textContent = 'რეგისტრაცია';
            slideParag.textContent = 'რეგისტრაციისთვის დააკლიკეთ';
        }
    }, 500);
    isLogin = false;
  } else {
    setTimeout(() => {
        if(slideHeading.textContent == 'Register'){
            slideHeading.textContent = 'Login';
            slideParag.textContent = 'click to login'
            console.log('here')
        }else{
            slideHeading.textContent = 'შესვლა';
            slideParag.textContent = 'შესასვლელად დააკლიკეთ'
        }
    }, 500);
    isLogin = true;
  }
});

