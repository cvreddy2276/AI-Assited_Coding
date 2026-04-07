// task5.js - Convert HTML content to JavaScript

// Define the page content as JavaScript objects
const pageContent = {
    title: "Document",
    heading: "hello everyone",
    paragraphs: [
        "this is my first html code",
        "i am learning html",
        "i am enjoying it"
    ]
};

// Function to generate HTML from JavaScript data
function generateHTML() {
    let html = `<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>${pageContent.title}</title>
</head>
<body>
    <h1>${pageContent.heading}</h1>
`;

    // Add paragraphs
    pageContent.paragraphs.forEach(para => {
        html += `    <p>${para}</p>\n`;
    });

    html += `</body>
</html>`;

    return html;
}

// Function to dynamically render content in browser (if running in DOM)
function renderToDOM() {
    if (typeof document !== 'undefined') {
        // Create heading
        const heading = document.createElement('h1');
        heading.textContent = pageContent.heading;
        document.body.appendChild(heading);

        // Create paragraphs
        pageContent.paragraphs.forEach(text => {
            const para = document.createElement('p');
            para.textContent = text;
            document.body.appendChild(para);
        });
    }
}

// Export for Node.js or use in browser
if (typeof module !== 'undefined' && module.exports) {
    module.exports = { pageContent, generateHTML, renderToDOM };
}
