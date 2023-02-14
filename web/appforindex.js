console.error("STOP")
console.log("if you are pasting something into this console, the chances that you are doing something dangerous is 20/10")
//start observer
const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
        if (entry.isIntersecting) {
            entry.target.classList.add('show');
        } else{
            entry.target.classList.remove('show');
        }
    });
});


const Elements = document.querySelectorAll('.hidden');

Elements.forEach((el) => observer.observe(el));



