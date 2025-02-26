document.addEventListener("DOMContentLoaded", function() {
    const mysteryButton = document.getElementById("getMystery");
    const mysteryDisplay = document.getElementById("mysteryDisplay");

    const mysteries = [
        "Що завжди йде, але ніколи не приходить? (Час)",
        "Що має ключі, але не може відкрити жодні двері? (Клавіатура)",
        "Що можна розбити, навіть не торкаючись? (Обіцянка)"
    ];

    mysteryButton.addEventListener("click", function() {
        const randomIndex = Math.floor(Math.random() * mysteries.length);
        mysteryDisplay.textContent = mysteries[randomIndex];
    });
});