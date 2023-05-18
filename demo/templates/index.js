

document.querySelector('.submit-button').addEventListener('click', function() {
    var language = document.querySelector('.language-select').value;
    var solution = document.querySelector('.solution-area').value;
});

document.querySelector('.solution-area').value = 'package runtime_test;\npublic class Solution{\n    public static int twoSum(int a, int b){ \n\n    }\n}';

const languageSelect = document.getElementById('language-select');
console.log(languageSelect.value);
languageSelect.addEventListener('change', () => {
const selectedLanguage = languageSelect.value;


switch(selectedLanguage) {
    case 'java':
        document.querySelector('.solution-area').value = 'package runtime_test;\npublic class Solution{\n    public static int twoSum(int a, int b){ \n\n    }\n}';
        break;
    case 'js':
        document.querySelector('.solution-area').value = 'function twoSum(a, b){\n\n}\nmodule.exports = {twoSum};';
        break;
    case 'py':
        document.querySelector('.solution-area').value = 'def twoSum(a, b):\n\    pass';
        break;
    case 'cpp':
        document.querySelector('.solution-area').value = 'int twoSum(int a, int b){\n\n}';
        break;
}
});

const solutionArea = document.getElementById('solution-area');
const sendButton = document.getElementById('submit-button');

sendButton.addEventListener('click', function() {
    const solution = solutionArea.value;
    const data = { solution: solution, lang: languageSelect.value};
    const jsonData = JSON.stringify(data);
    fetch('http://localhost:8080/example', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: jsonData
    }).then(response => response.json())
    .then(data =>{
        console.log(data, "FromFetch");
        document.getElementById('report-status').innerHTML = data.status;
        document.getElementById('report-message').innerHTML = data.message;
    }).catch(error => {
        console.error('Error:', error);
    });

  
});

