#!/bin/bash
# run with `. create.sh`

PWD=`pwd`

run () {
	mkdir ./src/components/Example
	echo "import styles from './Example.module.scss'

export default function Example() {
	return (
		<h1>Hello world</h1>
	)
}" >> ./src/components/Example/index.tsx
	touch ./src/components/Example/Example.module.scss
}

run