const showBtn = document.querySelector('.password_box button');
const password = document.querySelector('.password_box input');
showBtn.addEventListener('click', () => {
    if (password.type === "password") {
        showBtn.style.backgroundImage = "../img/eye.png";
        password.type = "text";
    } else {
        showBtn.style.backgroundImage = "../img/hidden.png";
        password.type = "password";
    }
});