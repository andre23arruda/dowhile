import { useContext } from 'react'
import { VscGithubInverted } from 'react-icons/vsc'
import { AuthContext } from '../../contexts/auth'

import seal from '../../assets/seal.svg'
import styles from './LoginBox.module.scss'

export default function LoginBox() {
	const { signInUrl } = useContext(AuthContext)

	return (
		<div className={ styles.loginBox }>
			<img className={ styles.seal } src={ seal } />

			<strong>Entre e compartilhe sua mensagem</strong>

			<a href={ signInUrl }>
				<VscGithubInverted size={ 24 }/>
				Entre com Github
			</a>
		</div>
	)
}
