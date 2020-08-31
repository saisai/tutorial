import React from 'react';
import logo from './logo.svg';
import './App.css';

import ClassCounter from './components/ClassCounter'
import HookCounter from './components/HookCounter'
import HookCounterTwo from './components/HookCounterTwo'
import HookCounterThree from './components/HookCounterThree'
import HookCounterFour from './components/HookCounterFour'
import ClassCounterOne from './components/ClassCounterOne'
import HookCounterOne from './components/HookCounterOne'
import ClassMouse from './components/ClassMouse'
import HookMouse from './components/HookMouse'
import MouseContainer from './components/MouseContainer'

function App() {
  return (
    <div className="App">
	{ /*
      <ClassCounter />
      <HookCounter />
      <HookCounterTwo />
<HookCounterThree />
      <HookCounterFour />
      <ClassCounterOne />
      <HookCounterOne />
      <ClassMouse />	
	<HookMouse />	  
	  */
	}
      
      
      <MouseContainer />
	  
    </div>
  );
}

export default App;
