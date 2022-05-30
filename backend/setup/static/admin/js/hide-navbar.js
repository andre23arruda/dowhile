document.addEventListener("DOMContentLoaded", function() {
    setTimeout(() => {
        const node = document.querySelector('#nav-sidebar')
        if (node) {
            node.style.setProperty('transition', '0.1s')
            node.style.setProperty('opacity', '1')
        }
    }, 0.1);
});