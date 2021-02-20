import './App.css';
import React, { Component } from "react";
import InputField from './components/InputField.js';

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      stage: '',
    };
  }
  
  componentDidMount() {
    console.log('mount');
  }
  
  componentWillUnmount() {
    console.log('unmount');
  }

  nextClicked() {
    this.setState({
      stage: 'y'
    });
  }
  render() {
    return (
      <div className="App">
        <header className="App-header">
          <p>Zoom Tutor</p>
          <InputField
            id={1}
            label="Zoom Transcript"
            predicted=""
            locked={false}
            active={false}
          />
        </header>
      </div>
    );
  }
}

export default App;
