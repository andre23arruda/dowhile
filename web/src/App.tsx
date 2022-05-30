import { useCallback, useContext, useState } from 'react'

import MessageForm from './components/MessageForm'
import MessagesList from './components/MessagesList'
import LoginBox from './components/LoginBox'

import { AuthContext } from './contexts/auth'

import styles from './App.module.scss'

function App() {
    const { user } = useContext(AuthContext)
    const [messagesTrigger, setMessagesTrigger] = useState({})
    const trigger = useCallback(() => setMessagesTrigger({}), [])

    const styleApp = `${ styles.appContainer } ${ user ? styles.background : '' }`
    return (
        <main className={ styleApp }>
            <MessagesList trigger={ messagesTrigger } />

            { user ? (
                <MessageForm trigger={ trigger }/>
            ) : (
                <LoginBox />
            )}
        </main>
    )
}

export default App
