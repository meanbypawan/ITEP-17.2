import { Component } from "react";
import Home from "./components/Home";
import CounterComp from "./components/CounterComp";
class App extends Component{
  constructor(){
    super();
    this.state = {
      counter: 100
    };
    console.log("App constructor called..");
  }
  componentDidMount(){
    console.log("App-componentDidMount()- executed..");
  }
  componentDidUpdate(){
    console.log("App - componentDidUpdate()- executed...");
  }
  componentWillUnmount(){
    console.log("App-componentWillUnMount()-executed..");
  }
  render(){
    console.log("App render executed...");
    return <>
       <h1>App component...{this.state.counter}</h1>
       <button onClick={()=>this.setState({counter: this.state.counter+1})}>Increment Counter</button>
       <Home/>
       <CounterComp/>
    </>
  }
}

export default App;