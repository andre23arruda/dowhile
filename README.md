<h1 align="center">
    <img alt="Widget" src=".github/logo.svg" width="300px" />
</h1>

<h4 align="center">
  🚀 Next Level Week Heat
</h4>


<p align="center">
  <a href="#-tecnologias">Tecnologias</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#-projeto">Projeto</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#instalação">Instalação</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#telas">Telas</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#exemplo">Exemplo</a>
</p>

## 🚀 Tecnologias

Esse projeto foi desenvolvido com as seguintes tecnologias:

- [Django](https://www.djangoproject.com/)
- [Django-Rest-Framework](https://www.django-rest-framework.org/)
- [React](https://reactjs.org)
- [React Native](https://facebook.github.io/react-native/)
- [Expo](https://expo.io/)

## 💻 Projeto
**Aplicação de crachá virtual para enviar mensagens sobre o DOWHILE 2021.**

## Instalação
### Pré requisitos
Ter instalado:
- [Python](https://www.python.org/downloads/)
- [Node](https://nodejs.org/en/download/)
- [Yarn](https://classic.yarnpkg.com/en/docs/install/)
- [Expo](https://docs.expo.dev/get-started/installation/)

### Clonar projeto
#### No terminal, rodar
```sh
git clone https://github.com/andre23arruda/dowhile2021
```

### Backend
#### No terminal, rodar:
```sh
# Entrar na pasta dos arquivos do backend
cd backend

# Renomear env_example.py para env.py
cp setup/env_example.py setup/env.py
# ADICIONE OS VALORES CORRETOS

# Criar um ambiente virtual
python -m venv venv

# Ativar o ambiente virtual
. activate.sh
# ou
. venv/Scripts/activate # windows
. venv/bin/activate # linux

# Instalar os pacotes necessários
pip install -r requirements.txt

# Executar as migrações
python manage.py migrate

# Rodar backend
python manage.py runserver
```

### Web
#### No terminal, rodar
```sh
# Entrar na pasta dos arquivos
cd web

# Renomear env_example para .env.local
cp env_example .env.local
# ADICIONE OS VALORES CORRETOS

# Instalar os pacotes necessários
yarn install

# Rodar
yarn dev
```

<div align="center">
    <img alt="Screen 1" title="Screen 1" src=".github/web_1.jpg?raw=true" width="400px" />
</div>
<p align="center">Screen 1</p>
<hr>

<div align="center">
    <img alt="Screen 2" title="Screen 2" src=".github//web_2.jpg?raw=true" width="400px" />
</div>
<p align="center">Screen 2</p>
<hr>

<div align="center">
    <img alt="Screen 3" title="Screen 3" src=".github//web_3.jpg?raw=true" width="400px" />
</div>
<p align="center">Screen 3</p>
<hr>

## Exemplo
<a href="https://andrearruda-dowhile.vercel.app/" target="_blank">Visitar</a>