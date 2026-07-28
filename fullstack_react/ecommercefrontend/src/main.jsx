import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import App from './App.jsx'
import { BrowserRouter } from 'react-router-dom'
import "react-toastify/dist/ReactToastify.css";
import { Provider } from 'react-redux';
import store from "./redux-config/store.js"
createRoot(document.getElementById('root')).render(
<BrowserRouter>
  <Provider store={store}>
    <App />
  </Provider>  
</BrowserRouter>
)