var fact = require("./factorial");

exports.factorial = function(num) {
    if(num === 1){return 1}
    return num * fact.factorial(num - 1)
};