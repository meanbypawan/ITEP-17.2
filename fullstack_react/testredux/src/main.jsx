import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import App from './App.jsx'
import { Provider } from 'react-redux'
import MyStore from "./redux-config/mystore.js"
createRoot(document.getElementById('root')).render(
<Provider store={MyStore}>
   <App />
</Provider>
)

