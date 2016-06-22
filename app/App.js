import React, { Component } from 'react';
import { render } from 'react-dom';

import { get } from 'jquery'

let predicateStyles = {
  fontWeight: 'bold',
  fontSize: '16px',
  color: 'red'
}

let subjectStyles = {
  fontWeight: 'bold',
  fontSize: '16px',
  color: 'blue'
}

class App extends Component {
  constructor(props){
    super(props);

    this.state = {
      subject: '',
      predicate: ''
    };

    this.generateNewSentence = this.generateNewSentence.bind(this);
  }

  componentDidMount(){
    this.generateNewSentence();
  }

  generateNewSentence(){
    get('/sentence')
      .done((response) => {
        // console.log(response);
        this.setState({
          'subject': response.subject,
          'predicate': response.predicate
        });
      });
  }

  render(){
    return (
      <div>
        <div className="sentence">
          <span className="subject" style={subjectStyles}>{this.state.subject}</span>
          &nbsp;
          <span className="predicate" style={predicateStyles}>{this.state.predicate}</span>
        </div>
        <button className="btn btn-primary" onClick={this.generateNewSentence}>Generate</button>
      </div>
    );
  }
}

render(<App/>, document.getElementById('root'));
