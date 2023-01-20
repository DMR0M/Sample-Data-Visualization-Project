import TableCSV from "./TableCSV.js";

const tableRoot = document.querySelector("#csvRoot");
const csvFileInput = document.querySelector("#csvFileInput");
const tableCsv = new TableCSV(tableRoot);

csvFileInput.addEventListener("change", e => {
    Papa.parse(csvFileInput.files[0], {
        delimiter: ",",
        skipEmptyLines: true,
        complete: results => {
            tableCsv.update(results.data.slice(1),
            results.data[0]);
        }
    });
});
