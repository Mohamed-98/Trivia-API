# Full Stack Trivia API  Frontend

## Getting Setup

> _tip_: this frontend is designed to work with [Flask-based Backend](../backend). It is recommended you stand up the backend first, test using Postman or curl, update the endpoints in the frontend, and then the frontend should integrate smoothly.

### Installing Dependencies

#### Installing Node and NPM

This project depends on Nodejs and Node Package Manager (NPM). Before continuing, you must download and install Node (the download includes NPM) from [https://nodejs.com/en/download](https://nodejs.org/en/download/).

#### Installing project dependencies

This project uses NPM to manage software dependencies. NPM Relies on the package.json file located in the `frontend` directory of this repository. After cloning, open your terminal and run:

```bash
npm install
```

>_tip_: **npm i** is shorthand for **npm install**


## Running Your Frontend in Dev Mode

The frontend app was built using create-react-app. In order to run the app in development mode use ```npm start```. You can change the script in the ```package.json``` file. 

Open [http://localhost:3000](http://localhost:3000) to view it in the browser. The page will reload if you make edits.<br>

```bash
npm start
```
## File directory tree structure
```
.
├── README.md
├── package-lock.json
├── package.json
├── public
│   ├── art.svg
│   ├── delete.png
│   ├── entertainment.svg
│   ├── favicon.ico
│   ├── geography.svg
│   ├── history.svg
│   ├── index.html
│   ├── manifest.json
│   ├── science.svg
│   └── sports.svg
└── src
    ├── App.js
    ├── App.test.js
    ├── components
    │   ├── FormView.js
    │   ├── Header.js
    │   ├── Question.js
    │   ├── QuestionView.js
    │   ├── QuizView.js
    │   ├── Search.js
    │   ├── art.svg
    │   ├── entertainment.svg
    │   ├── geography.svg
    │   ├── history.svg
    │   ├── science.svg
    │   └── sports.svg
    ├── index.js
    ├── logo.svg
    ├── serviceWorker.js
    └── stylesheets
        ├── App.css
        ├── FormView.css
        ├── Header.css
        ├── Question.css
        ├── QuizView.css
        └── index.css
```
4 directories, 36 files
