export default class {
    /**
     * @param {HTMLTableElement} root The table element which will display the CSV data.
     */
    constructor(root) {
        this.root = root;
    }

    /**
     * 
     * @param {string[][]} data 
     * @param {string[]} headerColumns 
     */
    update(data, headerColumns = []) {
        this.clear();
        this.setHeader(headerColumns);
        this.setBody(data);
    }


    // Clears all contents of the table including the header
    clear() {
        this.root.innerHTML = "";
    }
    /**
     * 
     * @param {string[]} headerColumns List of headings to be used
     */
    setHeader(headerColumns) {
        this.root.insertAdjacentHTML("afterbegin", `
            <thead class="thead-dark">
                <tr class="data-row">
                    ${ headerColumns.map(text => `<th>${text}</th>`).join("") }
                </tr>
            </thead>
        `);
    }
    /**
     * 
     * @param {string[][]} data 
     */
    setBody(data) {
        const rowsHtml = data.map(row => {
            return `<tr>
                ${ row.map(text => `<td class="data-content">${ text }</td>`).join("") }
            </tr>
            `;
        });

        this.root.insertAdjacentHTML("beforeend", `
            <tbody class="data-body">
                ${ rowsHtml.join("") }
            </tbody>
        `)
    }
}
