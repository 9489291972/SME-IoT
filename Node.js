const express = require('express');
const app = express();

// Define the port number
const PORT = 5050;

// Define the hostname (optional in most cases, default is localhost)
const HOST = '127.0.0.1'; // This is the IP address for localhost

// Start the server
app.listen(PORT, HOST, () => {
    console.log(`Server is running on http://${HOST}:${PORT}`);
});
