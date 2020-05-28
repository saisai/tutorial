import React from 'react';
import logo from './logo.svg';
import './App.css';
/*
function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
    </div>

  );
}

*/

function formatName(user) {
    return user.firstName + " " + user.lastName;
}

const user = {
    firstName: "Harper",
    lastName: "Perez"
}

const element = (
    <h1>
    Hello, {formatName(user)}!
    </h1>
)
function App2() {
    return (
        element
    )
}

function Welcome(props) {
    return <h4>Hello, {props.name} </h4>
}

const element2 = <Welcome name="Sara" />;
function App3() {
    return element2;
}

function App4() {
    return (
        <div>
        <Welcome name="Sara" />
        <Welcome name="Chal" />
        <Welcome name="Edite" />
        </div>

    );
}
/*
function tick() {
    return  (
        <div>
        <h1>Hello, world </h1>
        <h2>It is {new Date().toLocaleTimeString()}.</h2>
        </div>
    );
}

function App() {
    return tick();
}

setInterval(tick, 1);



export default App;
*/

function Clock(props) {
    return (
        <div>
            <h1>Hello, world</h1>
            <h2>It is {props.date.toLocaleTimeString()}.</h2>
        </div>
    )
}

function tick() {
    ReactDOM.render(
         <Clock date={new Date()} />,
        document.getElmentById('root')
    );

}



//export default App;

setInterval(tick, 1000);
