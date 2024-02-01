// let result = 5
const resultElement = document.getElementById('result')
console.log(resultElement.value)
const inputElement = document.getElementById('input1')

/*{ <input onchange="if(this.value > 0 and this.value < {{ count }}) {CBXPRShop.counItemUpdate('4881', this.value)} else {return false}" value='1'> }*/



const submitBtn = document.getElementById('submit')
submitBtn.onclick = function()  {
    const result = Number(inputElement.value) * 500
    resultElement.textContent = result
    console.log(result)
}
// console.log(result)
{/* <input type="number" id="input1" value="1" > */}
