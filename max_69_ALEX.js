/**
 * @param {number} num
 * @return {number}
 */
var maximum69Number  = function(num) {
    let strNum = ''+ num;
    let numMem = 0;

    if(strNum.indexOf("6") === -1)
    {
        return num;
    }

    for (let index = 0; index < strNum.length; index++) {

        let strNumToEval = "";
        
        if(strNum[index] === '9')
        {
            strNumToEval = strNum.replace(strNum[index],"6");
        }
        else
        {
            strNumToEval = strNum.replace(strNum[index],"9");
        }

        let newNum = parseInt(strNumToEval);

        if(newNum > numMem)
        {
            numMem = newNum;
        }
    }

    return numMem;
};

console.log(maximum69Number(99))