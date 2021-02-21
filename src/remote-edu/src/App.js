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
<<<<<<< HEAD
    this.auth = this.auth.bind(this);
=======
    this.getTranscript = this.getTranscript.bind(this);
>>>>>>> da2242774ae6b25b83e157ee8ba3b3df5b04a62a
  }
  
  componentDidMount() {
    console.log('mount');
  }
  
  componentWillUnmount() {
    console.log('unmount');
  }

<<<<<<< HEAD
  // ProcessText button event
=======
  getTranscript(name) {
    // TODO: Fix "Cross-Origin Request Blocked: The Same Origin Policy disallows reading the remote resource at http://127.0.0.1:5000/receive-transcript."
    var API = "http://localhost:5000";
    return fetch(API + '/receive-transcript/' + name + '/' + 'txt')
    // var body = {
    //   transcript_data: name,
    //   file_extension: "txt",
    // }
    // console.log(JSON.stringify(body));
    // return fetch(API + "/receive-transcript", {
    //   method: 'POST',
    //   body: JSON.stringify(body)
    // })
  }

>>>>>>> da2242774ae6b25b83e157ee8ba3b3df5b04a62a
  handleClick() {
    console.log('Click happened');
    // send transcript data to backend
    // bad input checker here
    console.log(this.state)
    if (this.state.stage == '1') {
      this.setState({stage: '2'});
      var sampleText = "hello word";
      console.log(this.getTranscript(sampleText));
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
