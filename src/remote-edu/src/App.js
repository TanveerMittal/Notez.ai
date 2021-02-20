import './App.css';
import React, { Component } from "react";
import InputField from './components/InputField.js';

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      stage: '1',
    };
    this.handleClick = this.handleClick.bind(this);
    this.getTranscript = this.getTranscript.bind(this);
  }
  
  componentDidMount() {
    console.log('mount');
  }
  
  componentWillUnmount() {
    console.log('unmount');
  }

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

  handleClick() {
    console.log('Click happened');
    if (this.state.stage == '1') {
      this.setState({stage: '2'});
      var sampleText = "hello word";
      console.log(this.getTranscript(sampleText));
    } else {
      this.setState({stage: '1'});
    }
  }

  showFile = async (e) => {
    e.preventDefault()
    const reader = new FileReader()
    reader.onload = async (e) => { 
      const text = (e.target.result)
      console.log(text)
    };
    reader.readAsText(e.target.files[0])
  }

  render() {
    const curStage = this.state.stage;
    let stageComp;
    if (curStage == '1') {
      stageComp = <div>
        <InputField
          id={1}
          label="Zoom Transcript"
          predicted=""
          locked={false}
          active={false}
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
