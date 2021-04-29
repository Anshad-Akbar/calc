function calc(value) {
    num1 = Number(document.getElementById('txt1').value)

    document.getElementById('txt1').value = num1
    document.getElementById('txt1').value = "  "
    sign = value
}


function res() {
    num2 = Number(document.getElementById('txt1').value)
    document.getElementById('txt1').value = " "

    if (sign == '+') {
        sum = num1 + num2 + num3
        document.getElementById('txt1').value = sum

    } else if (sign == '-') {
        sum = num1 - num2
        document.getElementById('txt1').value = sum


    } else if (sign == '/') {
        sum = num1 / num2
        document.getElementById('txt1').value = sum

    } else if (sign == '*') {
        sum = num1 * num2
        document.getElementById('txt1').value = sum
    }

}


function clr() {
    document.getElementById('txt1').value = "  "
}