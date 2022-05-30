import { createContext, ReactNode, useEffect, useState } from 'react'
import { getApi, postApi } from '../services/api'

type User = {
    avatar: string,
    name: string,
    username: string,
}

type AuthResponse = {
	avatar: string,
	name: string,
	token: string,
	username: string,
}

type AuthContextData = {
    user: User | null,
    signInUrl: string,
    signOut: () => void,
}

export const AuthContext = createContext({} as AuthContextData)

type AuthProviderType = {
    children: ReactNode
}

export function AuthProvider(props: AuthProviderType) {
    const [user, setUser] = useState<User | null>(null)
    const signInUrl = `https://github.com/login/oauth/authorize?client_id=${ import.meta.env.VITE_CLIENT_ID }`
	const codeParam = '/?code='

	async function signIn(code: string) {
		const { status, data } = await postApi(`github-auth${ codeParam }${ code }`, {})
		const { token, ...user } = data
        // console.log(token)
		localStorage.setItem('dowhileToken', token)
        setUser(user)
	}

	async function signOut() {
		localStorage.removeItem('dowhileToken')
        setUser(null)
	}

    useEffect(() => {
		const currentUrl = window.location.href
		if (currentUrl.includes(codeParam)) {
			const [baseUrl, code] = currentUrl.split(codeParam)
			console.log(code)
			window.history.pushState({}, '', baseUrl)
			signIn(code)
		}
	}, [])

	useEffect(() => {
        async function getProfile() {
            const dowhileToken = localStorage.getItem('dowhileToken') || ''
            if (dowhileToken) {
                const { status, data } = await getApi(`nlw_heat/profiles/`, dowhileToken)
                if (status >= 400) {
                    signOut()
                    return
                }
                setUser(data)
            }
        }
        if (!user) {
            getProfile()
            return
        }
	}, [])

    return (
        <AuthContext.Provider
            value={{
                signInUrl,
                user,
                signOut
            }}
        >
            { props.children }
        </AuthContext.Provider>
    )
}