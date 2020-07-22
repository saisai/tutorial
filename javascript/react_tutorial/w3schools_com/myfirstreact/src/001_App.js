//import React from 'react';
//import ReactDOM from 'react-dom';

import logo from './logo.svg';
import './App.css';

/*
class App extends React.Component {
  constructor() {
    super();
    this.state = {
		color: "blue",
		backgroundColor: "red",
		lineHeight: "30px"
		
		};
  }
  render() {
    return <h2 style={this.state}>I am a {this.state.color} Car!</h2>;
  }
}
*/

//function Oops extends React.Component{
/*
class Oopss extends React.Component {
	render() {
	return ( 
		<h1>Hello</h1> 
		);
	}
	
}

function Oops() {
	
	return (
	 "Hello "
	);
}

function Input() {
	
	return (
	'<input type="text" />'
	);
}

class Inputer extends React.Component {
	render() {
	return (
		<>
		<br />
		<input type="text" />
		<textarea></textarea>
		<select>
			<option>-</option>
			<option>hello </option>
		</select>
		</>
	);
	}
}

class Car extends React.Component {
  render() {
    return <h2>I am a {this.props.color}  {this.props.hello} Car!</h2>;
  }
}

function App() {
	return(
		<div>
		<Car color="red" hello="world" />
		<Car color="red" hello="world" />
		<Oops />
		<Input />
		<Inputer />
		</div>
		
	);
}

function Apps() {
  return (
   <table>
    <tr>
      <th>Name</th>
    </tr>
    <tr>
      <td>John</td>
    </tr>
    <tr>
      <td>Elsa</td>
    </tr>
  </table>
  );
}
*/

/*
class App extends React.Component {
  componentDidMount() {
    const apiUrl = 'https://api.github.com/users/hacktivist123/repos';
    fetch(apiUrl)
      .then((response) => response.json())
      .then((data) => console.log('This is your data', data));
  }
  render() {
    return <h1>my Component has Mounted, Check the browser 'console' </h1>;
  }
}
*/

import React, { useEffect, useState } from 'react';
import './App.css';
import List from './components/List';
import withListLoading from './components/withListLoading';

function App() {
  const ListLoading = withListLoading(List);
  const [appState, setAppState] = useState({
    loading: false,
    repos: null,
  });

  useEffect(() => {
    setAppState({ loading: true });
    const apiUrl = `https://api.github.com/users/hacktivist123/repos`;
    fetch(apiUrl)
      .then((res) => res.json())
      .then((repos) => {
        setAppState({ loading: false, repos: repos });
      });
  }, [setAppState]);
  
  return (
    <div className='App'>
      <div className='container'>
        <h1>My Repositories</h1>
      </div>
      <div className='repo-container'>
        <ListLoading isLoading={appState.loading} repos={appState.repos} />
      </div>
      <footer>
        <div className='footer'>
          Built{' '}
          <span role='img' aria-label='love'>
            💚
          </span>{' '}
          with by Shedrack Akintayo
        </div>
      </footer>
    </div>
  );
}

export default App;
