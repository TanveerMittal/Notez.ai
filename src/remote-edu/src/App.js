import './App.css';
import React, { Component } from "react";
import InputField from './components/InputField.js';
import SignIn from './components/SignIn.js';

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      stage: '0',
      user: '',
      text: '',
      type: '',
      inputBlock: '0',
    };
    this.handleClick = this.handleClick.bind(this);
    this.auth = this.auth.bind(this);
  }
  
  componentDidMount() {
    console.log('mount');
  }
  
  componentWillUnmount() {
    console.log('unmount');
  }

  // ProcessText button event
  handleClick() {
    console.log('Click happened');
    // send transcript data to backend
    // bad input checker here
    console.log(this.state)
    if (this.state.stage == '1') {
      this.setState({stage: '2'});
    } else {
      this.setState({stage: '1'});
    }
  }

  // Input File
  showFile = async (e) => {
    
    e.preventDefault()
    const reader = new FileReader()
    reader.onload = async (e) => { 
      const text = (e.target.result)
      this.setState({text: text})
    };
    reader.readAsText(e.target.files[0])
    var type = e.target.files[0].type
    this.setState({type: type})
    console.log(type)
    this.setState({inputBlock: '1'})
  }

  // login click event
  auth(){
    this.setState({stage: '1'});
  }

  // Login set
  userSet = (data) => {
    this.setState({user: data})
  }

  inputText = (data) => {
    if(this.state.inputBlock == '0'){
      this.setState({text: data})
      this.setState({type: 'text/plain'})
    }
  }

  render() {
    const curStage = this.state.stage;
    let stageComp;
    if (curStage == '0') {
      stageComp = <div>
        <SignIn
          auth = {this.auth} 
          onchange={(e) => {this.userSet(e)}}
        />
      </div>;
    } else if (curStage == '1') {
      stageComp = <div>
        <InputField
          id={1}
          label="Zoom Transcript"
          predicted=""
          locked={false}
          active={false}
          onchange={this.inputText}
        />
        <div><input type="file" onChange={(e) => this.showFile(e)} /></div>
        <button onClick={this.handleClick}>Process Text</button>
      </div>;
    } else if (curStage == '2') {
      stageComp = <div> 
        <div>Rudy Gillespie</div>
        <button onClick={this.handleClick}>Go Back</button>
      </div>;
    } else if (curStage == '3') {
      // TODO
    } else {
      // TODO
    }
    
    return (
      <div className="App">
        <header className="App-header">
          <p>Zoom Tutor</p>
          {stageComp}
        </header>
      </div>
    );
  }
}

export default App;
