// from data.js
var tableData = data;

// YOUR CODE HERE!
let tableSelect = d3.select('tbody');

tableData.forEach(city => {
    let row = tableSelect.append('tr');
    Object.entries(city).forEach(([key, value]) => {
       let td = tableSelect.append('td').text(value);
    })
});

let filterBtnSelect = d3.select('#filter-btn');

filterBtnSelect.on('click', function() {
    let inputElement = d3.select('#datetime');

    let inputValue = inputElement.property('value');
    
    let filterDate = tableData.filter(date => date.datetime === inputValue);
    console.log(filterDate);
    tableSelect.html('');

    filterDate.forEach(city => {
        let row = tableSelect.append('tr');
        Object.entries(city).forEach(([key, value]) => {
           let td = tableSelect.append('td').text(value);
        });
    });
});