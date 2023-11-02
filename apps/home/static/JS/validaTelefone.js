
var inputTelefone = document.getElementById("cell_phone");

// Adiciona um ouvinte de evento para o evento de digitaÃ§Ã£o
inputTelefone.addEventListener("input", function () {
    // Remove caracteres nÃ£o numÃ©ricos
    var numeroTelefone = inputTelefone.value.replace(/\D/g, "");

    // Limita o nÃºmero a 11 dÃ­gitos
    if (numeroTelefone.length > 12) {
        numeroTelefone = numeroTelefone.substring(0, 11);
    }

    // Verifica se o nÃºmero possui um DDD e adiciona parÃªnteses
    if (numeroTelefone.length > 2) {
        numeroTelefone = "(" + numeroTelefone.substring(0, 2) + ") " + numeroTelefone.substring(2);
    }

    // Verifica se o nÃºmero possui 9 dÃ­gitos e adiciona um hÃ­fen
    if (numeroTelefone.length > 10) {
        numeroTelefone = numeroTelefone.substring(0, 10) + "-" + numeroTelefone.substring(10, 15);
    }

    // Atualiza o valor do campo de entrada com o nÃºmero formatado
    inputTelefone.value = numeroTelefone;
});