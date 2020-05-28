import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
//import App from './App';
//import * as serviceWorker from './serviceWorker';
/*
function Tick() {
    const element = (<h1>{new Date().toLocaleTimeString()}</h1>);
    ReactDOM.render(element, document.getElementById('root'));

}
*/
/*
class Clock extends React.Component {
    constructor(props) {
        super(props);
        this.state = {date: new Date()};
    }

    componentDidMount() {
        this.timerID = setInterval(
            () => this.tick(),
            1000
        );
    }
    componentWillUnmount() {
        clearInterval(this.timerID);
    }
    tick() {
        this.setState ({
            date: new Date()
        });
    }
    render() {
        return (
            <div>
            <h1>Hello, world</h1>
            <h2>It is {this.state.date.toLocaleTimeString()}.</h2>
            </div>
        )
    }
}

function App() {
    return (
        <div>
            <Clock />
            <Clock />
            <Clock />
        </div>
    )
}

function ActionLink() {
    function handleClick(e) {
        e.preventDefault();
        console.log("The link was clicked.");
    }

    return (
        <a href="#" onClick={handleClick}> Click me </a>
    )
}

class Toggle extends React.Component {
    constructor(props) {
        super(props);
        this.state = {isToggleOn: true};

        // this binding is necessary to make `this` work in the callback
        this.handleClick = this.handleClick.bind(this);
    }

    handleClick() {
        this.setState(state => ({
            isToggleOn: !state.isToggleOn
        }));
    }

    render() {
        return (
            <button onClick={this.handleClick}>
                {this.state.isToggleOn ? 'ON' : 'OFF'}
            </button>
        );
    }
}

class LoggingButton extends React.Component {
    handleClick() {
        console.log("this is:", this);
    }

    render (){

        return (
            <button onClick={() => this.handleClick()}>
            Click Me
            </button>
        );
    }
}
*/


/*
 *
const numbers = [1, 2, 3, 4, 5];
const listItems = numbers.map((number) =>
    <li>{number}</li>
);

*/

/*
function NumberList(props) {
    const numbers = props.numbers;
    const listItems = numbers.map((number) =>
    <li key={number.toString()}>{number}</li>
    );
    return (
        <ul>{listItems}</ul>
    )
}

const numbers = [1, 2, ,3 ,4 ,5]

*/
/*
class NameForm extends React.Component {
    constructor(props) {
        super(props);
        this.state = {value: ''};

        this.handleChange = this.handleChange.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);
    }

    handleChange(event) {

        this.setState({value: event.target.value});
    }

    handleSubmit(event) {
        alert('A name was submitted: ' + this.state.value);
        event.preventDefalut();
    }

    render() {
        return(
            <form onSubmit={this.handleSubmit}>
                <label>
                Name:
                <input type="text" value={this.state.value} onChange={this.handleChange} />
                </label>
                <input type="Submit" value="Submit" />
            </form>
        );
    }
}
*/

class EssayForm extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            value: 'Please write an essay about your favorite DOM elemnt.'
        };

        this.handleChange = this.handleChange.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);
    }

    handleChange(event) {
        this.setState({value: event.target.value});
    }

    handleSubmit(event) {
        alert('An essay was submittee: ' + this.state.value);
        event.preventDefault();
    }

    render() {
        return(
            <form onSubmit={this.handleSubmit}>
                <label>
                Essay:
                <textarea value={this.state.value} onChange={this.handleChange} />
                </label>
                <input type="submit" value="Submit" />
            </form>
        );
    }


}
ReactDOM.render(
    <EssayForm />,
    document.getElementById('root')

);
/*
ReactDOM.render(
  <React.StrictMode>
   <Tick />
  </React.StrictMode>,
  document.getElementById('root')
);
*/
//setInterval(Tick, 100);
// If you want your app to work offline and load faster, you can change
// unregister() to register() below. Note this comes with some pitfalls.
// Learn more about service workers: https://bit.ly/CRA-PWA
//serviceWorker.unregister();
