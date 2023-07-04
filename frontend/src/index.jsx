import App from './App';
import React from 'react';
import ReactDOM from 'react-dom/client';
import './CSS/global.css';

// NOTE: Remove the strict mode in production.

ReactDOM.createRoot(document.getElementById("root")).render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);
