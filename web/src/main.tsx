import React from 'react'
import ReactDOM from 'react-dom/client'
import { ToastContainer } from 'react-toastify'
import 'react-toastify/dist/ReactToastify.css'

import App from './App'
import { AuthProvider } from './contexts/auth'
import './index.scss'

ReactDOM.createRoot(document.getElementById('root')!).render(
    // <React.StrictMode>
        <AuthProvider>
            <App />
			<ToastContainer />
        </AuthProvider>
    // </React.StrictMode>
)
