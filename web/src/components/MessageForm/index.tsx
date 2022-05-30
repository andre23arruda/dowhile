import { FormEvent, useContext, useState } from 'react'
import { toast } from 'react-toastify'
import { VscGithubInverted, VscSignOut } from 'react-icons/vsc'
import { AuthContext } from '../../contexts/auth'
import { postApi } from '../../services/api'
import { toastConfig } from '../../utils/toast'

import seal from '../../assets/seal.svg'
import styles from './MessageForm.module.scss'


type Props = {
	trigger: () => void
}

export default function MessageForm({ trigger }: Props) {
	const { user, signOut } = useContext(AuthContext)
	const [text, setText] = useState('')

	async function submitMessage(event: FormEvent) {
		event.preventDefault()
		console.log('teste')
		const token = localStorage.getItem('dowhileToken') || ''
		const formData = {
			text
		}
		const { status, data } = await postApi('nlw_heat/messages/', formData, token)
		console.log(data)
		setText('')
		toast(
			'Mensagem enviada com sucesso!',
			toastConfig
		)
		trigger()
	}

	function validateForm() {
		return text.trim().length > 0
	}

	return (
		<div className={ styles.messageFormContainer }>
			<img className={ styles.seal } src={ seal } />

			<button
				className={ styles.signOutButton }
				onClick={ signOut }
			>
				<VscSignOut size={ 32 } />
			</button>

			<header className={ styles.userInformation }>
				<div className={ styles.userImage }>
					<img src={ user?.avatar } alt={ user?.username } />
				</div>

				<strong>{ user?.name }</strong>

				<span>
					<VscGithubInverted size={ 16 } />

					{ user?.username }
				</span>
			</header>

			<form onSubmit={ submitMessage }>
				<label htmlFor="message">Mensagem</label>

				<textarea
					id="message"
					name="message"
					placeholder="Qual sua expectativa para o evento?"
					maxLength={ 140 }
					value={ text }
					onChange={ event => setText(event.target.value) }
				/>

				<button
					type="submit"
					disabled={ !validateForm() }
				>
					Enviar mensagem
				</button>
			</form>
		</div>
	)
}
