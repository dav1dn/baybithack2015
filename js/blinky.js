(function () {
    var words = ['cryptocurrencies', 'blockchains', 'bitcoin', 'digital currency'];
    var currentIndex = 3;
    var colors = ['#004777', '#efd28d', '#00afb5', '#a30000'];
    var element = document.getElementById('anim-text');
    function highlightCurrent() {
        element.style.backgroundColor = colors[Math.floor(Math.random() * colors.length)];
        element.style.color = '#f7f7f7';
        setTimeout(deleteCurrent, Math.random() * 1000 + 250);
    }

    function deleteCurrent() {
        element.innerHTML = '';
        element.style.backgroundColor = '';
        element.style.color = '#ff9900';
        setTimeout(typeNewWord, Math.random() * 3000 + 500);
    }

    function typeNewWord() {
        currentIndex++;
        var newWord = words[currentIndex % words.length];
        var index = 0;
        
        function TypeNextLetter(word, index) {
            console.log(index);
            if (index >= word.length) {
                setTimeout(highlightCurrent, Math.random() * 2000 + 2000);
            } else {
                console.log(element.innerHTML + ' + ' + word[index] );
                element.innerHTML = element.innerHTML + word[index];
                index++;
                setTimeout(function() {TypeNextLetter(word, index) }, Math.random()*250);
            }
        }

        TypeNextLetter(newWord, index);
    }

    setTimeout(function(){highlightCurrent();}, 3000);
})();
