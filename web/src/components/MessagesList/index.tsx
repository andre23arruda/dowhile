import { useEffect, useState } from 'react'
import { toast } from 'react-toastify'
import { getApi } from '../../services/api'
import { toastConfig } from '../../utils/toast'

// styles and images
import styles from './MessagesList.module.scss'
import logo from '../../assets/logo.svg'

type MessageType = {
	id: number,
	user_name: string,
	user_avatar: string,
	text: string,
}

type Props = {
	trigger: any
}

export default function MessagesList({ trigger }: Props) {
	const [messages, setMessages] = useState<MessageType[]>([])
	const [cloud, setCloud] = useState('')

	async function loadCloud() {
		if (cloud) {
			setCloud('')
			return
		}
		toast(
			'Gerando imagem',
			toastConfig
		)
		const { status, data } = await getApi('nlw_heat/messages/word_cloud/')
		setCloud(data.image)
	}

	useEffect(() => {
		async function loadMessages() {
			const { status, data } = await getApi('nlw_heat/messages/last_3/')
			setMessages(data as  MessageType[])
		}
		loadMessages()
	}, [trigger])

	return (
		<div className={ styles.messagesListContainer }>
			<img className={ styles.logo } src={ logo } alt="DoWhile 2021" />

			<button
				onClick={ loadCloud }
			>
				{ cloud ? 'Mensagens' : 'Nuvem de palavras' }
			</button>

			{ cloud ? (
				<div className={ styles.cloudImg }>
					<img
						src={ cloud }
						alt="Nuvem de palavras"
					/>
				</div>
			) : (
				<ul className={ styles.messagesList }>
					{ messages.map(message => (
						<li key={ message.id } className={ styles.message }>
							<p>{ message.text }</p>

							<div className={ styles.messageUser }>
								<div className={ styles.userImage }>
									<img src={ message.user_avatar } alt={ message.user_name } />
								</div>

								<span>{ message.user_name }</span>
							</div>
						</li>
					))}
				</ul>
			)}
		</div>
	)
}
